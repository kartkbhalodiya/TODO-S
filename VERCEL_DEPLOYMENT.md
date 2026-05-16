# Vercel Backend Deployment

This repo root is a Flutter app, so Vercel is configured to deploy only the Django backend.

## Files Used By Vercel

- `vercel.json` routes every request to `api/index.py`.
- `api/index.py` loads `backend/config/settings.py` and exposes the WSGI app.
- `requirements.txt` installs `backend/requirements.txt`.
- `.vercelignore` keeps Flutter build/mobile folders out of the deployment upload.
- `.env.vercel.example` lists the Vercel environment variables.

## Required Vercel Environment Variables

Set these in Vercel Project Settings > Environment Variables:

```text
DJANGO_SECRET_KEY
DJANGO_DEBUG=False
DATABASE_URL
DATABASE_SSL_REQUIRE=True
DJANGO_ALLOWED_HOSTS=.vercel.app,your-project-name.vercel.app
DJANGO_CSRF_TRUSTED_ORIGINS=https://your-project-name.vercel.app
GOOGLE_OAUTH_CLIENT_ID=782174705998-7l0035suockngjdvbhbue651sv6cemll.apps.googleusercontent.com
GEMINI_API_KEY
```

Optional:

```text
GEMINI_TEXT_MODEL=gemini-2.5-flash
GEMINI_LIVE_AUDIO_MODEL=gemini-2.5-flash-native-audio-preview-12-2025
CORS_ALLOW_ALL_ORIGINS=False
CORS_ALLOWED_ORIGINS=
```

## Database

Vercel serverless storage is not a persistent database. Use external Postgres:

- Neon
- Supabase
- Railway
- Vercel Postgres/Marketplace database

After setting `DATABASE_URL`, run migrations against that database:

```powershell
$env:DATABASE_URL="postgresql://USER:PASSWORD@HOST:5432/DBNAME?sslmode=require"
$env:DJANGO_DEBUG="False"
python backend\manage.py migrate
```

## Deploy

From the repo root:

```powershell
vercel
vercel --prod
```

Health check after deploy:

```text
https://your-project-name.vercel.app/api/health/
```

Use this as the app backend URL:

```text
https://your-project-name.vercel.app/api
```

## Known Limit

File uploads saved to `MEDIA_ROOT` are not persistent on Vercel functions. For real file storage, add S3, Cloudinary, or Vercel Blob later.
