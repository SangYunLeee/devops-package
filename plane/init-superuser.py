#!/usr/bin/env python
import os
from django.contrib.auth import get_user_model
from plane.license.models import Instance, InstanceConfiguration

# Create superuser
User = get_user_model()
email = os.environ.get('ADMIN_EMAIL', 'admin@plane.local')
password = os.environ.get('ADMIN_PASSWORD', 'admin123')

if not User.objects.filter(email=email).exists():
    u = User.objects.create_superuser(email=email, username='admin', password=password)
    u.is_email_verified = True
    u.save()
    print(f'Superuser {email} created')
else:
    print(f'Superuser {email} already exists')

# Configure instance
instance = Instance.objects.first()
if instance and not instance.is_setup_done:
    instance.is_setup_done = True
    instance.save()
    print('Instance setup marked as done')

# Create instance configurations
configs = [
    ('IS_SELF_MANAGED', 'true'),
    ('ENABLE_SIGNUP', os.environ.get('ENABLE_SIGNUP', 'true')),
    ('ENABLE_EMAIL_PASSWORD', os.environ.get('ENABLE_EMAIL_PASSWORD', 'true')),
    ('ENABLE_MAGIC_LINK_LOGIN', os.environ.get('ENABLE_MAGIC_LINK_LOGIN', 'false')),
    # Disable external services for air-gapped environment
    ('INTERCOM_APP_ID', ''),
    ('ENABLE_INTERCOM', 'false'),
    ('UNSPLASH_ACCESS_KEY', ''),
]

for key, value in configs:
    conf, created = InstanceConfiguration.objects.update_or_create(
        key=key,
        defaults={'value': value}
    )
    action = 'created' if created else 'updated'
    print(f'Config {key}={value} ({action})')
