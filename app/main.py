from fastapi import FastAPI
from utils.logger import get_logger

app = FastAPI()
logger = get_logger()

@app.get("/")
def home():
    logger.info("System started")
    return {"message": "AI Recruiting System Running 🚀"}