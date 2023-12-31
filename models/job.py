from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class Job(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, unique=True, index=True)
    budget = Column(Integer)

    proposals = relationship('Proposal', back_populates='job')