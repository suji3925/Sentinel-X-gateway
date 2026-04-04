from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
import datetime
import requests
import logging

from database import SessionLocal, SecurityLog, init_db
from alerts import notify_admin

app = FastAPI(title="Sentinel-X SOC Edition")
init_db()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("SENTINEL-X")

def get_geo_data(ip: str):
    """Forensic lookup for IP location and GPS."""
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
        data = response.json()
        if data.get("status") == "success":
            return {
                "location": f"{data.get('city')}, {data.get('country')}",
                "lat": data.get('lat', 0.0),
                "lon": data.get('lon', 0.0)
            }
    except:
        pass
    return {"location": "Unknown", "lat": 0.0, "lon": 0.0}

@app.middleware("http")
async def sentinel_middleware(request: Request, call_next):
    db = SessionLocal()
    ip = request.client.host
    path = request.url.path
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 1. IAM ENFORCEMENT: Check if IP is already BANNED
    banned_entity = db.query(SecurityLog).filter(SecurityLog.ip_address == ip, SecurityLog.status == "BANNED").first()
    if banned_entity:
        logger.warning(f"BLOCKED ACCESS: Banned IP {ip} attempted to reach {path}")
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN, 
            content={"detail": "ACCESS DENIED: ENTITY BLACKLISTED DUE TO PREVIOUS VIOLATIONS"}
        )

    # 2. HONEYPOT DETECTION (Active Defense)
    honeypot_traps = ["/admin", "/.env", "/wp-login.php", "/config", "/shell", "/phpmyadmin", "/root"]
    is_attack = path in honeypot_traps or "/etc/" in path or ".php" in path.lower()

    if is_attack:
        geo = get_geo_data(ip)
        
        log = db.query(SecurityLog).filter(SecurityLog.ip_address == ip).first()
        if not log:
            log = SecurityLog(
                ip_address=ip,
                status="BANNED",
                last_seen=timestamp,
                location=geo['location'],
                lat=geo['lat'],
                lon=geo['lon'],
                attempts=1,
                last_path=path
            )
            db.add(log)
        else:
            log.attempts += 1
            log.status = "BANNED"
            log.last_seen = timestamp
            log.last_path = path

        db.commit()
        
        # SOC Alerting
        notify_admin(ip, path, geo['location'], geo['lat'], geo['lon'])
        
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN, 
            content={
                "error": "SENTINEL-X SECURITY VIOLATION",
                "message": "Unauthorized access attempt detected. Your identity has been logged and blacklisted."
            }
        )

    response = await call_next(request)
    db.close()
    return response

@app.get("/")
async def home():
    return {"status": "Sentinel-X Active", "mode": "SOC/IAM Monitoring"}

@app.get("/logs")
async def view_logs():
    db = SessionLocal()
    logs = db.query(SecurityLog).all()
    db.close()
    return logs