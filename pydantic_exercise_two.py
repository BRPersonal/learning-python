from venv import logger

from pydantic import BaseModel
from typing import List


class Query(BaseModel):
    description: str
    sql: str

class QueryList(BaseModel):
    queries: List[Query]

# Example usage:
example_data = {
    "queries": [
        {
            "description": "Retrieve film details including film_id, title, release_year, rental_duration, rental_rate, length, replacement_cost, and rating",
            "sql": "SELECT f.film_id_erp1, f.title_erp1, f.release_year_erp1, f.rental_duration_erp1, f.rental_rate_erp1, f.length_erp1, f.replacement_cost_erp1, f.rating_erp1 FROM film_erp1 f"
        },
        {
            "description": "Count the total number of movies",
            "sql": "SELECT COUNT(*) AS total_movies FROM film_erp1"
        }
    ]
}

if __name__ == "__main__":
    try:
        query_list = QueryList(**example_data)

        # serialize the QueryList object to JSON
        json_data = query_list.model_dump_json()
        print(f"json_data: {json_data}")

    except Exception as e:
        logger.exception(f"Error in parsing: {str(e)}")


