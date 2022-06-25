from src.base_entities.base_api_entity import BaseEntityAPI
from src.entities.pet_entity.pet_attributes import petAttributes
from src.schemas.pet_schema import petPostRequestSchema, petidSchema

class petEntityAPIRequests(BaseEntityAPI):

    def __init__(self,main_entity):
        super(petEntityAPIRequests, self).__init__()
        self.entity = main_entity


    def create_new_pet(self, expected_code=200):
        request_data = petPostRequestSchema().dumps(self.entity)
        response = self.run_api_request('POST', '/v2/pet', data=request_data,expected_code=expected_code, verify_keys_order=True)
        if expected_code == 200:
            self.entity.update(petidSchema().load(response.json()))

    def update_pet_data(self, expected_code=200):
        request_data = petPostRequestSchema().dumps(self.entity)
        response = self.run_api_request('PUT', '/v2/pet', data=request_data,expected_code=expected_code)
        if expected_code == 200:
            self.entity.update(petidSchema().load(response.json()))

    def get_pet_data_by_id(self, expected_code=200):
        response = self.run_api_request('GET', '/v2/pet/%s' %self.entity.get_attribute(petAttributes.ID),expected_code=expected_code)
        if expected_code == 200:
            self.entity.update(petidSchema().load(response.json()))


    def delete_pet_by_id(self, expected_code=200):
        response =self.run_api_request('DELETE', '/v2/pet/%s' %self.entity.get_attribute(petAttributes.ID),expected_code=expected_code)
        return response