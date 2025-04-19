# Generated by Django 5.1.3 on 2025-04-19 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClickTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('click_trans_id', models.BigIntegerField()),
                ('service_id', models.IntegerField()),
                ('click_paydoc_id', models.BigIntegerField()),
                ('merchant_trans_id', models.CharField()),
                ('amount', models.FloatField()),
                ('action', models.SmallIntegerField()),
                ('error', models.IntegerField()),
                ('error_note', models.CharField()),
                ('sign_time', models.CharField()),
                ('sign_string', models.CharField()),
                ('merchant_prepare_id', models.IntegerField(blank=True, null=True)),
                ('merchant_confirm_id', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
