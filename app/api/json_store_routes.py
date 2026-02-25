from fastapi import APIRouter, HTTPException
from typing import Dict, Any

from app.repositories.json_issues_repository import JsonIssuesRepository
from app.services.vector_store_service import VectorStoreService

print("✅ JSON routes loaded ")

router = APIRouter(prefix="/json-store", tags=["JSON Store"])

json_repo = JsonIssuesRepository()
vector_service = VectorStoreService()


@router.post("/append", response_model=Dict[str, Any])
async def append_json_issues(payload: Dict[str, Any]):

    try:
        print("Appending JSON issues...")

        # Convert raw JSON → Issue objects
        issues = json_repo.parse_json(payload)
        print(f"Parsed {len(issues)} issues from JSON payload")

        if not issues:
            print("No issues found in JSON payload")
            raise ValueError("No issues found in JSON payload")

        # Store into FAISS
        added_count = vector_service.append_issues(issues)

        # Record upload event
        vector_service.record_upload("json_api", added_count)

        status = vector_service.get_status()

        return {
            "issues_added": added_count,
            "total_issues": status.total_issues,
            "upload_events": status.upload_events,
            "last_updated_utc": status.last_updated_utc
        }

    except Exception as e:
        print("Error occurred while appending JSON issues:", e)
        raise HTTPException(status_code=400, detail=str(e))
