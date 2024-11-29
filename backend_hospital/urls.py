from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app_base.urls')),
    path('',include('reseña_app.urls')),
    path('',include('proveedor_app.urls')),
    path('',include('promocion_app.urls')),
    path('',include('producto_app.urls')),
    path('',include('pedido_app.urls')),
    
    
]
