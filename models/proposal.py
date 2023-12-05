from sqlalchemy import Column, Integer, String, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from database import Base

class Proposal(Base):
    __tablename__ = 'proposals'

    id = Column(Integer, primary_key=True, index=True)
    proposalText = Column(String)
    email = Column(String, CheckConstraint("email LIKE '%@%'"))
    job_id = Column(Integer, ForeignKey('jobs.id'))  
    job = relationship('Job')
    freelancer_id = Column(Integer, ForeignKey('freelancers.id'))  
    #freelancer = relationship('Freelancer', back_populates='proposals')
    freelancer = relationship('Freelancer')

    