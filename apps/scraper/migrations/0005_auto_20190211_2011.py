# Generated by Django 2.1.5 on 2019-02-12 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0004_auto_20190210_0949'),
    ]

    operations = [
        migrations.CreateModel(
            name='Refer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('help', models.CharField(max_length=255)),
                ('label', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='element',
            name='refers',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='scraper.Refer'),
            preserve_default=False,
        ),
    ]