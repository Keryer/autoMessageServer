# Generated by Django 5.0.1 on 2024-02-03 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoMessageServer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField()),
                ('username', models.CharField(max_length=32)),
                ('message', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(default=0)),
            ],
        ),
    ]
