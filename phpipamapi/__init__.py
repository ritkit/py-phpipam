#
# phpipam/__init__.py
# (c) 2021 Jonas Gunz <himself@jonasgunz.de>
# License: MIT
#
from .backend import PhpIpamBackend
from .resources import PhpIpamResource

class Caller:
    """
    phpIPAM API Implementation

    Attributes
    ----------
    sections
    subnets
    addresses
    devices

    https://phpipam.net/api-documentation/
    """

    def __init__(self, api_url, app_id, verify = True, timeout = 60, api_user: str = None, api_password: str = None, api_key: str = None):
        """
        Parameters
        ----------
        api_url : str
            URL of phpIPAM instance. Example: https://phpipam.example.com/
        app_id : str
            AppID configrued in API settings
        api_user : str
            username, leave empty to use static token authentification
        api_password : str
            password or static authentification token
        verify : Bool (optional)
            verify API server SSL certificate
        """

        self._backend = PhpIpamBackend(api_url, app_id, verify, timeout, api_user, api_password, api_key)

    def __getattr__(self, item):
        return PhpIpamResource(self._backend, item)
