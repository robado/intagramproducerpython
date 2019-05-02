from pprint import pprint
from producer.endpoint import requester

token = '104907068.f67ebf1.3ed44e8f93254c3ba4b50ff03143feaa'  # <----- Insert your Instagram token here


class InstagramAPI:
    pprint(requester.user_endpoint(token)) # pprint is for pretty print so it is easier to read
