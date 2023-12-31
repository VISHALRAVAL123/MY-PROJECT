# Generated by Django 4.1.4 on 2022-12-31 11:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vishalapp', '0006_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vishalapp.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vishalapp.user')),
            ],
        ),
    ]
