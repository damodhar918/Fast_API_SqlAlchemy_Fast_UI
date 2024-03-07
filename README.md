# FastAPI_SqlAlchemy_Fast_UI
[![Python application](https://github.com/damodhar918/Fast_API_SqlAlchemy_Fast_UI/actions/workflows/python-app.yml/badge.svg)](https://github.com/damodhar918/Fast_API_SqlAlchemy_Fast_UI/actions/workflows/python-app.yml) [![codecov](https://codecov.io/github/damodhar918/FastAPI_SqlAlchemy_Fast_UI/graph/badge.svg?token=MHZTS92Y4I)](https://codecov.io/github/damodhar918/FastAPI_SqlAlchemy_Fast_UI) [![Unit Tests](https://github.com/damodhar918/Fast_API_SqlAlchemy_Fast_UI/actions/workflows/unittest.yml/badge.svg)](https://github.com/damodhar918/Fast_API_SqlAlchemy_Fast_UI/actions/workflows/unittest.yml)

FastAPI framework for managing items, leveraging SQLAlchemy for database operations.

## Description

FastAPI_SqlAlchemy_Fast_UI is a modern, fast web framework for building APIs with Python 3.8+. It is designed for managing items, offering high performance, easy learning curve, and readiness for production. The project utilizes SQLAlchemy for database operations, providing a robust backend for item management.

## Key Features

- **High Performance**: FastAPI is one of the fastest Python frameworks available, on par with NodeJS and Go.
- **Easy to Code**: Increases the speed of developing features by about 200% to 300%.
- **Fewer Bugs**: Reduces about 40% of human-induced errors.
- **Intuitive**: Offers great editor support with completion everywhere, reducing debugging time.
- **Robust**: Provides production-ready code with automatic interactive documentation.

## Installation

To install the required dependencies, run:

```bash
pip install .
or
pip install .[dev]
```

## Usage

To create a new item:
`**fake_load:**` A script for loading data into your application, useful for development and testing.
`fast_app: `A script for starting your FastAPI application with Uvicorn, simplifying the command needed to run your app.

## Running the Application

To run the FastAPI application, use the following command:

```bash
uvicorn src.app.main:app --reload
```

This command starts the FastAPI application defined in the `main1.py` file. The `--reload` flag enables hot reloading, which means the server will automatically update whenever you make changes to your code.

## Interacting with the API

### Updating an Item

To update an item with ID 1, use the following `curl` command:

```bash
curl -X PUT "http://127.0.0.1:8000/items/1" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"id\":5,\"name\":\"Updated Item\",\"description\":\"This is an updated item\",\"price\":29.99,\"is_offer\":false}"
```

This command sends a PUT request to the `/items/1` endpoint to update the item with ID 1. The request body contains the updated item data in JSON format.

### Adding a New Item

To add a new item, use the following `curl` command:

```bash
curl -X POST "http://127.0.0.1:8000/items/" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"id\":5,\"name\":\"Updated Item\",\"description\":\"This is an updated item\",\"price\":29.99,\"is_offer\":false}"
```

This command sends a POST request to the `/items/` endpoint to add a new item. The request body contains the new item data in JSON format.

### Deleting an Item

To delete an item with ID 5, use the following `curl` command:

```bash
curl -X DELETE "http://127.0.0.1:8000/items/5"
```

This command sends a DELETE request to the `/items/5` endpoint to delete the item with ID 5.

### Retrieving an Item

To retrieve an item with ID 1, use the following `curl` command:

```bash
curl -X GET "http://127.0.0.1:8000/items/1" -H "accept: application/json"
```

This command sends a GET request to the `/items/1` endpoint to retrieve the item with ID 1.

### Retrieving All Items

To retrieve all items, use the following `curl` command:

```bash
curl -X GET "http://127.0.0.1:8000/items" -H "accept: application/json"
```

This command sends a GET request to the `/items` endpoint to retrieve all items.

## Testing

To run the tests, navigate to the project directory and use the following commands:

```
pytest -vv
pytest --cov=src --cov-report=xml tests/
pytest --cov=src --cov-report=html tests/
```

The `--cov` flag is used for measuring test coverage, while the `--cov-report` flag is used to specify the format of the coverage report. Running these commands will generate an XML and HTML coverage report in the `tests/` directory.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue to discuss potential improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Damodhar Jangam - damodhar918@outlook.com
[damodhar918](github.com/damodhar918)
