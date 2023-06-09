# Generated by Django 4.1.7 on 2023-03-28 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentMainModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Dob', models.DateField(default=True)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('others', 'others')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StudentMarksModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Marks', models.CharField(max_length=50)),
                ('sem', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], max_length=200)),
                ('student', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='student.studentmainmodel')),
            ],
        ),
        migrations.CreateModel(
            name='studentMarksMainModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(choices=[('Mech', 'Mech'), ('csc', 'csc'), ('ece', 'ece'), ('it', 'it'), ('civil', 'civil')], max_length=100)),
                ('marks', models.ManyToManyField(to='student.studentmarksmodel')),
                ('student', models.OneToOneField(default=2, on_delete=django.db.models.deletion.CASCADE, to='student.studentmainmodel')),
            ],
        ),
    ]
