from paydantic import BaseModel,ConfigDict
from app.models.routereport import StopStatus
from typing import Optional

class CreateRouteReport(BaseModel):
    route_id:int
    report_id:int
    visit_order:int

class RouteReportUpdate(BaseModel):
    visit_order:Optional [int]=None  

class RouteReportResponse(BaseModel):
    route_id:int
    report_id:int
    visit_order:int
    status:Optional [StopStatus]=None

    model_config=ConfigDict (from_attributes=True)
