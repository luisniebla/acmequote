# Generated by Django 4.2.6 on 2023-10-23 04:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0005_coverage_surcharge_fee'),
    ]

    operations = [
        migrations.AddField(
            model_name='coverage',
            name='area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quote.state'),
        ),
    ]