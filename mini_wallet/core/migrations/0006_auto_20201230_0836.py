# Generated by Django 3.1.4 on 2020-12-30 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_usertransaction_statis_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertransaction',
            name='reference_id',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]