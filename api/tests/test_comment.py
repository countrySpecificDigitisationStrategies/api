from api.tests import AbstractTestCase
from api.models import BuildingBlock, Situation, Goal, Measure, Comment


class CommentTestCase(AbstractTestCase):

    fixtures = ['country', 'user', 'token']

    def setUp(self):
        super().setUp()

        building_block_a = BuildingBlock.objects.create(title='building_block_a')
        building_block_b = BuildingBlock.objects.create(title='building_block_b')

        situation_a = Situation.objects.create(building_block=building_block_a, title='situation_a')
        situation_b = Situation.objects.create(building_block=building_block_b, title='situation_b')

        goal_a = Goal.objects.create(situation=situation_a, title='goal_a')
        goal_b = Goal.objects.create(situation=situation_b, title='goal_b')

        self.measure_a = Measure.objects.create(goal=goal_a, title='measure_a')
        self.measure_b = Measure.objects.create(goal=goal_b, title='measure_b')

    def test_list(self):
        Comment.objects.create(measure=self.measure_a)
        Comment.objects.create(measure=self.measure_b)

        response = self.client.get(
            '/api/v1/comments'
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

    def test_retrieve(self):
        comment_a = Comment.objects.create(measure=self.measure_a)

        response = self.client.get(
            '/api/v1/comments/{}'.format(comment_a.id)
        )

        self.assertEqual(response.status_code, 200)
