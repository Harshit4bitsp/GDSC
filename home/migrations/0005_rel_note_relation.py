# Generated by Django 4.0.5 on 2022-06-02 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_note_tag_note_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='rel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='note',
            name='relation',
            field=models.ManyToManyField(blank=True, to='home.rel'),
        ),
    ]
