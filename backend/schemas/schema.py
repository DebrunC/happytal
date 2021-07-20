from pydantic import BaseModel, EmailStr

class ModelOutput(BaseModel):
	email: EmailStr
	numReco: int
