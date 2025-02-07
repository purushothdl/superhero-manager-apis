from sqlalchemy import Column, Integer, String, ForeignKey, Table, Boolean
from sqlalchemy.orm import relationship
from app.database.connection import Base

# Association table for many-to-many relationship
hero_mission_association = Table(
    "hero_mission_association",
    Base.metadata,
    Column("hero_id", Integer, ForeignKey("heroes.id")),
    Column("mission_id", Integer, ForeignKey("missions.id")),
)

class Hero(Base):
    __tablename__ = "heroes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    alias = Column(String)
    power_level = Column(Integer)
    city = Column(String)
    affiliation = Column(String)

    # Relationship to missions
    missions = relationship("Mission", secondary=hero_mission_association, back_populates="heroes")

class Mission(Base):
    __tablename__ = "missions"

    id = Column(Integer, primary_key=True, index=True)
    location = Column(String)
    threat_level = Column(String)
    status = Column(String, default="pending")

    # Relationship to heroes
    heroes = relationship("Hero", secondary=hero_mission_association, back_populates="missions")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String, default="user")  # "admin" or "user"
    is_active = Column(Boolean, default=True) 