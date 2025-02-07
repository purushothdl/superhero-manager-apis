from pydantic import BaseModel
from typing import List

class HeroCreate(BaseModel):
    name: str
    alias: str
    power_level: int
    city: str
    affiliation: str

class MissionCreate(BaseModel):
    location: str
    threat_level: str
    status: str = "pending"

class MissionAssign(BaseModel):
    hero_ids: List[int] 
    mission_id: int 