## PROJECT: 🛡️ Sentinel-X-Gateway

## 🔗 Project Overview

1. Sentinel-X is an IAM-based security middleware performing real-time identity & API verification at the gateway.
2. Uses honeypot-triggered detection and behavioral analysis to identify unauthorized access.
3. Applies forward-fix mitigation by instantly blocking malicious IPs, reducing dwell time.
4. Integrates with SOC alerting to deliver live threat intelligence and maintains forensic logs.


## 🔗 Strategic Motivation

- Inspired by 2026 data breaches (e.g., Stryker and AstraZeneca), 
this project shifts from reactive logging to Proactive Defense.
It ensures infrastructure integrity by automating threat responses
removing the risk of manual administrative delay.

## 🔗 Core Functionalities

- #### 🚀 Identity-Based Filtering (IAM):

- #### 🪤 Active Honeypot Architecture: 

- #### ⚡ Autonomous Mitigation:

- #### 📱 Instant SOC Alerting: 

- #### 📂 Forensic Persistence: 

## 🔗 Technical Stack:

  - Backend: FastAPI (Asynchronous Middleware for low-latency interception)
      
  - ORM/Database: SQLAlchemy + SQLite (Forensic Vault & IAM Logic)
      
  - Intelligence: IP-API (Real-time Geospatial Telemetry)
      
  - Alerting: Telegram API (Real-time SOC Response)


## 🔗 Deployment & Orchestration:

          Initialize Environment: pip install fastapi uvicorn sqlalchemy requests
    
          Identity Provisioning: Define authorized credentials and Telegram API_TOKEN in the configuration.
          
          Gateway Launch: uvicorn main:app --reload
          
          Edge Simulation: Tunnel local port 8000 via Ngrok to test against global threat vectors.

## 🔗 Validation Results:

  -> The system successfully blocked unauthorized probing from external mobile networks
  
  <img src="https://github.com/user-attachments/assets/25e57681-d32d-45d3-8bc9-5eaba63164d2" width="100">

    
  -> updated the forensic database 
  
  <img src="https://github.com/user-attachments/assets/a26370d3-21e8-44bd-83e1-ba71ecaff1df" width="100">
  
  -> delivered a SOC alert in under 1 second.
  
  <img src="https://github.com/user-attachments/assets/0a9678d5-a16f-41c3-88df-bef5bd120811" width="100">

## 🔗 Future Enhancements
    🔐 Extend IAM with OAuth2/JWT for stronger identity verification
    🤖 Add AI-based anomaly detection for smarter threat prediction
    📊 Build a real-time SOC dashboard with cloud & SIEM integration

# License:

  Personal Learning Project | Research in Autonomous Security & IAM. 🚀🛡️
