from django.contrib import admin
# Start 
from django.conf import settings
from django.conf.urls.static import static
# End 
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('apis.urls')),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

