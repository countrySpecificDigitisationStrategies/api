from api.utils.enum import *
from api.utils.error_code import *


class AppList(list):

    def __init__(self, *args):
        super(AppList, self).__init__(args)

    def __sub__(self, other):
        return self.__class__(*[item for item in self if item not in other])
