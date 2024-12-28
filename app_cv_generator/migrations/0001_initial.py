# Generated by Django 5.1.3 on 2024-11-06 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('address', models.TextField(max_length=1000)),
                ('city', models.CharField(max_length=1000)),
                ('state', models.CharField(max_length=1000)),
                ('pin_code', models.CharField(max_length=1000)),
                ('contact_number', models.CharField(max_length=1000)),
                ('email', models.EmailField(max_length=254)),
                ('linkedin_id', models.URLField(default=None)),
                ('summary', models.TextField(max_length=10000)),
                ('skills', models.TextField(max_length=10000)),
                ('experience', models.TextField(max_length=10000)),
                ('higher_secondary', models.CharField(max_length=1000)),
                ('degree', models.CharField(max_length=1000)),
                ('certificates', models.TextField(max_length=1000)),
                ('projects', models.TextField(max_length=10000)),
            ],
        ),
    ]