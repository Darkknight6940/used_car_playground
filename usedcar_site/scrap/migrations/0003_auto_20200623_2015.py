# Generated by Django 3.0.7 on 2020-06-23 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0002_auto_20200623_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelcode',
            name='code',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
