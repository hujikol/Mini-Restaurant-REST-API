# Resep API

This API allows you to create, read, update, and delete resep objects in a database. A resep object represents a recipe with a name and kategori id.

## Base URL

The base URL for this API is `http://localhost:8000`.

## Authentication

This API does not require authentication.

## Endpoints

# API Documentation

## Create New Resep

- **URL:** `/resep`
- **Method:** `POST`
- **Query Parameters:**
  - None
- **Request Body:**
  - `resep`: object (required)
    - `nama_resep`: string (required)
    - `kategori_id`: integer (required)
    - `bahan`: list of integers (required)
- **Response:**
  - Status Code: `201`
  - Response Body:
    - `id`: integer
    - `nama_resep`: string
    - `kategori_id`: integer
    - `bahan`: list of integers

## Get Single Resep

- **URL:** `/resep/{resep_id}`
- **Method:** `GET`
- **Query Parameters:**
  - None
- **Request Body:**
  - None
- **Response:**
  - Status Code: `200`
  - Response Body:
    - `id`: integer
    - `nama_resep`: string
    - `kategori_id`: integer
    - `bahan`: list of integers

## Get All Reseps

- **URL:** `/resep`
- **Method:** `GET`
- **Query Parameters:**
  - `offset`: integer (optional, default=0)
  - `page_size`: integer (optional, default=100)
  - `nama_resep`: string (optional)
  - `kategori_id`: integer (optional)
  - `sort_by`: string (optional, default="id")
  - `sort_order`: string (optional, default="asc")
- **Request Body:**
  - None
- **Response:**
  - Status Code: `200`
  - Response Body:
    - List of resep objects:
      - `id`: integer
      - `nama_resep`: string
      - `kategori_id`: integer
      - `bahan`: list of integers

## Update Existing Resep

- **URL:** `/resep/{resep_id}`
- **Method:** `PUT`
- **Query Parameters:**
  - None
- **Request Body:**
  - `resep`: object (required)
    - `nama_resep`: string (optional)
    - `kategori_id`: integer (optional)
    - `bahan`: list of integers (optional)
- **Response:**
  - Status Code: `200`
  - Response Body:
    - `id`: integer
    - `nama_resep`: string
    - `kategori_id`: integer
    - `bahan`: list of integers

## Delete Existing Resep

- **URL:** `/resep/{resep_id}`
- **Method:** `DELETE`
- **Query Parameters:**
  - None
- **Request Body:**
  - None
- **Response:**
  - Status Code: `204`
  - Response Body:
    - None
