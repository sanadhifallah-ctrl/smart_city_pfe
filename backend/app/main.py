from fastapi import FastAPI
from app.core.database import Base,engine
from app.models.user import User
from app.models.route import Route
from app.models.report import Report 
from app.models.routereport import RouteReport
app=FastAPI()

#creer les tables 
Base.metadata.create_all(bind=engine)

@app.get("/")
def route():
    return {"messg":"backend"}

@app.get("/test_db")
def route1():
    return {"messg":"db"}

@app.get("/test_db1")
def route1():
    return {"messg":"db1"}