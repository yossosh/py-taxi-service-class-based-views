# Generated by Django 4.1 on 2024-05-10 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ['model']},
        ),
        migrations.AlterModelOptions(
            name='driver',
            options={'ordering': ['username']},
        ),
        migrations.AlterModelOptions(
            name='manufacturer',
            options={'ordering': ['name']},
        ),
    ]
