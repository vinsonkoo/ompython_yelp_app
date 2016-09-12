from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
from os import environ

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def get_businesses(location, term):
    auth = Oauth1Authenticator(
        consumer_key=environ['CONSUMER_KEY'],
        consumer_secret=environ['CONSUMER_SECRET'],
        token=environ['TOKEN'],
        token_secret=environ['TOKEN_SECRET']
    )

    client = Client(auth)

    params = {
        'term': term,
        'lang': 'en',
        'limit': 10
    }

    response = client.search(location, **params)

    businesses = []

    for business in response.businesses:
        # print(business.name, business.rating, business.phone)
        businesses.append({"name": business.name, 
            "rating": business.rating, 
            "phone": business.phone,
            "address": str(business.location.display_address)[1:-1]
        })

    return businesses[:3]

# businesses = get_businesses('New York City', 'food')

# print(businesses)