import requests
from requests.auth import HTTPBasicAuth

class Requestor(object):
  def __init__(self, user=None, password=None):
    self.auth = HTTPBasicAuth(user, password)

  def get(self, url, params=None, json=None, headers=None):
    return requests.get(url, params=params, json=json, auth=self.auth, headers=headers)

  def post(self, url, params=None, json=None, headers=None):
    return requests.post(url, params=params, json=json, auth=self.auth, headers=headers)

  def put(self, url, params=None, json=None, headers=None):
    return requests.put(url, params=params, json=json, auth=self.auth, headers=headers)

  def delete(self, url, params=None, json=None, headers=None):
    return requests.delete(url, params=params, json=json, auth=self.auth, headers=headers)
