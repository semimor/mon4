# Generated by Django 4.1.5 on 2023-02-02 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0002_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='commentable',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.CharField(max_length=255),
        ),
    ]
