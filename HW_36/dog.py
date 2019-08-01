import requests

DOG_URL = 'https://dog.ceo/api/breeds/list/all'
SUB_BREEDS = 'https://dog.ceo/api/breed/hound/list'


def get_breeds():
    """Get list of breeds"""
    response = requests.get(DOG_URL)
    if response.ok:
        return response
    else:
        return None


def get_sub_breeds():
    """Get list of hound sub-breeds"""
    response = requests.get(SUB_BREEDS)
    if response.status_code == 200:
        return response
    else:
        return None
