# Generated by Django 5.0.3 on 2024-03-30 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.webp', upload_to='profile_pics'),
        ),
    ]
