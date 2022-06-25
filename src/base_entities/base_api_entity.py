import json
import requests
import os
import yaml
from hamcrest import assert_that , equal_to
from src.entities.pet_entity.pet_attributes_payload_keys_order import petAttributesPayloadKeysOrder


class BaseEntityAPI(object):

    #base entity api operations class , fetch the config.yml data in order to support multi env runs conf. , and extend the requests request behaviour
    def __init__(self):
        with open(os.getcwd() + '/local_config_file.yml', 'r') as ymlfile:
            self.config = yaml.safe_load(ymlfile)
            self.url = self.config['base']['url'] + ":" + self.config['base']['port']

    #validation on json keys order by converting the json to dict
    def verify_json_keys_order(self,data):
        json_to_dict = json.loads(data)
        keys_list= list(json_to_dict.keys())
        for key in keys_list:
            assert_that(petAttributesPayloadKeysOrder[key].value, equal_to(keys_list.index(key)))

    def run_api_request(self, method, endpoint, data=None, expected_code=None,verify_keys_order=False):

        updated_api_headers = {}
        if data:
            updated_api_headers = {'content-type': "application/json"}

        url = self.url + endpoint

        if verify_keys_order:
            self.verify_json_keys_order(data)


        try:
            response = requests.request(method=method, url=url,
                                        data=data, headers=updated_api_headers)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        #assertion on expected response code
        if expected_code:
            assert_that(response.status_code, equal_to(expected_code))

        # this class can be improved by handling more exception types , and also by adding logger
        return response