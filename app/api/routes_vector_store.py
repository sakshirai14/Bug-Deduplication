from fastapi import APIRouter, UploadFile, File, HTTPException, BackgroundTasks
from app.services.vector_store_service import VectorStoreService
from app.repositories.issues_repository import IssuesRepository
from app.models.schemas import VectorStoreStatus
from typing import Dict

router = APIRouter(prefix="/vector-store", tags=["Vector Store"])
vector_store_service = VectorStoreService()
issues_repository = IssuesRepository()

@router.post("/append", response_model=Dict)
async def append_issues(file: UploadFile = File(...)):
    try:
        print("enters try block")
        contents = await file.read()
        file.file.seek(0)
        
        # Parse issues
        issues = issues_repository.parse_file(file.file, file.filename)
        print("issues",issues)
        # Append to vector store
        added_count = vector_store_service.append_issues(issues)
        print(f"Added {added_count} issues to vector store")
        print("filename",file.filename)
        # Record upload
        vector_store_service.record_upload(file.filename, added_count)
        
        # Get updated status
        status = vector_store_service.get_status()
        
        return {
            "file_name": file.filename,
            "issues_added": added_count,
            "total_issues": status.total_issues,
            "upload_events": status.upload_events,
            "last_updated_utc": status.last_updated_utc
        }
        
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

@router.get("/status", response_model=VectorStoreStatus)
async def get_status():
    return vector_store_service.get_status()

@router.post("/reset", response_model=VectorStoreStatus)
async def reset_store():
    vector_store_service.reset_store()
    return vector_store_service.get_status()
