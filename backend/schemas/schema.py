from pydantic import BaseModel
from core.config import settings
from typing import List

class OutputModel(BaseModel):
	recommendations: List[int]
	Number_of_recommendations: int
	products_used: List[int]