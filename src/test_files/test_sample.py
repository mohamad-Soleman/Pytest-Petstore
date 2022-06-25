# content of test_sample.py
from src.entities.pet_entity.pet import Pet
from src.entities.pet_entity.pet_attributes import petAttributes

def pre_test_requirments():
    new_pet = Pet()
    new_pet.api.create_new_pet()
    new_pet.api.get_pet_data_by_id()
    return new_pet


def test_customer_creation_assertion():
    my_pet= pre_test_requirments()
    assert my_pet.id != None


def test_customer_update_assertion():
    my_pet = pre_test_requirments()
    my_pet.set_attribute(petAttributes.NAME,'new_name')
    my_pet.api.update_pet_data()
    my_pet.api.get_pet_data_by_id()
    assert my_pet.name == 'new_name'

def test_customer_delete_assertion():
    my_pet = pre_test_requirments()
    response = my_pet.api.delete_pet_by_id()
    my_pet.api.get_pet_data_by_id(expected_code=404)
    assert response.json()['message'] == str(my_pet.id)