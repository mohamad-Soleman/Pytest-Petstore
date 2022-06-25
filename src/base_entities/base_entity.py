


class BaseEntity(object):

    #list pf pate names to be randomly selectd when initiating new pet
    pet_names = ['Bella', 'Luna', 'Lucy', 'Daizy', 'Zoe', 'Lily', 'Lola', 'Bailey', 'Stella', 'Molly',
    'Max', 'Charlie', 'Milo', 'Buddy', 'Rocky', 'Bear', 'Leo', 'Duke', 'Teddy', 'Tucker']

    #all the basic operations that can be done on pet entity
    def update(self, kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def get_attribute(self, attribute):
        try:
            return getattr(self, attribute.value)
        except AttributeError:
            raise AttributeError("attribute {} missing".format(attribute))

    def set_attribute(self, attribute, value):
        setattr(self, attribute.value, value)