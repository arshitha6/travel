# Generated by Django 3.2.15 on 2022-09-15 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staticapp', '0002_new_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='piks')),
            ],
        ),
        migrations.AlterField(
            model_name='new_place',
            name='name',
            field=models.CharField(max_length=250),
        ),
    ]