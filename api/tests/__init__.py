from django.test import Client, TestCase


class AbstractTestCase(TestCase):

    def setUp(self):
        self.client = Client()

        self.header = {'Authorization': '14ed93dc-a58a-4fdb-b53b-5757685c69d7'}
        self.other_header = {'Authorization': 'd71dfddc-fad8-4dc1-8941-0109fa54d62c'}
