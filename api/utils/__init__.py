from random import choices

from requests.auth import HTTPBasicAuth

from api.utils.enum import *
from api.utils.error_code import *
from api.utils.error_response import *
from api.utils.validator import *


class AppList(list):

    def __init__(self, *args):
        super(AppList, self).__init__(args)

    def __sub__(self, other):
        return self.__class__(*[item for item in self if item not in other])


mainnet_url = 'http://157.230.31.149:18332'

testnet_url = 'http://157.245.22.149:18332'

headers = {'content-type': 'application/json'}

auth = HTTPBasicAuth('a', 'b')

mainnet_address = ''

testnet_address = 'tb1qv2fsuae65ul7es4se5wqg9uhdfjagc866e3w98'


def url_from_network(network) -> str:
    if network == MAINNET:
        return mainnet_url
    return testnet_url


def address_pool_from_network(network) -> str:
    if network == MAINNET:
        return mainnet_address_pool
    return testnet_address_pool


def generate_code() -> str:
    return ''.join(choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=10))
