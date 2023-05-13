# Generated by Django 4.2 on 2023-05-08 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='id')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('allergen', models.ManyToManyField(blank=True, to='app.allergen')),
            ],
            options={
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menu',
            },
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.PositiveIntegerField(verbose_name='day')),
                ('breakfast', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='breakfast', to='app.product')),
                ('dinner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dinner', to='app.product')),
                ('lunch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lunch', to='app.product')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.menu')),
            ],
            options={
                'verbose_name': 'Recommendation',
                'verbose_name_plural': 'Recommendations',
            },
        ),
    ]