from pydantic import BaseModel
from typing import List, Optional

class HeroResponse(BaseModel):
    id: int
    name: str
    alias: str
    power_level: int
    city: str
    affiliation: str

    class Config:
        from_attributes = True

class MissionResponse(BaseModel):
    id: int
    location: str
    threat_level: str
    status: str
    heroes: List[HeroResponse]

    class Config:
        from_attributes = True