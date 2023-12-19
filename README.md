# PersonRegistryAPI
This project is a CRUD (Create, Read, Update, Delete) application developed using the FastAPI framework. It provides a set of API endpoints to perform operations on the specified resources.

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



