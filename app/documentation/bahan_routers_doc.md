# API Routes and Query Parameters

## `create_bahan`

- Route: `/bahan`
- Method: `POST`
- Description: Creates a new Bahan object and adds it to the database.
- Query Parameters:
  - None
- Request Body:
  - `nama_bahan`: string, required
  - `satuan`: string, required
- Response:
  - Success:
    - Status Code: 201
    - Body:
      - `message`: string, "New bahan created"
      - `data`: object, newly created Bahan object
  - Error:
    - Status Code: 400
    - Body:
      - `message`: string, "Invalid input data"

## `get_bahan`

- Route: `/bahan/{bahan_id}`
- Method: `GET`
- Description: Retrieves a Bahan object from the database by its ID.
- Query Parameters:
  - None
- Request Body:
  - None
- Response:
  - Success:
    - Status Code: 200
    - Body:
      - `message`: string, "Bahan found"
      - `data`: object, Bahan object with matching ID
  - Error:
    - Status Code: 404
    - Body:
      - `message`: string, "Bahan with id {bahan_id} is not found"

## `get_bahan_by_name`

- Route: `/bahan/nama/{nama_bahan}`
- Method: `GET`
- Description: Retrieves a Bahan object from the database by its name.
- Query Parameters:
  - None
- Request Body:
  - None
- Response:
  - Success:
    - Status Code: 200
    - Body:
      - `message`: string, "Bahan found"
      - `data`: object, Bahan object with matching name
  - Error:
    - Status Code: 404
    - Body:
      - `message`: string, "Bahan with name {nama_bahan} is not found"

# API Routes and Query Parameters

## `get_all_bahan`

- Route: `/bahan`
- Method: `GET`
- Description: Retrieves a list of Bahan objects from the database with optional filters, sorting, and pagination.
- Query Parameters:
  - `offset`: integer, optional, default=0
    - The number of items to skip before starting to return results.
  - `page_size`: integer, optional, default=100
    - The maximum number of items to return in a single page.
  - `nama_bahan`: string, optional
    - Filters the results to only include Bahan objects whose name contains this value (case-insensitive).
  - `sort_by`: string, optional, default='id'
    - Sorts the results by the specified column. Possible values are 'id', 'nama_bahan', or 'satuan'.
  - `sort_order`: string, optional, default='asc'
    - Specifies the sort order. Possible values are 'asc' (ascending) or 'desc' (descending).
- Request Body:
  - None
- Response:
  - Success:
    - Status Code: 200
    - Body:
      - `message`: string, "All bahan retrieved"
      - `total_data`: integer, total number of Bahan objects that match the filter criteria
      - `data`: array of objects, list of Bahan objects that match the filter criteria
  - Error:
    - Status Code: 404
    - Body:
      - `message`: string, "No bahan found"

# API Routes and Query Parameters

## `update_bahan`

- Route: `/bahan/{bahan_id}`
- Method: `PUT`
- Description: Updates an existing Bahan object in the database with the specified ID.
- Query Parameters:
  - None
- Request Body:
  - `nama_bahan`: string, optional
    - The new name for the Bahan object.
  - `satuan`: string, optional
    - The new unit of measurement for the Bahan object.
- Response:
  - Success:
    - Status Code: 200
    - Body:
      - `message`: string, "Bahan with id {bahan_id} is updated"
      - `data`: object, the updated Bahan object
  - Error:
    - Status Code: 404
    - Body:
      - `message`: string, "Bahan with ID {bahan_id} is not found"
    - Status Code: 400
    - Body:
      - `message`: string, "At least one field is required to update bahan"

## `delete_bahan`

- Route: `/bahan/{bahan_id}`
- Method: `DELETE`
- Description: Deletes an existing Bahan object from the database with the specified ID.
- Query Parameters:
  - None
- Request Body:
  - None
- Response:
  - Success:
    - Status Code: 204
    - Body: None
  - Error:
    - Status Code: 404
    - Body:
      - `message`: string, "Bahan with ID {bahan_id} is not found"
