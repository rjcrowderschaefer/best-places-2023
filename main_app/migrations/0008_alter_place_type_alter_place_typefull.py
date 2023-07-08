# Generated by Django 4.2.2 on 2023-07-08 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_alter_place_type_alter_place_typefull'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='type',
            field=models.CharField(choices=[('CR', 'CR'), ('FW', 'FW'), ('BT', 'BT'), ('MW', 'MW'), ('FN', 'FN'), ('BV', 'BV'), ('TF', 'TF')], max_length=6),
        ),
        migrations.AlterField(
            model_name='place',
            name='typefull',
            field=models.CharField(choices=[('For Cultural Riches', 'For Cultural Riches'), ('For the Food - And Wine', 'For the Food - And Wine'), ('For Big-city Thrills', 'For Big-city Thrills'), ('For Moments On The Water', 'For Moments On The Water'), ('For Fresh Air and Nature', 'For Fresh Air and Nature'), ('For Beach Vibes', 'For Beach Vibes'), ('For A Look At The Future', 'For A Look At The Future')], max_length=50),
        ),
    ]