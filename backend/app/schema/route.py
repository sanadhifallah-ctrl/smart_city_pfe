from pydantic import BaseModel,ConfigDict
from app.models.route import RouteStatus
from datetime import datetime
from typing import Optional

class RouteCreate(BaseModel):
    agent_id:Optional [int]=None
    admin_id:int

class RouteUpdate(BaseModel):
    agent_id:Optional [int]=None
    status:Optional [RouteStatus] = None
    date_time:Optional [datetime] =None

class RouteResponse(BaseModel):
    id:int
    admin_id:int
    agent_id:int
    status:RouteStatus
    generated_at:datetime

    model_config=ConfigDict (from_attributes=True)

    