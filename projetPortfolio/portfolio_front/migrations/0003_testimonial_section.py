# Generated by Django 5.2 on 2025-04-24 10:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_front', '0002_servicecard_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='section',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='testimonials', to='portfolio_front.testimonialsection'),
        ),
    ]
