from sqlalchemy import Column,Integer,String,Boolean,Enum, ForeignKey,DateTime
from app.core.database import Base 
import enum
from sqlalchemy.sql import func


class RouteStatus(str, enum.Enum):
    planned = "planned"
    in_progress = "in_progress"
    completed = "completed"
class Route(Base):

    __tablename__="routes"

    id=Column(Integer,primary_key=True,index=True)

    admin_id=Column(Integer,ForeignKey("users.id"),nullable=False)

    agent_id=Column(Integer,ForeignKey("users.id"),nullable=False)

    status=Column(Enum(RouteStatus), default=RouteStatus.planned, nullable=False)

    generated_at = Column(DateTime(timezone=True), server_default=func.now())
    
    
