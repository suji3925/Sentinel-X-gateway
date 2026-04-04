from sqlalchemy import Column, String, Integer, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./sentinel_vault.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class SecurityLog(Base):
    __tablename__ = "security_logs"
    
    ip_address = Column(String, primary_key=True)
    status = Column(String, default="BANNED")
    last_seen = Column(String)
    location = Column(String, default="Unknown")
    lat = Column(Float, default=0.0)
    lon = Column(Float, default=0.0)
    attempts = Column(Integer, default=1)
    last_path = Column(String, default="Unknown")

def init_db():
    Base.metadata.create_all(bind=engine)