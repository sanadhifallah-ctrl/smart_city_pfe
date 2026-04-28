from pydantic import BaseModel,ConfigDict
from datetime import datetime
from typing import Optional

class CreateReport(BaseModel):
    latitude:float
    longitude:float
    audio_path:str
    address_text:Optional[str]=None
    
class UpdateReport(BaseModel):
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    audio_path: Optional[str] = None

class ReportResponse(BaseModel):
    id: int
    citizen_id:int
    route_id:int
    latitude: float
    longitude: float
    audio_path: str
    address_text: str
    status:ReportResponse
    created_at:datetime 
    
    model_config=ConfigDict (from_attributes=True)
    