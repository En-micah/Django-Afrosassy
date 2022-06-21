# Generated by Django 2.2.14 on 2022-06-21 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paystack_payment', '0001_initial'),
        ('core_shop', '0003_auto_20220620_2016'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payment',
            options={},
        ),
        migrations.RemoveField(
            model_name='payment',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='email',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='id',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='ref',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='verified',
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_ptr',
            field=models.OneToOneField(auto_created=True, default='none for now', on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='paystack_payment.Payment'),
            preserve_default=False,
        ),
    ]
