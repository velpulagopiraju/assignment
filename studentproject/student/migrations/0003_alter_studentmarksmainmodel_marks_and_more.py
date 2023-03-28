# Generated by Django 4.1.7 on 2023-03-28 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_studentmarksmainmodel_marks_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmarksmainmodel',
            name='marks',
            field=models.ManyToManyField(to='student.studentmarksmodel'),
        ),
        migrations.AlterField(
            model_name='studentmarksmainmodel',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='student.studentmainmodel'),
        ),
    ]