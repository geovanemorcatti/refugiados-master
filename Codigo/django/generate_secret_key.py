"""
  This script is used to generate a fresh secret_key for django. Please remember to keep your secret key used in production... Well, secret!
  To read more: https://docs.djangoproject.com/en/3.1/ref/settings/#std:setting-SECRET_KEY
"""
import secrets

length = 50
chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'

secret_key = ''.join(secrets.choice(chars) for i in range(length))

print('This is your new secret key. KEEP IT SAFE:')
print(secret_key)