# Generated by Django 5.0.3 on 2024-03-25 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('writer', models.CharField(max_length=20)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('email', models.CharField(max_length=30)),
                ('comment', models.TextField()),
            ],
        ),
    ]
