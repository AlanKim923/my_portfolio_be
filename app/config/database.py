import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class DatabaseConfig:
    HOST = os.environ["DB_HOST"]
    PORT = os.environ["DB_PORT"]
    DB_NAME = os.environ["DB_NAME"]

    DB_USER = os.environ["DB_USER"]
    DB_PWD = os.environ["DB_PWD"]

    URL = f"postgresql+psycopg2://{DB_USER}:{DB_PWD}@{HOST}:{PORT}/{DB_NAME}"
