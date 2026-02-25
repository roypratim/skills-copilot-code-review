import os

# If requested, replace pymongo.MongoClient with mongomock for local runs
if os.environ.get("USE_MONGO_MOCK"):
    try:
        import mongomock
        import pymongo
        pymongo.MongoClient = mongomock.MongoClient
    except Exception:
        # If mongomock isn't available, let the import error surface when running
        pass

import uvicorn

from src.app import app


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
