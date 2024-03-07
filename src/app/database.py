from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker
from databases import Database
from pathlib import Path

DATABASE_DIR: Path = Path().cwd() / "src" / "data"
DATABASE_URL = f"sqlite:///{DATABASE_DIR}/test.db"
print(f"Database URL: {DATABASE_URL}")

# Check if the directory exists, and create it if it doesn't
if not DATABASE_DIR.exists():
    DATABASE_DIR.mkdir(parents=True)
database = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()
# Create tables if they don't exist
# Base.metadata.create_all(bind=engine)
