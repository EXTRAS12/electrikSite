# Generated by Django 3.2.7 on 2021-09-30 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worklist',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Фотография для Вас'),
        ),
    ]
