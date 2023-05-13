# Generated by Django 3.2.18 on 2023-05-13 14:15

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields
import posts.models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0005_auto_20220424_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('category', models.CharField(choices=[('오지, 노지', '오지, 노지'), ('유료', '유료'), ('글램핑, 카라반', '글램핑, 카라반')], max_length=10)),
                ('city', models.CharField(max_length=10)),
                ('nature', models.CharField(choices=[('계곡', '계곡'), ('바다', '바다'), ('산', '산'), ('강변', '강변'), ('호수', '호수')], max_length=10)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=14, validators=[django.core.validators.RegexValidator(regex='^0[1-9]\\d{0,2}-\\d{3,4}-\\d{4}$')])),
                ('open_hour', models.TimeField()),
                ('close_hour', models.TimeField()),
                ('rating', models.DecimalField(decimal_places=1, default=0, max_digits=5)),
                ('like_users', models.ManyToManyField(related_name='like_posts', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('visit_users', models.ManyToManyField(related_name='visit_posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=posts.models.PostImage.post_image_path)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
            ],
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facility', models.CharField(choices=[('와이파이', '와이파이'), ('매점', '매점'), ('샤워시설', '샤워시설'), ('전기', '전기'), ('온수제공', '온수제공'), ('대여', '대여'), ('장작', '장작'), ('개수대', '개수대'), ('화장실', '화장실')], max_length=10)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
            ],
        ),
    ]
