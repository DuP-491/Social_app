# Generated by Django 3.0.3 on 2020-05-14 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Group', '0005_group_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='type',
            field=models.IntegerField(choices=[(0, 'Closed'), (1, 'Open')], default=1),
        ),
        migrations.AlterField(
            model_name='groupmember',
            name='auth',
            field=models.IntegerField(choices=[(0, 'President'), (1, 'Core-Member'), (2, 'Elder'), (3, 'Member')], default=3),
        ),
    ]
