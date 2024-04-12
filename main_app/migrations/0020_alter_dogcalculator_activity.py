from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0019_alter_dogcalculator_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dogcalculator',
            name='activity',
            field=models.CharField(choices=[(60.82, 'typical'), (69.18, 'active'), (38.77, 'overweight'), (96.92, 'high_activity'), (49.79, 'senior'), (49.79, 'inactive'), (77.36, 'light_duty'), (89.99, 'med_duty'), (117.63, 'high_duty')], default=60.82),
        ),
    ]
