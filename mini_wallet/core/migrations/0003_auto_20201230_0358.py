# Generated by Django 3.1.4 on 2020-12-30 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201229_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userwallet',
            name='disabled_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
