# Generated by Django 4.2.6 on 2023-11-01 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_ingredient_alter_cookingevent_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(to='main_app.ingredient'),
        ),
    ]