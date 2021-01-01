# Generated by Django 3.1.4 on 2021-01-01 12:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_premiumjob_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='rating',
            field=models.PositiveSmallIntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='job_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_type', to='core.jobtype'),
        ),
        migrations.AlterField(
            model_name='order',
            name='premium_job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='premium_job', to='core.premiumjob'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'pending'), (2, 'Approved'), (3, 'Accepted'), (4, 'Amends_requested'), (5, 'Rejected')], null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject', to='core.subject'),
        ),
    ]