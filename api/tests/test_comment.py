from api.tests import AbstractTestCase
from api.models import Pillar, BuildingBlock, Measure, Comment


class CommentTestCase(AbstractTestCase):

    fixtures = ['user', 'token']

    def setUp(self):
        super().setUp()

        self.pillar = Pillar.objects.create(title='pillar')

        self.building_block = BuildingBlock.objects.create(pillar=self.pillar, title='building-block')

        self.measure = Measure.objects.create(building_block=self.building_block, title='measure')

    def test_list(self):
        Comment.objects.create(measure=self.measure)
        Comment.objects.create(measure=self.measure)

        response = self.client.get(
            '/api/v1/comments'
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def test_retrieve(self):
        comment = Comment.objects.create(measure=self.measure)

        response = self.client.get(
            '/api/v1/comments/{}'.format(comment.id)
        )

        self.assertEqual(response.status_code, 200)
