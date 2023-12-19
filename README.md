# PersonRegistryAPI
Objective :
The objective of this FastAPI project is to create a robust API for managing a database of individual records. The primary goals are:

CRUD Operations: Implement endpoints for Create, Read, Update, and Delete operations on individual records representing people stored in a JSON file.

Search Functionality: Enable filtering by age and name, allowing users to search for specific individuals or groups within the stored data.

Data Persistence: Utilize a JSON file (people.json) to persistently store and retrieve individual records, ensuring data consistency across API sessions.

Clone the repository:
  git clone https://github.com/your-username/project-name.git

Create a virtual environment and then activate :
  python3 -m venv venv
  venv\Scripts\activate

Install the project dependencies :
  pip install -r requirements.txt

Start the development server:
  uvicorn main:app --reload
  The server will start running on http://localhost:8000/

API endpoints:
GET /: Check if the API is running.
GET /person/{p_id}: Retrieve a person's details by ID.
GET /search: Search for people using filters.
POST /addperson: Add a new person to the list.
PUT /changePerson: Update details of an existing person.
DELETE /deleteperson/{p_id}: Delete a person from the list by ID.



