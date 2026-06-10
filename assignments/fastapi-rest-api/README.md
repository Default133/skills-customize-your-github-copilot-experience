# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API using FastAPI so students can practice modern Python web development, request validation, and automatic API documentation.

- Focus on defining REST endpoints with FastAPI.
- Practice Pydantic request/response models and validation.
- Learn how query parameters and JSON request bodies work.

## 📝 Tasks

### 🛠️ Create REST API Endpoints

#### Description
Implement a FastAPI application that provides endpoints for listing, retrieving, and creating items.

#### Requirements
Completed program should:

- Define a `FastAPI` app instance.
- Create a `GET /items/` endpoint that returns a list of items.
- Create a `GET /items/{item_id}` endpoint that returns a single item by its ID.
- Create a `POST /items/` endpoint that accepts a JSON body and adds a new item.

### 🛠️ Define Request and Response Models

#### Description
Use Pydantic models to validate incoming data and shape API responses.

#### Requirements
Completed program should:

- Define an `ItemCreate` model for POST request data.
- Define an `Item` model for API responses with an `id` field.
- Use the models in route type annotations and return validated responses.
- Validate required fields such as `name` and `price`.

### 🛠️ Add Query Parameters and API Docs

#### Description
Support optional query parameters and verify that FastAPI’s automatic documentation is available.

#### Requirements
Completed program should:

- Add an optional `q` query parameter to `GET /items/`.
- Filter or otherwise use the query parameter in the endpoint logic.
- Confirm the API docs appear at `/docs` and the OpenAPI schema at `/openapi.json`.
