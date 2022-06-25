from enum import Enum

#enum class to store the create pet payload keys order
class petAttributesPayloadKeysOrder(Enum):
    id = 0
    category = 1
    name = 2
    photoUrls = 3
    tags = 4
    status = 5

