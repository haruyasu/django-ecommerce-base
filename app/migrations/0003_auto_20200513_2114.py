# Generated by Django 2.2.12 on 2020-05-13 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200513_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='billing_address',
        ),
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='BilllingAddress',
        ),
    ]