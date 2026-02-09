from sqlalchemy.orm import Session
from models import Lead
from schemas import LeadCreate

def create_lead(db: Session, lead: LeadCreate):
    db_lead = Lead(
        name=lead.name,
        email=lead.email,
        phone=lead.phone
    )
    db.add(db_lead)
    db.commit()
    db.refresh(db_lead)
    return db_lead

def get_leads(db: Session):
    return db.query(Lead).all()

def update_lead_status(db: Session, lead_id: int, status: str):
    lead = db.query(Lead).filter(Lead.id == lead_id).first()
    if not lead:
        return None
    lead.status = status
    db.commit()
    db.refresh(lead)
    return lead
