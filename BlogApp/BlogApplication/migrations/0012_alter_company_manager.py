# Generated by Django 4.0.10 on 2023-10-04 21:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BlogApplication', '0011_alter_company_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='managed_company', to=settings.AUTH_USER_MODEL),
        ),
    ]