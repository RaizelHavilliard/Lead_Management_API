from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import logging

from database import Base, engine, SessionLocal
from models import Lead
from schemas import LeadCreate, LeadUpdate, LeadOut
from crud import create_lead, get_leads, update_lead_status
from auth import verify_api_key

logging.basicConfig(level=logging.INFO)

app = FastAPI(title="Lead Management API")

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/leads", response_model=LeadOut, dependencies=[Depends(verify_api_key)])
def add_lead(lead: LeadCreate, db: Session = Depends(get_db)):
    existing = db.query(Lead).filter(Lead.email == lead.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Lead already exists")
    return create_lead(db, lead)

@app.get("/leads", response_model=list[LeadOut], dependencies=[Depends(verify_api_key)])
def list_leads(db: Session = Depends(get_db)):
    return get_leads(db)

@app.patch("/leads/{lead_id}", response_model=LeadOut, dependencies=[Depends(verify_api_key)])
def change_status(lead_id: int, payload: LeadUpdate, db: Session = Depends(get_db)):
    lead = update_lead_status(db, lead_id, payload.status)
    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")
    return lead

@app.post("/leads/{lead_id}/follow-up", dependencies=[Depends(verify_api_key)])
def trigger_follow_up(lead_id: int, db: Session = Depends(get_db)):
    lead = db.query(Lead).filter(Lead.id == lead_id).first()
    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")

    logging.info(f"Follow-up triggered for lead {lead.email}")
    return {"message": "Follow-up triggered"}
