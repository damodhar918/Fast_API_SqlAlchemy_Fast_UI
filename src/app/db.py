from datetime import date
from sqlmodel import create_engine, SQLModel, Field
from pathlib import Path
from typing import Optional

DATABASE_DIR: Path = Path().cwd() / "src" / "data"
DATABASE_URL = f"sqlite:///{DATABASE_DIR}/test.db"
print(f"Database URL: {DATABASE_URL}")


class Items(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    description: str
    price: int
    is_offer: Optional[bool] = False
    offer_ends: Optional[date] = None


class User(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    dob: date


# create the engine
engine = create_engine(DATABASE_URL)

SQLModel.metadata.create_all(engine)
