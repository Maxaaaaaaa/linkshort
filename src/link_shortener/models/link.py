from pydantic import BaseModel

class LinkCreate(BaseModel):
    long_url: str

class Link(BaseModel):
    id: int
    long_url: str
    short_url: str
