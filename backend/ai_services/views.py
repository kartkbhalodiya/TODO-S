import json
import urllib.error
import urllib.request

from django.conf import settings
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView


class BaseAIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def _gemini_response(self, prompt):
        api_key = getattr(settings, "GEMINI_API_KEY", "")
        if not api_key:
            return None, Response(
                {"error": "Gemini API key is not configured on the backend."},
                status=status.HTTP_503_SERVICE_UNAVAILABLE,
            )

        model = getattr(settings, "GEMINI_TEXT_MODEL", "gemini-2.5-flash")
        url = (
            "https://generativelanguage.googleapis.com/v1beta/models/"
            f"{model}:generateContent?key={api_key}"
        )
        payload = {
            "contents": [
                {
                    "role": "user",
                    "parts": [{"text": prompt}],
                }
            ],
            "generationConfig": {
                "temperature": 0.7,
                "topP": 0.95,
                "maxOutputTokens": 512,
            },
        }
        request = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )

        try:
            with urllib.request.urlopen(request, timeout=25) as response:
                data = json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            return None, Response(
                {"error": "Gemini request failed.", "status_code": exc.code},
                status=status.HTTP_502_BAD_GATEWAY,
            )
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
            return None, Response(
                {"error": "Gemini service is unavailable."},
                status=status.HTTP_502_BAD_GATEWAY,
            )

        candidates = data.get("candidates") or []
        if not candidates:
            return None, Response(
                {"error": "Gemini returned no candidates."},
                status=status.HTTP_502_BAD_GATEWAY,
            )

        parts = candidates[0].get("content", {}).get("parts") or []
        text = "".join(part.get("text", "") for part in parts).strip()
        if not text:
            return None, Response(
                {"error": "Gemini returned an empty response."},
                status=status.HTTP_502_BAD_GATEWAY,
            )
        return text, None


class AnalyzeEmailView(BaseAIView):
    def post(self, request):
        body = request.data.get("body", "")
        result, error = self._gemini_response(
            f"Analyze this email and provide a brief summary:\n{body}"
        )
        if error:
            return error
        return Response({"summary": result})


class GenerateReplyView(BaseAIView):
    def post(self, request):
        email_body = request.data.get("email_body", "")
        tone = request.data.get("tone", "Professional")
        result, error = self._gemini_response(
            f"Generate a {tone} reply for this email:\n{email_body}"
        )
        if error:
            return error
        return Response({"reply": result})


class SummarizeNotificationsView(BaseAIView):
    def post(self, request):
        notifications = request.data.get("notifications", [])
        text = ". ".join(
            f"{item.get('app', '')}: {item.get('title', '')} - {item.get('body', '')}"
            for item in notifications
        )
        result, error = self._gemini_response(
            f"Summarize these notifications concisely:\n{text}"
        )
        if error:
            return error
        return Response({"summary": result})


class DailyBriefingView(BaseAIView):
    def post(self, request):
        result, error = self._gemini_response(
            "Generate a concise morning briefing from this real app context:\n"
            f"{json.dumps(request.data)}"
        )
        if error:
            return error
        return Response({"briefing": result})


class ChatView(BaseAIView):
    def post(self, request):
        message = request.data.get("message", "")
        context = request.data.get("context", "")
        prompt = f"Context: {context}\n\nUser: {message}" if context else message
        result, error = self._gemini_response(
            "You are Nova, a Gemini-powered Android personal assistant. "
            "Answer briefly and do not claim device actions are complete unless "
            "the app reports success.\n\n"
            f"{prompt}"
        )
        if error:
            return error
        return Response({"response": result})


class DetectFraudView(BaseAIView):
    def post(self, request):
        content = request.data.get("content", "")
        result, error = self._gemini_response(
            "Analyze this content for phishing or fraud indicators. "
            f"Return WARNING or SAFE with a short reason:\n{content}"
        )
        if error:
            return error
        return Response({"result": result})
