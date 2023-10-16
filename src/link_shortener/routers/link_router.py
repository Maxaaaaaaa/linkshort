from fastapi import APIRouter, HTTPException, Depends
from databases import Database
from ..models.link import Link, LinkCreate
from ..dependencies import get_database

router = APIRouter()

@router.post("/shorten/", response_model=Link)
async def shorten_link(link_data: LinkCreate, db: Database = Depends(get_database)):

    pass
