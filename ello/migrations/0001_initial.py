# Generated by Django 4.0.4 on 2022-10-19 05:40

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Hotal',
            fields=[
                ('Hotal_id', models.AutoField(primary_key=True, serialize=False)),
                ('Hotal_Name', models.CharField(max_length=50)),
                ('hotal_new_price', models.CharField(default='', max_length=255)),
                ('hotal_new_price_premium', models.CharField(default='', max_length=255)),
                ('hotal_discreption', models.TextField(max_length=500)),
                ('Hotal_Location', models.CharField(max_length=200)),
                ('Hotal_Latitude', models.FloatField()),
                ('Hotal_Longitude', models.FloatField()),
                ('Hotal_images1', models.ImageField(blank=True, null=True, upload_to='hotalmedia')),
                ('garden_images1', models.ImageField(blank=True, null=True, upload_to='hotalmedia')),
                ('garden_images2', models.ImageField(blank=True, null=True, upload_to='hotalmedia')),
                ('garden_images3', models.ImageField(blank=True, null=True, upload_to='hotalmedia')),
                ('garden_images4', models.ImageField(blank=True, null=True, upload_to='hotalmedia')),
                ('garden_images5', models.ImageField(blank=True, null=True, upload_to='hotalmedia')),
                ('reception_images1', models.ImageField(blank=True, null=True, upload_to='hotalmedia')),
                ('reception_images2', models.ImageField(blank=True, null=True, upload_to='hotalmedia')),
                ('reception_images3', models.ImageField(blank=True, null=True, upload_to='hotalmedia')),
                ('reception_images4', models.ImageField(blank=True, null=True, upload_to='hotalmedia')),
                ('reception_images5', models.ImageField(blank=True, null=True, upload_to='hotalmedia')),
                ('bedroom_images1', models.ImageField(blank=True, null=True, upload_to='hotalmedia')),
                ('bedroom_images2', models.ImageField(blank=True, null=True, upload_to='hotalmedia')),
                ('bedroom_images3', models.ImageField(blank=True, null=True, upload_to='hotalmedia')),
                ('bedroom_images4', models.ImageField(blank=True, null=True, upload_to='hotalmedia')),
                ('bedroom_images5', models.ImageField(blank=True, null=True, upload_to='hotalmedia')),
                ('washroom_images1', models.ImageField(blank=True, null=True, upload_to='hotalmedia')),
                ('washroom_images2', models.ImageField(blank=True, null=True, upload_to='hotalmedia')),
                ('washroom_images3', models.ImageField(blank=True, null=True, upload_to='hotalmedia')),
                ('washroom_images4', models.ImageField(blank=True, null=True, upload_to='hotalmedia')),
                ('washroom_images5', models.ImageField(blank=True, null=True, upload_to='hotalmedia')),
                ('Exterior_images1', models.ImageField(blank=True, null=True, upload_to='hotalmedia')),
                ('Exterior_images2', models.ImageField(blank=True, null=True, upload_to='hotalmedia')),
                ('Exterior_images3', models.ImageField(blank=True, null=True, upload_to='hotalmedia')),
                ('Exterior_images4', models.ImageField(blank=True, null=True, upload_to='hotalmedia')),
                ('Exterior_images5', models.ImageField(blank=True, null=True, upload_to='hotalmedia')),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('hotal_ratting', models.ImageField(default=0, upload_to='')),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='exclusive_partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exclusive_partners_images1', models.ImageField(blank=True, null=True, upload_to='exclusive_partners')),
                ('exclusive_partners_images2', models.ImageField(blank=True, null=True, upload_to='exclusive_partners')),
                ('exclusive_partners_images3', models.ImageField(blank=True, null=True, upload_to='exclusive_partners')),
                ('exclusive_partners_images4', models.ImageField(blank=True, null=True, upload_to='exclusive_partners')),
                ('exclusive_partners_Details', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Holiday_packages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Holiday_packages_images1', models.ImageField(blank=True, null=True, upload_to='Holiday_packages')),
                ('Holiday_packages_images2', models.ImageField(blank=True, null=True, upload_to='Holiday_packages')),
                ('Holiday_packages_images3', models.ImageField(blank=True, null=True, upload_to='Holiday_packages')),
                ('Holiday_packages_images4', models.ImageField(blank=True, null=True, upload_to='Holiday_packages')),
                ('Holiday_packages_Details', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='offer_for_you',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_for_you_pic', models.ImageField(blank=True, null=True, upload_to='offer_for_you')),
                ('first_time_book', models.CharField(blank=True, max_length=255)),
                ('coupon_code', models.CharField(blank=True, max_length=255)),
                ('offer_Details', models.CharField(blank=True, max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='promotions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=255)),
                ('promotions_Details', models.CharField(max_length=255)),
                ('promotions_images1', models.ImageField(blank=True, null=True, upload_to='promotion')),
                ('promotions_images2', models.ImageField(blank=True, null=True, upload_to='promotion')),
                ('promotions_images3', models.ImageField(blank=True, null=True, upload_to='promotion')),
                ('promotions_images4', models.ImageField(blank=True, null=True, upload_to='promotion')),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='whats_new',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('whats_new_images1', models.ImageField(blank=True, null=True, upload_to='whats_new')),
                ('whats_new_images2', models.ImageField(blank=True, null=True, upload_to='whats_new')),
                ('whats_new_images3', models.ImageField(blank=True, null=True, upload_to='whats_new')),
                ('whats_new_images4', models.ImageField(blank=True, null=True, upload_to='whats_new')),
                ('whats_new_details', models.CharField(blank=True, max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='youtube_video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=255)),
                ('location', models.CharField(blank=True, max_length=255)),
                ('link', models.CharField(blank=True, max_length=255)),
                ('youtube_video_Details', models.CharField(blank=True, max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_pastudent', models.BooleanField(default=False)),
                ('phone', models.IntegerField(default=0)),
                ('address', models.TextField(max_length=120)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
