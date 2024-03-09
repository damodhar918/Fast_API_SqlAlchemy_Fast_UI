from fastapi import FastAPI, HTTPException, Depends
from typing import List
from .models import Item, Base
from .schemas import ItemBase, ItemOut
from sqlalchemy.orm import Session
from sqlalchemy import inspect
from .database import engine, get_db

app = FastAPI()

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

# Debugging: Check if the table exists after creation
inspector = inspect(engine)
if inspector.has_table("items"):
    print("Tables:", inspector.get_table_names())
else:
    print("Table does not exist")


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/items/", response_model=ItemBase)
async def create_item(item: ItemBase, db: Session = Depends(get_db)):
    db_item = Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@app.get("/items/{item_id}", response_model=ItemBase)
async def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@app.get("/items/", response_model=List[ItemOut])
async def read_item(db: Session = Depends(get_db)):
    db_item = db.query(Item).all()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@app.put("/items/{item_id}", response_model=ItemBase)
async def update_item(item_id: int, item: ItemBase, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    for key, value in item.model_dump().items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item


@app.delete("/items/{item_id}", response_model=ItemBase)
async def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return db_item


# Assuming your FastAPI application instance is named `app` and is defined in a file named `main.py`

def main():
    import uvicorn
    uvicorn.run("app.main_api:app", reload=True, port=8000, host="127.0.0.2")


if __name__ == "__main__":
    main()
