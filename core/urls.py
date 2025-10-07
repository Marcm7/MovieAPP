from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),  # won't be used for CRUD
    path('', RedirectView.as_view(url='/videos/', permanent=False)),
    path('videos/', include('videos.urls')),
]
