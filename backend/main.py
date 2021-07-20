from fastapi import FastAPI
from core.config import settings
from fastapi import HTTPException,status
from model.functions import getRecommendationByClient

from pydantic import  EmailStr

app= FastAPI(title= settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)

@app.get("/")
def hello_api():
	return "Welcome to the recommender system app"


@app.get("/model/recommendation/{idUser}",response_model=dict)#,response_model=dict
def RecommendationClient(idUser:int,numReco:int=settings.NUMBER_RECOMMENDATIONS):
	
	reco = getRecommendationByClient(idUser,numReco)
	if not reco:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="function not found")
	return reco


