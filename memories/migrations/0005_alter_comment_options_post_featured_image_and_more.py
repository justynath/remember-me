# Generated by Django 4.2.16 on 2024-12-16 16:41

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memories', '0004_favourite'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_on']},
        ),
        migrations.AddField(
            model_name='post',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='post',
            name='theme',
            field=models.CharField(choices=[('childhood', 'Childhood'), ('school', 'School'), ('work', 'Work'), ('holidays', 'Holidays'), ('family', 'Family'), ('finn', 'Finn'), ('friends', 'Friends'), ('football', 'Football')], max_length=100),
        ),
    ]
