# Generated by Django 4.2.4 on 2023-08-21 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog_shelters', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dog',
            name='adoption_date',
        ),
        migrations.AlterField(
            model_name='dog',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='dog',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='shelter',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]