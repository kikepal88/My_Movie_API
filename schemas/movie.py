from pydantic import BaseModel, Field
from typing import Optional

class Movie(BaseModel):
  id: Optional[int] = None
  title: str = Field(max_length=15, min_length=3)
  overview: str = Field(max_length=50, min_length=15)
  year: int = Field(le=2024)
  rating: float = Field(ge=1, le=10)
  category: str = Field(max_length=15, min_length=5)

  class Config:
    json_schema_extra = {
      'example': {
        'id': 1,
        'title': 'Mi película',
        'overview': 'Descripción de la película',
        'year': 2024,
        'rating': 9.8,
        'category': 'Horror'
      }
    }