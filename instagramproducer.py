from pprint import pprint
from producer.endpoint import requester

token = ''  # <----- Insert your Instagram token here


class InstagramAPI:
    pprint(requester.user_endpoint(token)) # pprint is for pretty print so it is easier to read
