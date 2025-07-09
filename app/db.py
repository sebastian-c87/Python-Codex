import os
from datetime import datetime
from typing import Dict

from pymongo import MongoClient


_MONGO_URI = os.getenv("MONGODB_URI")
_DB_NAME = os.getenv("MONGODB_DB", "code_debugger")
_COLLECTION_NAME = os.getenv("MONGODB_COLLECTION", "history")

_client = MongoClient(_MONGO_URI) if _MONGO_URI else None
_collection = _client[_DB_NAME][_COLLECTION_NAME] if _client else None


def save_analysis(code: str, analysis: str, suggestions: str) -> None:
    """Store analysis result in MongoDB if configured."""
    if not _collection:
        return
    _collection.insert_one({
        "code": code,
        "analysis": analysis,
        "suggestions": suggestions,
        "timestamp": datetime.utcnow(),
    })
