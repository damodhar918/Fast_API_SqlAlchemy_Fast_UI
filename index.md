### Project Structure

```
/myapp
    /app
        __init__.py
        main.py
        models.py
        schemas.py
        database.py
    /tests
        __init__.py
        test_app.py
    README.md
    requirements.txt
```

### File Descriptions

- **`main.py`**: This is the entry point of your application. It will contain your FastAPI app instance and the route definitions.
- **`models.py`**: This file will define your SQLAlchemy models.
- **`schemas.py`**: This file will define Pydantic models for request and response handling.
- **`database.py`**: This file will handle the database configuration and session creation.

### Example Code for Each File

#### `database.py`

```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database

DATABASE_URL = "sqlite:///./test.db"
database = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
```

#### `models.py`

```python
from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Integer)
    is_offer = Column(Boolean, default=False)
```

#### `schemas.py`

```python
from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    description: str
    price: float
    is_offer: bool

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True
```

#### `main.py`

```python
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/items/", response_model=schemas.Item)
async def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# Add other endpoints here
```

### Running the Application

To run your application, navigate to the `myapp` directory and execute:

```bash
uvicorn app.main:app --reload
```
