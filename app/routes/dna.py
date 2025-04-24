from fastapi import APIRouter
from app.schemas.dna_traits import DNATraits

router = APIRouter()

@router.post("/upload-dna-traits/")
async def upload_traits(traits: DNATraits):
    # Save to DB or temp storage
    return {"message": "DNA traits received", "traits": traits}
