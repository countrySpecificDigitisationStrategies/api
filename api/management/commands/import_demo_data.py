from django.core.management.base import BaseCommand

from api.models import BuildingBlock, Situation, Goal, Measure, Country, User, Strategy, StrategyMeasure, Thread, Comment


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
            situation=situation_a,
            title='Goal A',
            description='Goal A description'
        )

        goal_b, created = Goal.objects.get_or_create(
            situation=situation_a,
            title='Goal B',
            description='Goal B description'
        )

        goal_c, created = Goal.objects.get_or_create(
            situation=situation_b,
            title='Goal C',
            description='Goal C description'
        )

        goal_d, created = Goal.objects.get_or_create(
            situation=situation_b,
            title='Goal D',
            description='Goal D description'
        )

        goal_e, created = Goal.objects.get_or_create(
            situation=situation_c,
            title='Goal E',
            description='Goal E description'
        )

        goal_f, created = Goal.objects.get_or_create(
            situation=situation_c,
            title='Goal F',
            description='Goal F description'
        )

        goal_g, created = Goal.objects.get_or_create(
            situation=situation_d,
            title='Goal G',
            description='Goal G description'
        )

        goal_h, created = Goal.objects.get_or_create(
            situation=situation_d,
            title='Goal H',
            description='Goal H description'
        )



        measure_a, created = Measure.objects.get_or_create(
            goal=goal_a,
            title='Measure A',
            description='Measure A description'
        )

        measure_b, created = Measure.objects.get_or_create(
            goal=goal_b,
            title='Measure B',
            description='Measure B description'
        )

        measure_c, created = Measure.objects.get_or_create(
            goal=goal_c,
            title='Measure C',
            description='Measure C description'
        )

        measure_d, created = Measure.objects.get_or_create(
            goal=goal_d,
            title='Measure D',
            description='Measure D description'
        )



        country_a, created = Country.objects.get_or_create(name='Country A')
        country_b, created = Country.objects.get_or_create(name='Country B')



        user_a, created = User.objects.get_or_create(email='admin@sysdev.com', is_active=True, is_staff=True, is_superuser=True)
        user_a.set_password('password')
        user_a.save()

        user_b, created = User.objects.get_or_create(email='admin_2@sysdev.com', is_active=True, is_staff=True, is_superuser=True)
        user_b.set_password('password')
        user_b.save()



        strategy_a, created = Strategy.objects.get_or_create(
            user=user_a,
            country=country_a,
            title='Strategy A',
            description='Strategy A description',
            is_published=True
        )

        strategy_b, created = Strategy.objects.get_or_create(
            user=user_b,
            country=country_b,
            title='Strategy B',
            description='Strategy B description',
            is_published=True
        )



        strategy_measure_a, created = StrategyMeasure.objects.get_or_create(
            strategy=strategy_a,
            measure=measure_a,
            description='Details on Measure A in Strategy A'
        )

        strategy_measure_b, created = StrategyMeasure.objects.get_or_create(
            strategy=strategy_a,
            measure=measure_b,
            description='Details on Measure B in Strategy A'
        )

        strategy_measure_c, created = StrategyMeasure.objects.get_or_create(
            strategy=strategy_b,
            measure=measure_c,
            description='Details on Measure C in Strategy B'
        )

        strategy_measure_d, created = StrategyMeasure.objects.get_or_create(
            strategy=strategy_b,
            measure=measure_d,
            description='Details on Measure D in Strategy B'
        )



        thread_a, created = Thread.objects.get_or_create(
            user=user_a,
            strategy_measure=strategy_measure_a,
            title='Thread A',
            description='Thread A description'
        )

        thread_b, created = Thread.objects.get_or_create(
            user=user_b,
            strategy_measure=strategy_measure_b,
            title='Thread B',
            description='Thread B description'
        )



        comment_a, created = Comment.objects.get_or_create(
            user=user_b,
            thread=thread_a,
            parent=None,
            description='Comment A description'
        )

        comment_b, created = Comment.objects.get_or_create(
            user=user_a,
            thread=thread_a,
            parent=comment_a,
            description='Comment B description'
        )

        comment_c, created = Comment.objects.get_or_create(
            user=user_a,
            thread=thread_b,
            parent=None,
            description='Comment C description'
        )

        comment_d, created = Comment.objects.get_or_create(
            user=user_b,
            thread=thread_a,
            parent=comment_c,
            description='Comment D description'
        )
