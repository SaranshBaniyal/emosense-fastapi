from fastapi import FastAPI
from uvicorn import run
import os
import logging
from fastapi.middleware.cors import CORSMiddleware

logger = logging.getLogger()
app = FastAPI()

# Allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"detail": "Hello World"}

if __name__ == "__main__":
    logger.info("Starting the FastAPI application...")
    
    # Use uvicorn to run the FastAPI application
    run(app, host="0.0.0.0", port=8000, log_level="info")