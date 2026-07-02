import json
from pathlib import Path

from app.api.schemas import Assessment
from config import CATALOG_PATH


class CatalogLoader:
    def __init__(self):
        self.catalog_path = Path(CATALOG_PATH)
        self.catalog = None

    def load_catalog(self):
        """
        Load the SHL product catalog from JSON.
        Uses in-memory caching so the file is read only once.
        """

        if self.catalog is not None:
            return self.catalog

        with open(self.catalog_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        assessments = []

        for item in data:
            assessment = Assessment(
                entity_id=item.get("entity_id", ""),
                name=item.get("name", ""),
                link=item.get("link", ""),
                description=item.get("description", ""),
                job_levels=item.get("job_levels", []),
                languages=item.get("languages", []),
                duration=item.get("duration", ""),
                remote=item.get("remote", ""),
                adaptive=item.get("adaptive", ""),
                keys=item.get("keys", [])
            )

            assessments.append(assessment)

        self.catalog = assessments
        return self.catalog

    def get_by_name(self, name: str):
        """
        Find an assessment by its exact name.
        """

        catalog = self.load_catalog()

        for assessment in catalog:
            if assessment.name.lower() == name.lower():
                return assessment

        return None