from pydantic import BaseModel, Field
from typing import Dict


class PredictionResponse(BaseModel):
    predicted_category: str = Field(..., description='Predicted class of the Person', example="High")
    confidence: float = Field(..., description='Confidence for the predicted class', example=0.8347)
    class_probabilities: Dict[str, float] = Field(..., description='Probabilities for the classes', example={'low': 0.1, 'medium': 0.45, 'high': 0.98})