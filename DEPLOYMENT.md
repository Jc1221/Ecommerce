# Deployment Instructions

## Production Settings

Before deploying to production, make these changes:

### 1. Security Settings (ecommerce/settings.py)

```python
# Change DEBUG to False
DEBUG = False

# Add your domain to ALLOWED_HOSTS
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# Use environment variables for sensitive data
import os
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key')

# Database configuration for production
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}
```

### 2. Static Files Configuration

```python
# Static files for production
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
```

### 3. Media Files

Configure media file serving for production:
- Use cloud storage (AWS S3, Google Cloud Storage)
- Or configure web server (Nginx) to serve media files

### 4. Requirements for Production

```bash
pip install gunicorn
pip install psycopg2-binary  # for PostgreSQL
pip install whitenoise       # for static file serving
```

### 5. Environment Variables

Create a `.env` file (not included in git):
```
SECRET_KEY=your-super-secret-key
DEBUG=False
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432
```

### 6. Run Production Server

```bash
# Collect static files
python manage.py collectstatic --noinput

# Run with Gunicorn
gunicorn ecommerce.wsgi:application --bind 0.0.0.0:8000
```

## Nginx Configuration Example

```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location /static/ {
        alias /path/to/your/project/staticfiles/;
    }

    location /media/ {
        alias /path/to/your/project/media/;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```