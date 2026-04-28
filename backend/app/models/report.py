from sqlalchemy import Column,Integer,String,Boolean, ForeignKey, Enum,Float,DateTime
from app.core.database import Base 
import enum
from sqlalchemy.sql import func
class ReportStatus(str, enum.Enum):
    pending    = "pending"
    in_progress = "in_progress"
    resolved   = "resolved"

class Report(Base):
    _tablename_="reports"
    
    id=Column(Integer,primary_key=True,index=True)

    citizen_id=Column(Integer, ForeignKey("users.id"),nullable=False)

    audio_path=Column(String(255),nullable=True)

    latitude=Column(Float, nullable=False)
    
    longitude =Column(Float, nullable=False)

    address_text =Column(String(255), nullable=True)

    status=Column(Enum(ReportStatus), nullable=False, default=ReportStatus.pending)

    created_at = Column(DateTime(timezone=True), server_default=func.now()