#
# phpipam/resources.py
# (c) 2021 Jonas Gunz <himself@jonasgunz.de>
# License: MIT
#
from .backend import PhpIpamBackend

# Custom functions are defined here
resource_types = {
    'sections' : {
        'getSubnets':{
            'method':'GET',
            'request':'/sections/{section_id}/subnets',
        }
    },
    'subnets' : {
        'search':{
            'method':'GET',
            'request':'/subnets/search/{search}'
        },
        'getIP':{
            'method':'GET',
            'request':'/subnets/{subnet_id}/addresses/{ip}/'
        },
        'getAddresses':{
            'method':'GET',
            'request':'/subnets/{subnet_id}/addresses/'
        },
    },
    'addresses' : {
        'getByIP':{
            'method':'GET',
            'request':'/addresses/{ip}/{subnet_id}/'
        },
        'getByTag':{
            'method':'GET',
            'request':'/addresses/tags/{tag_id}/addresses/'
        },
        'search':{
            'method':'GET',
            'request':'/addresses/search/{ip}/'
        },
        'getFirstFree':{
            'method':'GET',
            'request':'/addresses/first_free/{subnet_id}/'
        },
        'getTags':{
            'method':'GET',
            'request':'/addresses/tags/'
        },
        'getTag':{
            'method':'GET',
            'request':'/addresses/tags/{tag_id}/'
        },
        'createFirstFree':{
            'method':'POST',
            'request':'/addresses/first_free/{subnet_id}/'
        }
    },
    'vlan':{},
    'l2domains':{},
    'vrf':{},
    'devices' : {
        'getAddresses':{
            'method':'GET',
            'request':'/devices/{device_id}/addresses/'
        },
        'getSubnets':{
            'method':'GET',
            'request':'/devices/{device_id}/subnets/'
        }
    },
    'prefix':{},
}

class PhpIpamResourceFunction:
    def __init__(self, backend, resource, function):
        if not function in resource_types[resource]:
            raise NotImplementedError(f'Operation {function} is not defined for {resource}.')

        self._backend = backend
        self._resource = resource
        self._function = resource_types[resource][function]
        self._name = function

    def __call__(self, **kwargs):
        if 'data' in kwargs:
            data = kwargs['data']
        else:
            data = {}
        try:
            return self._backend.request( self._function['method'], self._function['request'].format(**kwargs), data=data )
        except KeyError as e:
            raise AttributeError( f"{self._resource}.{self._name}: Missing arguments: {e.args}" ) from e


class PhpIpamResource:
    def __init__(self, backend, resource):
        if not resource in resource_types:
            raise NotImplementedError(f'Invalid resource "{resource}"')

        self._type = resource
        self._backend = backend

    def __getattr__(self, attr):
        return PhpIpamResourceFunction(self._backend, self._type, attr)

    # Functions every ObjectType shares

    def get(self):
        """List of all objects"""
        return self._backend.request('GET', f'/{self._type}')

    def byID(self, object_id):
        """object identified by object_id : str"""
        return self._backend.request('GET', f'/{self._type}/{object_id}')

    def create(self, data):
        return self._backend.request('POST', f'/{self._type}/', data=data)

    def patch(self, object_id, data):
        return self._backend.request('PATCH', f'/{self._type}/{object_id}', data=data)

    def delete(self, object_id):
        return self._backend.request('DELETE', f'/{self._type}/{object_id}')