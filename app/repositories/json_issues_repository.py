from typing import Dict, List
from app.models.schemas import Issue, JsonIssue


class JsonIssuesRepository:

    REQUIRED_FIELDS = ["issue_id", "title", "repro_steps"]

    def parse_json(self, payload: Dict) -> List[Issue]:

        if "issues" not in payload:
            raise ValueError("Payload must contain 'issues'")

        rows = payload["issues"]

        issues = []

        for idx, row in enumerate(rows):

            missing = [
                f for f in self.REQUIRED_FIELDS
                if f not in row or not str(row[f]).strip()
            ]

            if missing:
                raise ValueError(f"Row {idx} missing {missing}")

            model = {
                "id": row["issue_id"],
                "title": row["title"],
                "repro_steps": row["repro_steps"],
                "module": row.get("module"),
                "work_item_type": "json",
                "source": "json_api"
            }

            issues.append(Issue(**model))

        return issues
