import os
from dotenv import load_dotenv
from fastapi import FastAPI
from app.sdk.job_manager import BaseJobManager
from app.sdk.job_router import JobManagerFastAPIRouter
from csv_scraper import scrape_csv
import logging

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)

HOST = os.getenv("HOST", "localhost")
PORT = int(os.getenv("PORT", "8000"))
MODE = os.getenv("MODE", "production")

app = FastAPI()
app.job_manager = BaseJobManager()  # type: ignore

job_manager_router = JobManagerFastAPIRouter(app, scrape_csv)

if __name__ == "__main__":
    import uvicorn
    print(f"Starting server on {HOST}:{PORT}")
    uvicorn.run("server:app", host=HOST, port=PORT, reload=True)
