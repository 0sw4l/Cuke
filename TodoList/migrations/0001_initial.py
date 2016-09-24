# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('tratamiento', models.CharField(default=None, max_length=15, choices=[(b'Sr', b'Sr'), (b'Srita', b'Srita'), (b'Sra', b'Sra'), (b'Don', b'Don'), (b'Ingeniero', b'Ingeniero'), (b'Doctor', b'Doctor')])),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nota', models.CharField(max_length=50)),
                ('prioridad', models.CharField(default=None, max_length=10, choices=[(b'Urgente', b'Urgente'), (b'Normal', b'Normal'), (b'Relajao', b'Rejalao'), (b'Pendiente', b'Pendiente')])),
                ('completada', models.BooleanField(default=False)),
                ('categoria', models.ForeignKey(to='TodoList.Categoria')),
                ('usuario', models.ForeignKey(to='TodoList.Cliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
