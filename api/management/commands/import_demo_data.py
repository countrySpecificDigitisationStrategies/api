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



        measure_a, created = Measure.objects.get_or_create(
            building_block=building_block_a,
            title='Measure A',
            description='Measure A description'
        )

        measure_b, created = Measure.objects.get_or_create(
            building_block=building_block_a,
            title='Measure B',
            description='Measure B description'
        )

        measure_c, created = Measure.objects.get_or_create(
            building_block=building_block_b,
            title='Measure C',
            description='Measure C description'
        )

        measure_d, created = Measure.objects.get_or_create(
            building_block=building_block_b,
            title='Measure D',
            description='Measure D description'
        )

        measure_e, created = Measure.objects.get_or_create(
            building_block=building_block_c,
            title='Measure E',
            description='Measure E description'
        )

        measure_f, created = Measure.objects.get_or_create(
            building_block=building_block_c,
            title='Measure F',
            description='Measure F description'
        )

        measure_g, created = Measure.objects.get_or_create(
            building_block=building_block_d,
            title='Measure G',
            description='Measure G description'
        )

        measure_h, created = Measure.objects.get_or_create(
            building_block=building_block_d,
            title='Measure H',
            description='Measure H description'
        )



        user = User.objects.get(email='admin@sysdev.com')



        strategy_a, created = Strategy.objects.get_or_create(
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
        )
