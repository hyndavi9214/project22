# Generated by Django 4.2.7 on 2023-12-08 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cname', models.CharField(max_length=100)),
                ('Code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Captial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpname', models.CharField(max_length=100)),
                ('Code', models.IntegerField()),
                ('Cname', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.country')),
            ],
        ),
    ]