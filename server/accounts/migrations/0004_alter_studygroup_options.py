# Generated by Django 4.0.4 on 2022-05-25 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_advanceduser_group_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studygroup',
            options={'ordering': ['id'], 'verbose_name': ' Учебная группа', 'verbose_name_plural': 'Учебные группы'},
        ),
    ]
