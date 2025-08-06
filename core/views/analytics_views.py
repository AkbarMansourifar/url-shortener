from django.db.models import Count
from datetime import timedelta, datetime, time
from ..models import Visit, URL
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from django.utils.timezone import now


class AnalyticsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, short_url):
        url_obj = get_object_or_404(URL, short_url=short_url)

        range_param = request.query_params.get("range", "7d")
        now_time = now()

        time_ranges = {
            "today": datetime.combine(now_time.date(), time.min),
            "24h": now_time - timedelta(hours=24),
            "7d": now_time - timedelta(days=7),
            "30d": now_time - timedelta(days=30),
        }

        start_time = time_ranges.get(range_param, time_ranges["7d"])
        qs = Visit.objects.filter(url=url_obj, timestamp__gte=start_time)

        return Response({
            "total_views": qs.count(),
            "unique_users": qs.values("ip_address").distinct().count(),
            "by_device": dict(qs.values("device_type").annotate(count=Count("id")).values_list("device_type", "count")),
            "by_browser": dict(qs.values("browser").annotate(count=Count("id")).values_list("browser", "count")),
        })