from django.urls import path
from . import views

urlpatterns = [
    path('analyze-email/', views.AnalyzeEmailView.as_view(), name='analyze-email'),
    path('generate-reply/', views.GenerateReplyView.as_view(), name='generate-reply'),
    path('summarize-notifications/', views.SummarizeNotificationsView.as_view(), name='summarize-notifications'),
    path('daily-briefing/', views.DailyBriefingView.as_view(), name='daily-briefing'),
    path('chat/', views.ChatView.as_view(), name='chat'),
    path('detect-fraud/', views.DetectFraudView.as_view(), name='detect-fraud'),
]
