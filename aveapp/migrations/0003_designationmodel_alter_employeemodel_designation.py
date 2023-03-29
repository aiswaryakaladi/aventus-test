# Generated by Django 4.1.7 on 2023-03-29 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aveapp', '0002_alter_employeemodel_designation_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='designationmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='employeemodel',
            name='designation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aveapp.designationmodel'),
        ),
    ]
