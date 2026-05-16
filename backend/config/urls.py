from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path


def health(request):
    return JsonResponse({"status": "ok", "service": "ai_assistant_backend"})


urlpatterns = [
    path("", health),
    path("api/health/", health),
    path("admin/", admin.site.urls),
    path("api/auth/", include("accounts.urls")),
    path("api/email/", include("email_app.urls")),
    path("api/tasks/", include("tasks.urls")),
    path("api/notifications/", include("notifications_app.urls")),
    path("api/reminders/", include("reminders.urls")),
    path("api/calendar/", include("calendar_app.urls")),
    path("api/automation/", include("automation.urls")),
    path("api/files/", include("files_app.urls")),
    path("api/memory/", include("memory.urls")),
    path("api/ai/", include("ai_services.urls")),
    path("api-auth/", include("rest_framework.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
