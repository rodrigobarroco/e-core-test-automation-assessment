import os

class Config:
    BASE_URL = os.getenv("BASE_URL", "https://automation-sandbox-python-mpywqjbdza-uc.a.run.app")
    TIMEOUT = int(os.getenv("TIMEOUT", 30))  # Default to 30 seconds, but can be overridden
    BROWSER = os.getenv("BROWSER", "chromium")  # Allow browser to be set via env var

