# Generated by Django 5.0.3 on 2024-04-12 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_dogcalculator'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dogcalculator',
            old_name='dog',
            new_name='dog_weight',
        ),
        migrations.AddField(
            model_name='dogcalculator',
            name='servingspercup',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]