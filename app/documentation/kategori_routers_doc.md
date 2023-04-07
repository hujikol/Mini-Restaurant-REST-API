# Kategori API

This API allows you to create, read, update, and delete kategori objects in a database. A kategori object represents a kategori with it's name.

## Base URL

The base URL for this API is `http://localhost:8000`.

## Authentication

This API does not require authentication.

## Endpoints

## API Documentation

### `create_kategori`

Creates a new category in the database.

#### Request

- **Method:** POST
- **Endpoint:** `/kategori`
- **Headers:**
  - `Content-Type`: application/json
- **Body:**
  ```json
  {
    "nama_kat": "string"
  }
  ```
  - `nama_kat` (required): The name of the category to be created.

#### Response

- **Status Codes:**
  - 201: Category successfully created.
  - 409: Category with the same name already exists.
- **Body:**
  ```json
  {
    "message": "string",
    "kategori": {
      "id": "integer",
      "nama_kat": "string"
    }
  }
  ```
  - `message`: A message indicating the status of the request.
  - `kategori`: The newly created category object.

### `get_kategori`

Retrieves a category from the database based on its ID.

#### Request

- **Method:** GET
- **Endpoint:** `/kategori/{kategori_id}`
- **Headers:**
  - `Content-Type`: application/json
- **Path Parameters:**
  - `kategori_id` (required): The ID of the category to retrieve.

#### Response

- **Status Codes:**
  - 200: Category successfully retrieved.
  - 404: Category not found.
- **Body:**
  ```json
  {
    "message": "string",
    "data": {
      "id": "integer",
      "nama_kat": "string"
    }
  }
  ```
  - `message`: A message indicating the status of the request.
  - `data`: The retrieved category object.

### `get_kategori_by_name`

Retrieves a category from the database based on its name.

#### Request

- **Method:** GET
- **Endpoint:** `/kategori`
- **Headers:**
  - `Content-Type`: application/json
- **Query Parameters:**
  - `nama_kat` (required): The name of the category to retrieve.

#### Response

- **Status Codes:**
  - 200: Category successfully retrieved.
  - 404: Category not found.
- **Body:**
  ```json
  {
    "message": "string",
    "data": {
      "id": "integer",
      "nama_kat": "string"
    }
  }
  ```
  - `message`: A message indicating the status of the request.
  - `data`: The retrieved category object.

### `get_all_kategori`

Retrieves all categories from the database with pagination.

#### Request

- **Method:** GET
- **Endpoint:** `/kategori/all`
- **Headers:**
  - `Content-Type`: application/json
- **Query Parameters:**
  - `offset` (optional): The number of items to skip before starting to collect the result set. Default is 0.
  - `page_size` (optional): The maximum number of items to return. Default is 100.

#### Response

- **Status Codes:**
  - 200: Categories successfully retrieved.
- **Body:**
  ```json
  {
    "message": "string",
    "total_data": "integer",
    "data": [
      {
        "id": "integer",
        "nama_kat": "string"
      }
    ]
  }
  ```
  - `message`: A message indicating the status of the request.
  - `total_data`: The total number of categories in the database.
  - `data`: An array of category objects.

### `update_kategori`

Updates a category in the database.

#### Request

- **Method:** PUT
- **Endpoint:** `/kategori/{kategori_id}`
- **Headers:**
  - `Content-Type`: application/json
- **Path Parameters:**
  - `kategori_id`: The ID of the category to update.
- **Body:**
  ```json
  {
    "nama_kat": "string"
  }
  ```
  - `nama_kat` (optional): The new name of the category.

#### Response

- **Status Codes:**
  - 200: Category successfully updated.
  - 400: No fields provided to update or invalid data provided.
  - 404: Category not found.
- **Body:**
  ```json
  {
    "message": "string",
    "data": {
      "id": "integer",
      "nama_kat": "string"
    }
  }
  ```
  - `message`: A message indicating the status of the request.
  - `data`: The updated category object.

### `delete_kategori`

Deletes a category from the database.

#### Request

- **Method:** DELETE
- **Endpoint:** `/kategori/{kategori_id}`
- **Headers:**
  - `Content-Type`: application/json
- **Path Parameters:**
  - `kategori_id`: The ID of the category to delete.

#### Response

- **Status Codes:**
  - 204: Category successfully deleted.
  - 404: Category not found.
- **Body:**
  ```json
  {
    "message": "string"
  }
  ```
  - `message`: A message indicating the status of the request.
