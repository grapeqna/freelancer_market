from pydantic import BaseModel

class CreateFreelancer(BaseModel):
    name: str
    skills: str
    rate: int

class CreateJob (BaseModel):
    title: str
    description: str
    budget: int

class CreateProposal (BaseModel):
    proposalText: str
    email: str
    job_id: int
    freelancer_id: int
