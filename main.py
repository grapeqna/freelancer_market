from fastapi import FastAPI, Depends, HTTPException
#from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database import SessionLocal, Base, engine
from models.freelancer import Freelancer
from models.job import Job
from models.proposal import Proposal
#from schemas import Freelancer 
from schemas import CreateFreelancer as cr_f
from schemas import CreateJob as cr_j
from schemas import CreateProposal as cr_p

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine, tables=[
        Freelancer.__table__,
        Job.__table__,
        Proposal.__table__,
    
    ])

# Read 
@app.get("/freelancers/")
def read_freelancer(freelancer_id: int, db: Session = Depends(get_db), skip: int =0, limit: int =100):
    freelancer = db.query(Freelancer).filter(Freelancer.id == freelancer_id).first()
    return freelancer
    # return(db.query(Freelancer.Freelancer)
    #        .offset(skip)
    #        .limit(limit)
    #        .all())

@app.get("/jobs/")
def read_jobs(job_id: int, db: Session = Depends(get_db), skip: int =0, limit: int =100):
    job = db.query(Job).filter(Job.id == job_id).first()
    return job

@app.get("/proposals/")
def read_proposals(proposal_id: int, db: Session = Depends(get_db), skip: int =0, limit: int =100):
    proposal = db.query(Proposal).filter(Proposal.id == proposal_id).first()
    return proposal

# Create
@app.post("/freelancers_cr/")
def create_freelancer(freelancer: cr_f, db: Session = Depends(get_db)):
    db_freelancer = Freelancer(name=freelancer.name, skills=freelancer.skills, rate=freelancer.rate)
    db.add(db_freelancer)
    db.commit()
    db.refresh(db_freelancer)
    return db_freelancer

@app.post("/jobs_cr/")
def create_jobs(job: cr_j, db: Session = Depends(get_db)):
    db_jobs = Job(title= job.title, description= job.description, budget= job.budget)
    db.add(db_jobs)
    db.commit()
    db.refresh(db_jobs)
    return db_jobs

@app.post("/proposals_cr/")
def create_proposals(proposal: cr_p, db: Session = Depends(get_db)):
    db_proposals = Proposal(proposalText= proposal.proposalText, email= proposal.email, job_id= proposal.job_id, freelancer_id= proposal.freelancer_id)
    db.add(db_proposals)
    db.commit()
    db.refresh(db_proposals)
    return db_proposals

def get_f(db: Session, freelancer_id: int):
    return (db.query(Freelancer)
            .get({'id': freelancer_id}))

def get_j(db: Session, job_id: int):
    return (db.query(Job)
            .get({'id': job_id}))

def get_p(db: Session, proposal_id: int):
    return (db.query(Proposal)
            .get({'id': proposal_id}))

#Update
@app.put("/freelancers/{freelancer_id}")
def update_freelancer(freelancer_id: int, freelancer: cr_f, db: Session = Depends(get_db) ):
    db_freelancer = get_f(db,freelancer_id)
    db_freelancer.name = freelancer.name
    db_freelancer.skills = freelancer.skills
    db_freelancer.rate= freelancer.rate
    db.commit()
    db.refresh(db_freelancer)
    return db_freelancer

@app.put("/jobs/{jobs_id}")
def update_job(job_id: int, job: cr_j, db: Session = Depends(get_db) ):
    db_job = get_j(db,job_id)
    db_job.title = job.title
    db_job.description = job.description
    db_job.budget= job.budget
    db.commit()
    db.refresh(db_job)
    return db_job

@app.put("/proposals/{proposals_id}")
def update_proposal(proposal_id: int, proposal: cr_p, db: Session = Depends(get_db) ):
    db_proposal = get_p(db,proposal_id)
    db_proposal.proposalText = proposal.proposalText
    db_proposal.email = proposal.email
    db_proposal.job_id= proposal.job_id
    db_proposal.freelancer_id= proposal.freelancer_id
    db.commit()
    db.refresh(db_proposal)
    return db_proposal

# Delete
@app.delete("/freelancers/{freelancer_id}")
def delete_freelancer(freelancer_id: int, db: Session = Depends(get_db) ):
    db_freelancer= get_f(db, freelancer_id)
    db.delete(db_freelancer)
    db.commit()
    return None

@app.delete("/jobs/{jobs_id}")
def delete_job(job_id: int, db: Session = Depends(get_db) ):
    db_job= get_j(db, job_id)
    db.delete(db_job)
    db.commit()
    return None

@app.delete("/proposals/{proposals_id}")
def delete_proposal(proposal_id: int, db: Session = Depends(get_db) ):
    db_proposal= get_p(db, proposal_id)
    db.delete(db_proposal)
    db.commit()
    return None



@app.get("/freelancers2")
async def get_freelancers(db: Session = Depends(get_db), skip: int =0, limit: int =100):
    return(db.query(Freelancer)
           .offset(skip)
           .limit(limit)
           .all())

@app.get("/jobs2")
async def get_jobs(db: Session = Depends(get_db), skip: int =0, limit: int =100):
    return(db.query(Job)
           .offset(skip)
           .limit(limit)
           .all())

@app.get("/proposals2")
async def get_proposals(db: Session = Depends(get_db), skip: int =0, limit: int =100):
    return(db.query(Proposal)
           .offset(skip)
           .limit(limit)
           .all())
   # return {"important message": "Save the World!!!!!!!"}
