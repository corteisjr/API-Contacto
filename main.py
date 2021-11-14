# Optional
from typing import Optional
# pydantic
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class Contact(BaseModel):
    contact_id: int
    first_name: str
    last_name: str
    user_name: str
    password: str
    
    class Config:
        schema_extra = {
        "example": {
            "contact_id": 1,
            "first_name": "Jhon",
            "last_name": "Doe",
            "user_name": "Jhon_123"
        }
    }

class ContactOut(BaseModel):
    contact_id: int
    first_name: str
    last_name: str
    user_name: str
    password: str
    


@app.get("/")
def home():
    return {"Hello": "FastAPI"}


@app.post('/contact', response_model_exclude={"password"}, description="Create a single contact")
async def create_contact(contact: Contact):
    return contact


@app.get("/contact/{contact_id}")
def contact_details(contact_id: int, page: Optional[int]=1):
    if page:
        return {'contact_id': contact_id, 'page': page}
    return {"contact_id": contact_id}