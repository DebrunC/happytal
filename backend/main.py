from fastapi import FastAPI
from core.config import settings
from fastapi import HTTPException,status
from model.functions import getRecommendationByClient
from schemas.schema import OutputModel


from pydantic import  EmailStr

app= FastAPI(title= settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)

@app.get("/")
def hello_api():
	return "Welcome to the recommender system app"


@app.get("/model/recommendation/{idUser}",response_model=OutputModel)
def RecommendationClient(idUser:int,numReco:int=settings.NUMBER_RECOMMENDATIONS):
	reco = getRecommendationByClient(idUser,numReco)
	return reco