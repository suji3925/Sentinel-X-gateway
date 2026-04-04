import requests

TOKEN = "YOUR TELEGRAM TOKEN"
CHAT_ID = "TELEGRAM_CHAT_ID"

def notify_admin(ip, path, location, lat, lon):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    
    message = (
        f"🛡️ **SENTINEL-X: INTRUSION DETECTED**\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"👤 **ATTACKER IP:** `{ip}`\n"
        f"📍 **LOCATION:** {location}\n"
        f"🌍 **GPS COORDS:** `{lat}, {lon}`\n"
        f"📂 **TARGET PATH:** `{path}`\n\n"
        f"🔗 [VIEW INVESTIGATION MAP](https://www.google.com/maps?q={lat},{lon})\n"
        f"🚫 **STATUS:** PERMANENTLY BANNED\n"
        f"━━━━━━━━━━━━━━━━━━━━━━"
    )
    
    try:
        requests.post(url, json={"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"})
    except Exception as e:
        print(f"Telegram Alert Failed: {e}")