from django.core.management.base import BaseCommand
from api.models import BuildingBlock, Situation, Goal, Measure, Strategy, StrategyMeasureInformation, Comment, User


class Command(BaseCommand):

    help = 'Import demo data'

    def handle(self, *args, **options):
        building_block_a, created = BuildingBlock.objects.get_or_create(
            title='BuildingBlock A',
            description='BuildingBlock A description'
        )

        building_block_b, created = BuildingBlock.objects.get_or_create(
            title='BuildingBlock B',
            description='BuildingBlock B description'
        )



        situation_a, created = Situation.objects.get_or_create(
            building_block=building_block_a,
            title='Situation A',
            description='Situation A description'
        )

        situation_b, created = Situation.objects.get_or_create(
            building_block=building_block_a,
            title='Situation B',
            description='Situation B description'
        )

        situation_c, created = Situation.objects.get_or_create(
            building_block=building_block_b,
            title='Situation C',
            description='Situation C description'
        )

        situation_d, created = Situation.objects.get_or_create(
            building_block=building_block_b,
            title='Situation D',
            description='Situation D description'
        )



        goal_a, created = Goal.objects.get_or_create(
            building_block=situation_a,
            title='Goal A',
            description='Goal A description'
        )

        goal_b, created = Goal.objects.get_or_create(
            building_block=situation_a,
            title='Goal B',
            description='Goal B description'
        )

        goal_c, created = Goal.objects.get_or_create(
            building_block=situation_b,
            title='Goal C',
            description='Goal C description'
        )

        goal_d, created = Goal.objects.get_or_create(
            building_block=situation_b,
            title='Goal D',
            description='Goal D description'
        )

        goal_e, created = Goal.objects.get_or_create(
            building_block=situation_c,
            title='Goal E',
            description='Goal E description'
        )

        goal_f, created = Goal.objects.get_or_create(
            building_block=situation_c,
            title='Goal F',
            description='Goal F description'
        )

        goal_g, created = Goal.objects.get_or_create(
            building_block=situation_d,
            title='Goal G',
            description='Goal G description'
        )

        goal_h, created = Goal.objects.get_or_create(
            building_block=situation_d,
            title='Goal H',
            description='Goal H description'
        )



        #user = User.objects.get(email='admin@sysdev.com')



        """strategy_a, created = Strategy.objects.get_or_create(
            user=user,
            title='Strategy A',
            description='Strategy A description'
        )

        strategy_measure_information, created = StrategyMeasureInformation.objects.get_or_create(
            measure=measure_a,
            strategy=strategy_a,
            description='Comment on Measure A in Strategy A'
        )

        strategy_measure_information, created = StrategyMeasureInformation.objects.get_or_create(
            measure=measure_b,
            strategy=strategy_a,
            description='Comment on Measure B in Strategy A'
        )"""
