# Generated by Django 5.1.6 on 2025-02-27 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=9)),
                ('logradouro', models.CharField(max_length=50)),
                ('bairro', models.CharField(max_length=30)),
                ('localidade', models.CharField(max_length=30)),
                ('uf', models.CharField(max_length=2)),
            ],
        ),
    ]
