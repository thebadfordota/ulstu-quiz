# Generated by Django 4.0.4 on 2022-05-23 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_studygroup'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='group_id',
            field=models.ManyToManyField(to='accounts.studygroup', verbose_name='Для следующих учебных групп'),
        ),
        migrations.DeleteModel(
            name='StudyGroup',
        ),
    ]