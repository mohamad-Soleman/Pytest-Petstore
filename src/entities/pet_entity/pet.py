from src.base_entities.base_entity import BaseEntity
from src.entities.pet_entity.pet_attributes import petAttributes
import random
from src.entities.pet_entity.pet_entity_api_requests import petEntityAPIRequests


class Pet(BaseEntity):

    def __repr__(self):
        return "PET"
    #initiate new pet will also create an instanse of the api requests class , witch represet all the operations that can be done on pet
    def __init__(self):
        self.main_entity = self
        self.api = petEntityAPIRequests(main_entity=self.main_entity)
        self.generate_pet_details()

    #generating all the reuqired pet data
    def generate_pet_details(self):
        self.set_attribute(petAttributes.ID, 0)
        self.set_attribute(petAttributes.CATEGORY_ID, '0')
        self.set_attribute(petAttributes.CATEGORY_NAME, 'string')
        self.set_attribute(petAttributes.NAME, random.choice(self.pet_names))
        self.set_attribute(petAttributes.TAGS_ID, 0)
        self.set_attribute(petAttributes.TAGS_NAME, 'string')
        self.set_attribute(petAttributes.STATUS, 'available')
        self.set_attribute(petAttributes.PHOTO_URLS, ['string'])


