from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chaithu_app.urls', namespace='chaithu_app')),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chaithu_app.urls', namespace='chaithu_app')),  # 👈 Correct usage with namespace
]
