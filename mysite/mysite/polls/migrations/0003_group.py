# Generated by Django 2.0.4 on 2018-05-28 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20180528_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('members', models.ManyToManyField(to='polls.Person')),
            ],
        ),
    ]