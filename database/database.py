from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base


# Load database url
load_dotenv()
database_url = os.getenv("DATABASE_URL")

# Create the engine
engine = create_engine(database_url)

# Create a session factory
Session = sessionmaker(bind=engine)


# Function to get a new session
def get_session():
    return Session()


# Create tables if they don't exist, will use Alembic in future versions
def create_tables():
    Base.metadata.create_all(engine)
