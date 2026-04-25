from sqlalchemy import Column,Integer,Boolean,ForeignKey
from app.core.database import Base 

class RouteReport(Base):
    __tablename__="routereports"

    id=Column(Integer,primary_key=True,index=True)

    route_id=Column(Integer,ForeignKey("routes.id"),nullable=False)

    report_id=Column(Integer,ForeignKey("reports.id"),nullable=False)

    visit_order=Column(Integer,nullable=False)