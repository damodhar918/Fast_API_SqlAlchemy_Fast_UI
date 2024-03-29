
from fastapi.testclient import TestClient
from app.main_api import app  # Import your FastAPI app

# Create a TestClient instance
client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

# "name": fake.word(),
#         "description": fake.sentence(),
#         "price": fake.random_int(min=1, max=1000),
#         "is_offer": fake.boolean()


def test_create_item():
    item_data = {"name":"hundred","description":"Not chair bank there.","price":70,"is_offer":True,"offer_ends":"2001-10-29"}
    response = client.post("/items/", json=item_data)
    item_id = response.json()["id"]
    assert response.status_code == 200
    assert response.json() == {
        # Assuming the first item created has an id of 1
        "id": item_id,"name":"hundred","description":"Not chair bank there.","price":70,"is_offer":True,"offer_ends":"2001-10-29"}
    response = client.delete(f"/items/{item_id}")
    assert response.status_code == 200


def test_read_item():
    # First, create an item to read
    item_data = {"name":"hundred","description":"Not chair bank there.","price":70,"is_offer":True,"offer_ends":"2001-10-29"}
    response = client.post("/items/", json=item_data)
    assert response.status_code == 200
    item_id = response.json()["id"]

    # Now, read the item
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json() == {
        "id": item_id,"name":"hundred","description":"Not chair bank there.","price":70,"is_offer":True,"offer_ends":"2001-10-29"}
    
    response = client.delete(f"/items/{item_id}")
    assert response.status_code == 200


def test_update_item():
    # First, create an item to update
    item_data = {"name":"hundred","description":"Not chair bank there.","price":70,"is_offer":True,"offer_ends":"2001-10-29"}
    response = client.post("/items/", json=item_data)
    assert response.status_code == 200
    item_id = response.json()["id"]

    # Now, update the item
    updated_data = {
        "id": item_id,"name":"hundred","description":"Not chair bank there.","price":70,"is_offer":True,"offer_ends":"2001-10-29"}
    response = client.put(f"/items/{item_id}", json=updated_data)
    assert response.status_code == 200
    assert response.json() == updated_data
    response = client.delete(f"/items/{item_id}")
    assert response.status_code == 200


def test_delete_item():
    # First, create an item to delete
    item_data = {"name":"hundred","description":"Not chair bank there.","price":70,"is_offer":True,"offer_ends":"2001-10-29"}
    response = client.post("/items/", json=item_data)
    assert response.status_code == 200
    item_id = response.json()["id"]

    # Now, delete the item
    response = client.delete(f"/items/{item_id}")
    assert response.status_code == 200
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 404
