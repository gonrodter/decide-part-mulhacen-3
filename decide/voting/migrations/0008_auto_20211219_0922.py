# Generated by Django 2.0 on 2021-12-19 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0007_auto_20211212_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voting',
            name='question',
            field=models.ManyToManyField(related_name='votings', to='voting.Question'),
        ),
    ]
