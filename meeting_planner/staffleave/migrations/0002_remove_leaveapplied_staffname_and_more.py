# Generated by Django 4.0.2 on 2022-04-22 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staffleave', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leaveapplied',
            name='staffname',
        ),
        migrations.AlterField(
            model_name='leaveapplied',
            name='staffid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staffleave.staffdetails'),
        ),
    ]
