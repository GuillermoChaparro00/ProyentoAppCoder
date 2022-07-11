
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("app_coder.urls")),
    path("app_coder/", include("app_coder.urls"))
]
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)