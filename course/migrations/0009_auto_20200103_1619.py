# Generated by Django 3.0.1 on 2020-01-03 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_auto_20200103_0028'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='module',
            options={'ordering': ['order'], 'verbose_name': 'Module'},
        ),
        migrations.AddField(
            model_name='module',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]