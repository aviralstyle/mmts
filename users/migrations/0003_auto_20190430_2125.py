# Generated by Django 2.2 on 2019-04-30 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190430_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_of_birth',
            field=models.DateTimeField(blank=True),
        ),
    ]
