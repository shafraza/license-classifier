from pydantic import BaseModel

class License(BaseModel):
    id: int
    description: str
    category: str = ""
    explanation: str = ""
    validated: bool = False
