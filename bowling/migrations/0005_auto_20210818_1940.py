# Generated by Django 3.1.5 on 2021-08-18 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bowling', '0004_auto_20210818_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalthrow',
            name='frame',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='throws', to='bowling.personalframe'),
        ),
    ]
