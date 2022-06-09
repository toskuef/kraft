from django.contrib import admin
from django.urls import path, include

from kraft import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crm/', include('crm.urls', namespace='crm')),
    path('auth/', include('users.urls', namespace='users')),
    path('auth/', include('django.contrib.auth.urls')),
    path('production/', include('production.urls', namespace='production')),
    path('supply/', include('supply.urls', namespace='supply')),
    path('drag/', include('drag.urls')),
    path('', include('chat.urls')),
    # path('', include('main.urls', namespace='main')),


]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
