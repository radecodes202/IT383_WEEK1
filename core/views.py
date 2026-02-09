from django.shortcuts import render
from django.db.models import Sum, Avg, Count, F, Q
from core.models import *

# Create your views here.

def dashboard_view(request):
    stats = Project.objects.aggregate(
        total_budget=Sum('budget'),
        avg_budget=Avg('budget'),
        project_count=Count('id'),
    )

    recent_assets = Asset.select_related('assigned_to').all()[:5]

    context = {
        'stats': stats,
        'recent_assets': recent_assets,
    }

    return render(request, 'core/dashboard.html', context)


