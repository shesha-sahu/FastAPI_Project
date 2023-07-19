from fastapi import FastAPI, Query ,HTTPException
from pydantic import BaseModel
from typing import Optional
import json,uvicorn

app = FastAPI()

@app.get('/')
def root():
     return {"Data": "Check endpoint hit successfuly"}

class Person(BaseModel):
    
  id: Optional[int]= None
  name: str
  age: int
  gender: str
  city:str


with open('people.json','r') as f:
  people = json.load(f)

@app.get('/person/{p_id}')
def get_person(p_id: int):
        person = [p for p in people if p['Id']== p_id]
        return person[0] if len(person) > 0 else {}

@app.get('/search')
def search_person(Age: Optional[int] = Query(None, title="Age", description="The age filtter" ),
                  Name : Optional[str] = Query(None, title="Name", description="The name filtter" ) ):
     
     people1 = [p for p in people if p['Age']==Age]

     if Name is None:
          if Age is None:
               return people
          else:
               return people1
     else:
          people2 = [p for p in people if Name.lower() in p['Name'].lower() ]
          if Age is None:
               return people2
          else:
               combined = [p for p in people if p in people2]
               return combined
                     

@app.post('/addperson')
def add_person(person: Person):
     p_id = max([p['Id'] for p in people]) +1
     new_person = {
          
        "Id": p_id,
        "Name": person.name, 
        "Age": person.age,
        "Gender": person.gender,
        "City": person.city
     }
     people.append(new_person)

     with open('people.json', 'w') as f:
          json.dump(people, f)

     return new_person
    
@app.put('/changePerson',status_code=200)
def change_person(person:Person):
     new_person = {
        "Id": person.id,
        "Name": person.name, 
        "Age": person.age,
        "Gender": person.gender,
        "City": person.city
     }
     
     person_list = [p for p in people if p['Id'] == person.id]
     if len(person_list) > 0 :
          people.remove(person_list[0])
          people.append(new_person)
          with open('people.json', 'w') as f:
               json.dump(people, f)
          return new_person
     else:
          raise HTTPException(status_code=404, detail =f"person with Id {person.id} does not exist")       



@app.delete('/deleteperson/{p_id}')
def delete_person(p_id: int):
     person = [p for p in people if p["Id"] ==p_id]
     if len(person)>0 :
          people.remove(person[0] )
          with open('people.json', 'w') as f:
               json.dump(people, f)
          
     else:
          raise HTTPException(status_code=404, detail =f"person with Id {person.id} does not exist")       



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1",port=8000)



     
     

     



