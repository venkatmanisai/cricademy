# Generated by Django 3.0.5 on 2020-05-05 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('tests', '0003_auto_20200505_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile'),
        ),
    ]
