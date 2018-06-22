# Generated by Django 2.0.2 on 2018-04-26 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180426_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='watch_course.Course'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='course_index',
            field=models.IntegerField(default=1),
        ),
    ]