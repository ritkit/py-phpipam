#
# phpipam/backend.py
# (c) 2021 Jonas Gunz <himself@jonasgunz.de>
# License: MIT
#
import json
import datetime
import requests
from dateutil.parser import parse as datetime_parse

class APIConnectionException(ExceptionGroup):
    pass

class APIQueryException(ExceptionGroup):
    pass

class APIObjectNotFoundException(ExceptionGroup):
    pass

class PhpipamBackend:
    def __init__(self, api_url, app_id, verify, timeout: int = 60, api_user: str = "", api_password: str = "", api_key: str = ""):
        self.api_url = api_url.strip('/') + '/api/' + app_id
        self.api_user = api_user
        self.verify = verify
        self.srv_timeout = timeout

        # Check for static auth
        if api_key == "" and api_password != "":
            self.api_password = api_password
            self._GetApiToken()

        elif api_key != "" and api_password == "":
            self.api_token = api_key
            self.api_token_expires = ""

        else:
            raise AttributeError("Either API Password or API Key must be proved")
        
        self._CheckAccess()

    def _GetApiToken(self):
        data = requests.post(self.api_url + "/user", auth=(self.api_user, self.api_password),
                             verify=self.verify, timeout=self.srv_timeout).json()
        if not data['success']:
            raise APIConnectionException('Failed to authenticate: ' + str(data['code'])
                                         + ' ' + data['message'])

        self.api_token = data['data']['token']
        self.api_token_expires = data['data']['expires']

    def _CheckAccess(self):
        if self._isTokenExpired():
            self._GetApiToken()

        data = requests.get(self.api_url, headers={'token':self.api_token}, verify=self.verify,
                                timeout=self.srv_timeout).json()

        if not 'success' in data or not data['success']:
            raise APIConnectionException("Query failed with code " + str(data['code']) + ": "
                                    + str(data['message']))

        elif data['code'] != 200:
            raise APIConnectionException("Query failed with code " + str(data['code']) + ": "
                                    + str(data['message']))

    def _isTokenExpired(self):
        # static auth does not expire
        if len(self.api_token_expires) == 0:
            return False

        expiration = datetime_parse(self.api_token_expires)

        return expiration < datetime.datetime.now()

    def request ( self, method, url, data: dict = None):
        if self._isTokenExpired():
            self._GetApiToken()

        data = requests.request(method, self.api_url + url, data=data, 
                                headers={'token':self.api_token}, verify=self.verify,
                                timeout=self.srv_timeout).json()

        if not 'success' in data or not data['success']:
            raise APIQueryException("Query failed with code " + str(data['code']) + ": " + str(data['message']))

        if 'data' in data:
            return data['data']

        return data
