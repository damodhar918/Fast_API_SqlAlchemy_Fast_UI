from datetime import date
from sqlmodel import create_engine, SQLModel, Field
from pathlib import Path

DATABASE_DIR: Path = Path().cwd() / "src" / "data"
DATABASE_URL = f"sqlite:///{DATABASE_DIR}/db.sqlite3"
print(f"Database URL: {DATABASE_URL}")


class User(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    dob: date


# create the engine
engine = create_engine(DATABASE_URL, echo=True)

SQLModel.metadata.create_all(engine)
