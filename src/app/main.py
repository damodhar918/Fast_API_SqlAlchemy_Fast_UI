# from contextlib import asynccontextmanager
# from datetime import date
from fastapi import FastAPI, HTTPException, Depends
from typing import List, Annotated
from fastapi.responses import HTMLResponse
from fastui import FastUI, AnyComponent, prebuilt_html, components as c
from fastui.components.display import DisplayMode, DisplayLookup
from fastui.events import GoToEvent, BackEvent
from fastui.forms import FormResponse, fastui_form
# from pydantic import BaseModel, Field
from sqlmodel import Session, select
# from typing import Optional
# from .models import Item
from .db import Items, engine
from .schemas import ItemBase, ItemOut, DeleteUserForm, UserForm
from .database import get_db

app = FastAPI()


@app.post("/api_item/", response_model=ItemBase)
async def create_item(item: ItemBase, db: Session = Depends(get_db)):
    db_item = Items(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@app.get('/api/item/add/', response_model=FastUI, 
         response_model_exclude_none=True)
def add_user():
    return [
        c.Page(
            components=[
                c.Heading(text='Add User', level=2),
                c.Paragraph(text='Add a user to the system'),
                c.ModelForm[UserForm](
                    submit_url='/api/item/add/'
                ),
            ]
        )
    ]


@app.post('/api/item/add/')
async def add_user(form: Annotated[UserForm,
                                   fastui_form(UserForm)]) -> FormResponse:
    with Session(engine) as session:
        user = Items(**form.model_dump())
        session.add(user)
        session.commit()

    return FormResponse(event=GoToEvent(url='/'))


@app.get("/api/", response_model=FastUI, response_model_exclude_none=True)
def users_table() -> list[AnyComponent]:

    with Session(engine) as session:
        users = session.exec(select(Items)).all()

    return [
        c.Page(  # Page provides a basic container for components
            components=[
                c.Heading(text='Users', level=2),  # renders `<h2>Users</h2>`
                c.Table[Items](  # c.Table is a generic component
                    #    parameterized with the model used for rows
                    data=users,
                    # define two columns for the table
                    columns=[
                        # the first is the users, name rendered as
                        # a link to their profile
                        DisplayLookup(
                            field='name', on_click=GoToEvent(url='/item/{id}/')),
                        # DisplayLookup(field="description",),
                        DisplayLookup(field="price"),
                        DisplayLookup(field="is_offer"),

                        # the second is the date of birth, rendered as a date
                        DisplayLookup(field='offer_ends',
                                      mode=DisplayMode.date),
                    ],
                ),
                c.Div(components=[
                    c.Link(
                        components=[c.Button(text='Add User')],
                        on_click=GoToEvent(url='/item/add/'),
                    ),
                ])
            ]
        ),
    ]


@app.get("/api/item/{user_id}/", response_model=FastUI,
         response_model_exclude_none=True)
def user_profile(user_id: int) -> list[AnyComponent]:
    """
    User profile page, the frontend will fetch this when the user
    visits `/item/{id}/`.
    """
    with Session(engine) as session:
        user = session.get(Items, user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")

    return [
        c.Page(
            components=[
                c.Heading(text=user.name, level=2),
                c.Link(components=[c.Text(text='Back')], on_click=BackEvent()),
                c.Details(data=user),
                c.Div(components=[
                    c.Heading(text="Delete User?", level=4),
                    c.ModelForm[DeleteUserForm](
                        submit_url=f'/api/item/{user_id}/delete/',
                        class_name="text-left"
                    )
                ], class_name="card p-4 col-4")
            ]
        ),
    ]


@app.post('/api/item/{user_id}/delete/')
async def delete_user(
    user_id: int,
    form: Annotated[DeleteUserForm, fastui_form(DeleteUserForm)]
) -> FormResponse:
    # delete the users
    with Session(engine) as session:
        user = session.get(Items, user_id)
        if user is not None:
            session.delete(user)
            session.commit()

    return FormResponse(event=GoToEvent(url='/'))


@app.get("/api_item/{item_id}", response_model=ItemBase)
async def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(Items).filter(Items.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@app.get("/api_item/", response_model=List[ItemOut])
async def read_item(db: Session = Depends(get_db)):
    db_item = db.query(Items).all()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@app.put("/api_item/{item_id}", response_model=ItemBase)
async def update_item(item_id: int, item: ItemBase,
                      db: Session = Depends(get_db)):
    db_item = db.query(Items).filter(Items.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    for key, value in item.model_dump().items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item


@app.delete("/api_item/{item_id}", response_model=ItemBase)
async def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(Items).filter(Items.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return db_item


@app.get('/{path:path}')
async def html_landing() -> HTMLResponse:
    """Simple HTML page which serves the React app, 
    comes last as it matches all paths."""
    return HTMLResponse(prebuilt_html(title='FastUI Demo'))


def main():
    import uvicorn
    uvicorn.run("app.main_ui:app", reload=True, port=8000)


if __name__ == "__main__":
    main()
