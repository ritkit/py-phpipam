""" Maintain a list of functions within the PHPIpam API
"""
resource_types = {
    'sections' : {
        'getSubnets':{
            'method':'GET',
            'request':'/sections/{object_id}/subnets/'
        },
        'getByName':{
            'method':'GET',
            'request':'/sections/{name}/subnets/'
        }
    },
    'subnets' : {
        'search':{
            'method':'GET',
            'request':'/subnets/search/{search}'
        },
        'getIP':{
            'method':'GET',
            'request':'/subnets/{object_id}/addresses/{ip}/'
        },
        'getAddresses':{
            'method':'GET',
            'request':'/subnets/{object_id}/addresses/'
        },
    },
    'addresses' : {
        'getByIP':{
            'method':'GET',
            'request':'/addresses/{ip}/{object_id}/'
        },
        'getByTag':{
            'method':'GET',
            'request':'/addresses/tags/{object_id}/addresses/'
        },
        'search':{
            'method':'GET',
            'request':'/addresses/search/{ip}/'
        },
        'getFirstFree':{
            'method':'GET',
            'request':'/addresses/first_free/{object_id}/'
        },
        'getTags':{
            'method':'GET',
            'request':'/addresses/tags/'
        },
        'getTag':{
            'method':'GET',
            'request':'/addresses/tags/{object_id}/'
        },
        'createFirstFree':{
            'method':'POST',
            'request':'/addresses/first_free/{object_id}/'
        }
    },
    'vlan':{},
    'l2domains':{},
    'vrf':{},
    'devices' : {
        'getAddresses':{
            'method':'GET',
            'request':'/devices/{object_id}/addresses/'
        },
        'getSubnets':{
            'method':'GET',
            'request':'/devices/{object_id}/subnets/'
        }
    },
    'prefix':{},
}