# API Routes and Query Parameters

## `create_bahan_resep`

This API creates a new `Bahan_Resep` object and adds it to the database. The input data should be in the form of a `Bahan_ResepCreate` object. The API returns a success message along with the newly created `Bahan_Resep` object.

**HTTP Method:** POST

**URL:** `/bahan_resep/`

**Query Parameters:**

None

**Request Body:**

```json
{
    "resep_id": int,
    "bahan_id": int,
    "jumlah": float
}
```

**Response:**

```json
{
    "message": str,
    "data": {
        "id": int,
        "resep_id": int,
        "bahan_id": int,
        "jumlah": float
    }
}
```

## `get_bahan_resep` API

This API retrieves a `Bahan_Resep` object from the database by its `resep_id` and `bahan_id`. The API returns a success message along with the retrieved `Bahan_Resep` object.

**HTTP Method:** GET

**URL:** `/bahan_resep/{resep_id}/{bahan_id}`

**Query Parameters:**

None

**Request Body:**

None

**Response:**

```json
{
    "message": str,
    "data": {
        "id": int,
        "resep_id": int,
        "bahan_id": int,
        "jumlah": float
    }
}
```

## `get_bahan_by_resep_id` API

This API retrieves all `Bahan_Resep` objects from the database by their `resep_id`. The API returns a success message along with a list of retrieved `Bahan_Resep` objects.

**HTTP Method:** GET

**URL:** `/bahan_resep/resep/{resep_id}`

**Query Parameters:**

- `offset` (optional): The number of items to skip before starting to collect the result set. Default is 0.
- `page_size` (optional): The maximum number of items to return in the result set. Default is 100.

**Request Body:**

None

**Response:**

```json
{
    "message": str,
    "data": [
        {
            "id": int,
            "resep_id": int,
            "bahan_id": int,
            "jumlah": float
        },
        ...
    ]
}
```

## get_resep_by_bahan_ids

This API endpoint retrieves all Resep objects from the database that contain the given list of bahan_ids.

**Query Parameters**

- `db`: Session - Required. The database session.
- `bahan_ids`: List[int] - Required. A list of integers representing the ids of the bahans to search for in the Resep objects.
- `offset`: int - Optional. An integer representing the number of results to skip before returning data. Default is 0.
- `page_size`: int - Optional. An integer representing the maximum number of results to return. Default is 100.

**Response**

- `message`: str - A message indicating whether any Resep objects were found for the given bahan_ids.
- `data`: list[int] - A list of integers representing the ids of the Resep objects that contain all of the given bahan_ids.

## get_all_bahan_resep

This API endpoint retrieves all Bahan_Resep objects from the database.

**Query Parameters**

- `db`: Session - Required. The database session.
- `offset`: int - Optional. An integer representing the number of results to skip before returning data. Default is 0.
- `page_size`: int - Optional. An integer representing the maximum number of results to return. Default is 100.

**Response**

- `message`: str - A message indicating whether any Bahan_Resep objects were found.
- `data`: list[Bahan_Resep] - A list of Bahan_Resep objects retrieved from the database.

## update_bahan_resep

This API endpoint updates a Bahan_Resep object in the database by its resep_id and bahan_id.

**Query Parameters**

- `db`: Session - Required. The database session.
- `resep_id`: int - Required. An integer representing the id of the Resep object to which the Bahan_Resep object belongs.
- `bahan_id`: int - Required. An integer representing the id of the Bahan_Resep object to update.
- `bahan`: schemas.Bahan_ResepUpdate - Required. A schema representing the updated Bahan_Resep object.

**Response**

- `message`: str - A message indicating whether the Bahan_Resep object was successfully updated.
- `data`: Bahan_Resep - The updated Bahan_Resep object retrieved from the database.

## delete_bahan_resep

This API endpoint deletes a Bahan_Resep object from the database by its resep_id and bahan_id.

**Query Parameters**

- `db`: Session - Required. The database session.
- `resep_id`: int - Required. An integer representing the id of the Resep object to which the Bahan_Resep object belongs.
- `bahan_id`: int - Required. An integer representing the id of the Bahan_Resep object to delete.

**Response**

- `message`: str - A message indicating whether the Bahan_Resep object was successfully deleted.
- `data`: Bahan_Resep - The deleted Bahan_Resep object retrieved from the database.
