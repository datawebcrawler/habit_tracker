# Generated by Django 5.2.1 on 2025-06-03 01:47

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('scheduled_date', models.DateField(db_column='scheduled_date')),
                ('start_time', models.TimeField()),
                ('status', models.CharField(choices=[('pendente', 'Pendente'), ('feito', 'Feito'), ('adiado', 'Adiado')], default='pendente', max_length=10)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('activity', models.ForeignKey(db_column='activity_id', on_delete=django.db.models.deletion.CASCADE, to='activities.activity')),
            ],
            options={
                'db_table': 'schedule',
            },
        ),
    ]
