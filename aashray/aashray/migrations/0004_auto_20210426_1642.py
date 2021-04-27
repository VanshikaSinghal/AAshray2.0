# Generated by Django 3.1.5 on 2021-04-26 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aashray', '0003_plasmadonorform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(blank=True, max_length=255)),
                ('address', models.TextField(blank=True, max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('VerificationTime', models.DateTimeField(blank=True)),
                ('verified', models.BooleanField(default=False)),
                ('currDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Helpline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=13, unique=True)),
                ('currDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('medicine', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(blank=True, max_length=255)),
                ('address', models.TextField(blank=True, max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('verificationTime', models.DateTimeField(blank=True)),
                ('verified', models.BooleanField(default=False)),
                ('currDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Other',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('image', models.ImageField(default='', upload_to='media/Others/')),
                ('currDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Oxygen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(blank=True, max_length=255)),
                ('address', models.TextField(blank=True, max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('VerificationTime', models.DateTimeField(blank=True)),
                ('verified', models.BooleanField(default=False)),
                ('currDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plasma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bloodGroup', models.CharField(blank=True, choices=[('A+', 'A+'), ('B+', 'B+'), ('AB+', 'AB+'), ('O+', 'O+'), ('A-', 'A-'), ('B-', 'B-'), ('AB-', 'AB-'), ('O-', 'O-')], max_length=3)),
                ('contact', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(blank=True, max_length=255)),
                ('address', models.TextField(blank=True, max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('VerificationTime', models.DateTimeField(blank=True)),
                ('verified', models.BooleanField(default=False)),
                ('currDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='plasmadonorform',
            name='medIssues',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]