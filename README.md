# phpipam-api

## About
A further addition to the incomplete phpIPAM API implementation in python.

Can make a variety of calls out to PHP 

### Attribution
Thanks to Jonas Gunz and his initial [git project](https://github.com/kompetenzbolzen/python-phpipam).

## Getting started
Super easy drop this into folder anywhere, no need to install it. 
Use `pip install -e <folder location>` to install it into whatever project that calls it.

## Usage
```
import phpipamapi

ipam = phpipamapi.caller("https://phpipam.example.com/", "myapp", api_user="apiuser", api_password="p4s5word")

data = ipam.<controller>.<operation>(<arguments>)
```

A key can be defined in phpipam to be used for an API call instead. If you are going to use a key, replace the caller function with the following.

```
ipam = phpipamapi.caller("https://phpipam.example.com/", "myapp", 
api_key="thisi$afakek3y")
```

All functions return a dictionary object or a list of dictionary objects.
Refer to the [API Doc](https://phpipam.net/api-documentation/) for data layout.
If an error is encountered, an exception is raised.

### Controllers

Functions shared by all controllers:

* `get()` returns all obejcts in in controller
* `byID(object_id=<object id>)` get specific obejct by ID
* `create(object_id=<object id>, data=<data>)`
* `edit(object_id=<object id>, data=<data>)`
* `delete(object_id=<object id>)`

#### sections

* `getSubnets(section_id=<section id>)`

#### subnets

* `search(search=<query>)` search for subnet by CIDR
* `getIP(subnet_id=<subnet id>, ip=<ip>)` get address object from subnet by IP
* `getAddresses(subnet_id=<subnet id>)` get all addresses in subnet

#### addresses

* `getByIP(subnet_id=<subnet id>, ip=<ip>)`
* `getByTag(tag_id=<tag id>)`
* `search(ip=<ip>)`
* `getFirstFree(subnet_id=<subnet id>)`
* `getTags()`
* `getTag(tag_id=<tag id>)`
* `createFirstFree(subnet_id=<subnet id>)`

#### vlan

#### l2domains

#### vrf

#### devices

* `getAddresses(device_id=<device id>)`
* `getSubnets(device_id=<device id>)`

#### prefix


## Requirements

* `dateutil`
* `requests`

## License
Distributed under the MIT License. See `LICENSE.txt` for more information.
