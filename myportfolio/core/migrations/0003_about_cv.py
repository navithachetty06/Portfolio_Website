# Generated by Django 5.0 on 2023-12-30 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='cv',
            field=models.FileField(default='default_cv.pdf', upload_to='cv'),
        ),
    ]