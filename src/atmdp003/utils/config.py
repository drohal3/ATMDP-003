import os
from dotenv import load_dotenv

load_dotenv()

def lazy_env(var_name: str, default=None, required=True):
    """
    Return a function that fetches an environment variable lazily.
    Raises ValueError only when accessed if required and missing.
    """
    def getter():
        value = os.getenv(var_name, default)
        if required and value is None:
            raise ValueError(f"Missing required environment variable: {var_name}")
        return value
    return getter


# PRECURSORS_RAW_CSV_PATH = lazy_env("PRECURSORS_RAW_CSV_PATH")
TRACEGASES_RAW_DIR_PATH = lazy_env("TRACEGASES_RAW_DIR_PATH")
PREPROCESSED_DIR_PATH = lazy_env("PREPROCESSED_DIR_PATH")
COMBINED_CSV_PATH = lazy_env("COMBINED_CSV_PATH")

