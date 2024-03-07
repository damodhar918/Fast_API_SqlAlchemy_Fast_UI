import requests
from faker import Faker

# Initialize the Faker generator
fake = Faker()

# Function to generate fake data for an Item


def generate_fake_item():
    return {
        "name": fake.word(),
        "description": fake.sentence(),
        "price": fake.random_int(min=1, max=1000),
        "is_offer": fake.boolean(),
        "offer_ends" : fake.date()
    }


def request_response(response):
    # Check the response
    if response.status_code == 200:
        print("Item created successfully:")
        print(response.json())
    else:
        print(
            f"Failed to create item. Status code: {response.status_code}")
        print(response.text)


# Define the URL of your FastAPI application
URL = "http://localhost:8000/items/"


def main():
    # Loop to generate and post 10 items
    for _ in range(10):
        # Generate fake data for an Item
        data = generate_fake_item()
        try:
            # Send a POST request to the FastAPI application
            request_response(requests.post(URL, json=data))

        except Exception as e:
            print(data)
            print("No connection", URL)
            print(e)


if __name__ == "__main__":
    main()
