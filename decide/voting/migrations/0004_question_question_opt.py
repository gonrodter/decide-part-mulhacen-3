# Generated by Django 2.0 on 2021-12-07 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0003_auto_20180605_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_opt',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]