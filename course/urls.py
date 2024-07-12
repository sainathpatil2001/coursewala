from django.contrib import admin

from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', include('login.urls')),  # Adjust based on your home app
    path('admin/', admin.site.urls),
    path('accounts/', include('login.urls')),
    path('student/', include(('student.urls', 'student'))),
    path('teacher/', include(('teacher.urls', 'teacher'))),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
