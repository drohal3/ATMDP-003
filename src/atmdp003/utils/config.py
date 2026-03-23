import os
from dotenv import load_dotenv

load_dotenv()

ENV_PRECURSORS_RAW_CSV_PATH = "PRECURSORS_RAW_CSV_PATH"
ENV_TRACEGASES_RAW_DIR_PATH = "TRACEGASES_RAW_DIR_PATH"
ENV_PREPROCESSED_DIR_PATH = ""


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

