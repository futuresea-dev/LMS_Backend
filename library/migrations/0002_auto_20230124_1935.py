# Generated by Django 3.1.5 on 2023-01-25 03:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmodel',
            name='amount',
        ),
        migrations.AddField(
            model_name='authormodel',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='authormodel',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='authormodel_createdby', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='authormodel',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='authormodel',
            name='deleted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='authormodel_deletedby', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='authormodel',
            name='is_test_data',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='authormodel',
            name='modified_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='authormodel',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='authormodel_modifiedby', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='ISBN',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookmodel_createdby', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='deleted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookmodel_deletedby', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='is_test_data',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='modified_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookmodel_modifiedby', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='pages',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='store_amount',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='categorymodel',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='categorymodel',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categorymodel_createdby', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='categorymodel',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='categorymodel',
            name='deleted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categorymodel_deletedby', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='categorymodel',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='categorymodel',
            name='is_test_data',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='categorymodel',
            name='modified_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='categorymodel',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categorymodel_modifiedby', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='favoritesmodel',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='favoritesmodel',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='favoritesmodel_createdby', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='favoritesmodel',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='favoritesmodel',
            name='deleted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='favoritesmodel_deletedby', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='favoritesmodel',
            name='is_test_data',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='favoritesmodel',
            name='modified_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='favoritesmodel',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='favoritesmodel_modifiedby', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='publishermodel',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='publishermodel',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='publishermodel_createdby', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='publishermodel',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publishermodel',
            name='deleted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='publishermodel_deletedby', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='publishermodel',
            name='descripton',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publishermodel',
            name='is_test_data',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='publishermodel',
            name='modified_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publishermodel',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='publishermodel_modifiedby', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='authormodel',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='authormodel',
            name='author_image',
            field=models.ImageField(default='placeholder_author.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='authormodel',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='authormodel',
            name='death_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.authormodel'),
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='book_cover',
            field=models.ImageField(default='placeholder_cover.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.categorymodel'),
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='published_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bookmodel',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.publishermodel'),
        ),
        migrations.AlterField(
            model_name='favoritesmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]