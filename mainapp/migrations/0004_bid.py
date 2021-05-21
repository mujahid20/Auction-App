# Generated by Django 3.2.3 on 2021-05-19 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_alter_item_minbid'),
    ]

    operations = [
        migrations.CreateModel(
            name='bid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('bidder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.user')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.item')),
            ],
        ),
    ]