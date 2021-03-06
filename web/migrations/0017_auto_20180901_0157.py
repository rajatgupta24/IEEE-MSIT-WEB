# Generated by Django 2.0.4 on 2018-08-31 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0016_auto_20180426_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='SigMentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Full Name')),
                ('contact', models.CharField(max_length=13, verbose_name='Mobile Number')),
            ],
        ),
        migrations.RemoveField(
            model_name='sig',
            name='sigContent',
        ),
        migrations.AddField(
            model_name='sig',
            name='image',
            field=models.ImageField(null=True, upload_to='uploads/sigs/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='sig',
            name='members',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='web.Designation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sig',
            name='sig_description',
            field=models.TextField(null=True, verbose_name='Sig Description'),
        ),
        migrations.AddField(
            model_name='sig',
            name='timings',
            field=models.CharField(max_length=50, null=True, verbose_name='Timings of SIG'),
        ),
        migrations.AddField(
            model_name='sigmentor',
            name='sig',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Sig'),
        ),
    ]
