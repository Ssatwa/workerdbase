# Generated by Django 4.2.3 on 2023-07-31 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField()),
                ('education', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'worker',
            },
        ),
    ]
