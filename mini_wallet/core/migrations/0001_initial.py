# Generated by Django 3.1.4 on 2020-12-29 15:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserWallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField(default=0)),
                ('status_wallet', models.BooleanField(default=False)),
                ('disabled_by', models.CharField(max_length=200)),
                ('disabled_at', models.DateTimeField(editable=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_transaction', models.CharField(max_length=50)),
                ('amount', models.IntegerField(default=0)),
                ('reference_id', models.CharField(max_length=100)),
                ('updated_by', models.CharField(max_length=200)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('userwallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.userwallet')),
            ],
        ),
    ]
