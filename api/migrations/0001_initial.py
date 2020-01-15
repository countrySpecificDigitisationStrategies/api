# Generated by Django 2.2.9 on 2020-01-15 18:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('email', models.EmailField(max_length=50, unique=True, verbose_name='email')),
                ('firstname', models.CharField(blank=True, max_length=50, null=True, verbose_name='firstname')),
                ('lastname', models.CharField(blank=True, max_length=50, null=True, verbose_name='lastname')),
                ('is_admin', models.BooleanField(default=False, verbose_name='is_admin')),
                ('is_representative', models.BooleanField(default=False, verbose_name='is_representative')),
                ('is_moderator', models.BooleanField(default=False, verbose_name='is_moderator')),
                ('is_active', models.BooleanField(default=True, verbose_name='is_active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='is_staff')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='is_superuser')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
        migrations.CreateModel(
            name='BuildingBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('title', models.CharField(max_length=250, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
            ],
            options={
                'verbose_name': 'building_block',
                'verbose_name_plural': 'building_blocks',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('name', models.CharField(max_length=250, verbose_name='name')),
                ('flag', models.ImageField(blank=True, null=True, upload_to='flag/')),
                ('flag_circle', models.ImageField(blank=True, null=True, upload_to='flag_circle/')),
                ('flag_rectangle', models.ImageField(blank=True, null=True, upload_to='flag_rectangle/')),
                ('is_developing_country', models.BooleanField(default=False, verbose_name='is_developing_country')),
            ],
            options={
                'verbose_name': 'country',
                'verbose_name_plural': 'countries',
            },
        ),
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('title', models.CharField(max_length=250, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
            ],
            options={
                'verbose_name': 'measure',
                'verbose_name_plural': 'measures',
            },
        ),
        migrations.CreateModel(
            name='Strategy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('title', models.CharField(max_length=250, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('is_published', models.BooleanField(default=False, verbose_name='is_published')),
                ('country', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='api.Country', verbose_name='country')),
            ],
            options={
                'verbose_name': 'strategy',
                'verbose_name_plural': 'strategies',
            },
        ),
        migrations.CreateModel(
            name='StrategyMeasure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('measure', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='strategy_measures', to='api.Measure')),
                ('strategy', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='strategy_measures', to='api.Strategy')),
            ],
            options={
                'verbose_name': 'strategy_measure',
                'verbose_name_plural': 'strategy_measures',
            },
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('code', models.UUIDField(default=uuid.uuid4, unique=True, verbose_name='code')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tokens', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'token',
                'verbose_name_plural': 'tokens',
            },
        ),
        migrations.CreateModel(
            name='StrategyMeasureThread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('title', models.CharField(max_length=250, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('strategy_measure', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='strategy_measure_threads', to='api.StrategyMeasure', verbose_name='strategy_measure')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='strategy_measure_threads', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'strategy_measure_thread',
                'verbose_name_plural': 'strategy_measure_threads',
            },
        ),
        migrations.CreateModel(
            name='StrategyMeasureComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('description', models.TextField(verbose_name='description')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='strategy_measure_comments', to='api.StrategyMeasureComment', verbose_name='parent')),
                ('strategy_measure_thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='strategy_measure_comments', to='api.StrategyMeasureThread', verbose_name='strategy_measure_thread')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='strategy_measure_comments', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'strategy_measure_comment',
                'verbose_name_plural': 'strategy_measure_comments',
            },
        ),
        migrations.AddField(
            model_name='strategy',
            name='measures',
            field=models.ManyToManyField(through='api.StrategyMeasure', to='api.Measure', verbose_name='measures'),
        ),
        migrations.AddField(
            model_name='strategy',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='strategies', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.CreateModel(
            name='SituationCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('title', models.CharField(max_length=250, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('goal_title', models.CharField(max_length=250, verbose_name='goal_title')),
                ('goal_description', models.TextField(verbose_name='goal_description')),
                ('building_block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='situation_categories', to='api.BuildingBlock', verbose_name='building_block')),
            ],
            options={
                'verbose_name': 'situation_category',
                'verbose_name_plural': 'situation_categories',
            },
        ),
        migrations.CreateModel(
            name='Situation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('title', models.CharField(max_length=250, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('situation_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='situations', to='api.SituationCategory', verbose_name='situation_category')),
            ],
            options={
                'verbose_name': 'situation',
                'verbose_name_plural': 'situations',
            },
        ),
        migrations.CreateModel(
            name='PasswordReset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('code', models.UUIDField(default=uuid.uuid4, unique=True, verbose_name='code')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='password_resets', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'password_reset',
                'verbose_name_plural': 'password_resets',
            },
        ),
        migrations.AddField(
            model_name='measure',
            name='situation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measures', to='api.Situation', verbose_name='situation'),
        ),
        migrations.CreateModel(
            name='EmailConfirmation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('code', models.UUIDField(default=uuid.uuid4, unique=True, verbose_name='code')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='email_confirmations', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'email_confirmation',
                'verbose_name_plural': 'email_confirmations',
            },
        ),
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('title', models.CharField(max_length=250, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('country', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='api.Country', verbose_name='country')),
            ],
            options={
                'verbose_name': 'analysis',
                'verbose_name_plural': 'analyses',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='api.Country', verbose_name='country'),
        ),
        migrations.AddField(
            model_name='user',
            name='current_country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='current_country_users', to='api.Country', verbose_name='current_country'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
