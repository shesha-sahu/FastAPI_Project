import requests
import pytest
import json



ENDPOINT = "http://127.0.0.1:8000"

@pytest.mark.int
def test_can_call_endpoint():
    
    response = requests.get(ENDPOINT)
    assert response.status_code == 200

@pytest.mark.int
def test_can_addperson():
    payload ={ "id": 0,
  "name": "Arjun",
  "age": 20,
  "gender": "F",
  "city": "Unkown" 
  }
    
    addperson_response = requests.post(ENDPOINT+ "/addperson", json = payload )
    assert addperson_response.status_code == 200
    data = addperson_response.json()
    print(data)

@pytest.mark.int
def test_getperson():
  pass
  payload = {"Id": 34}

  p_id = payload['Id']
  get_response = requests.get(ENDPOINT + f'/person/{p_id}')
  assert get_response.status_code == 200
  get_response_data = get_response.json()
  print(get_response_data)

  assert get_response_data['Id'] == payload['Id']
#   assert get_response_data['Name'] == payload['Name']

@pytest.mark.int
def test_can_changePerson():
    payload = {
        "id":34,
  "name": "Raghav",
  "age": 40,
  "gender": "M",
  "city": "Villa"
  }
    
    changePerson_response = requests.put(ENDPOINT+ "/changePerson", json = payload )
    assert changePerson_response.status_code == 200
    data = changePerson_response.json()
    print(data)

@pytest.mark.int
def test_can_deleteperson():

    payload = { "id": 34}
   
    delete_id = payload['id']
    print(delete_id)
    delete_response = requests.delete(ENDPOINT + f"/deleteperson/{delete_id}")
    print(delete_response)
    assert delete_response.status_code == 200
    delete_data = delete_response.json()
    print(delete_data)
    
