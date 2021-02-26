# Generated by Django 3.1.7 on 2021-02-26 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField()),
                ('whatsapp', models.IntegerField()),
                ('city', models.CharField(max_length=254)),
                ('ur', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Incidents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('description', models.TextField()),
                ('value', models.IntegerField()),
                ('ong', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hero.ong')),
            ],
        ),
    ]
