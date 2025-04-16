import re
from typing import List, Dict
from firm_core.db_client.faster_suite_db_client import FasterSuiteDBClient


class VendorDetector:
    def __init__(self, db_client: FasterSuiteDBClient):
        self.db = db_client

    def score_contact(self, contact: Dict) -> int:
        score = 0
        name = contact.get("name", "").lower()

        # 1. Company type
        if contact.get("type") == "Company":
            score += 1

        # 2. No linked matters
        if contact.get("matter_count", 0) == 0:
            score += 1

        # 3. Tagged as vendor
        if "vendor" in contact.get("tags", []):
            score += 2

        # 4. Name keyword hints
        if re.search(r"records|medical|court|reporting|vendor", name):
            score += 1

        return score

    def get_scored_contacts(self, min_score: int = 2) -> List[Dict]:
        contacts = self.db.get_all_contacts_with_metadata()
        scored = []

        for contact in contacts:
            contact["score"] = self.score_contact(contact)
            if contact["score"] >= min_score:
                scored.append(contact)

        return sorted(scored, key=lambda x: x["score"], reverse=True)
