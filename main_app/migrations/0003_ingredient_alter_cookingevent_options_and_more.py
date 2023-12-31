# Generated by Django 4.2.6 on 2023-11-01 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_cookingevent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('food_group', models.CharField(choices=[('fruit', 'Fruit'), ('vegetable', 'Vegetable'), ('grain', 'Grain'), ('protein', 'Protien'), ('dairy', 'Dairy'), ('sugar', 'Sugar')], default='fruit', max_length=30)),
            ],
        ),
        migrations.AlterModelOptions(
            name='cookingevent',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='cookingevent',
            name='date',
            field=models.DateField(verbose_name='Cooking Event Date'),
        ),
    ]
