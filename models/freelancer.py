from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Freelancer(Base):
    __tablename__ = 'freelancers'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True, index=True)
    skills = Column(String)
    rate = Column( Integer)

    proposals = relationship('Proposal', back_populates='freelancer')
