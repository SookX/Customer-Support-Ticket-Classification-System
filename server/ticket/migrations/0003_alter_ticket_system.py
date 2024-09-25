# Generated by Django 5.0.4 on 2024-09-25 19:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
        ('ticket', '0002_ticket_system'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='system',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ticket_system', to='system.system'),
            preserve_default=False,
        ),
    ]
