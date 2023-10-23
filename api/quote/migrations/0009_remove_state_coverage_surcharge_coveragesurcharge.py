# Generated by Django 4.2.6 on 2023-10-23 04:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0008_alter_coverage_surcharge_fee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state',
            name='coverage_surcharge',
        ),
        migrations.CreateModel(
            name='CoverageSurcharge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee', models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)),
                ('coverage_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quote.coverage')),
                ('state_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quote.state')),
            ],
        ),
    ]