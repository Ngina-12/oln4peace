from django.db import migrations

def create_superuser(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin1',
            email='georgiamendez64@gmail.com',
            password='onesheeptwo'
        )

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_chapter_options_remove_galleryphoto_date_and_more.py'),  # <-- replace with your last migration file name
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]