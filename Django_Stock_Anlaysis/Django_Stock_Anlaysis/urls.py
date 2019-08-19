
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Stock Analysis API",
      default_version='v1',
      description="These apis are used for stock analysis and django practice",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="nandha.paramasivam@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

app_urls = [
    path('admin/', admin.site.urls),
    path('api/v1/',include(('stocks_detail_api.urls', 'stocks_detail_api'), namespace='stocks_detail_api' )),
    path('',include(('stocks_detail_fe.urls', 'stocks_detail_fe'), namespace='stocks_detail_fe' )),

]

swagger_urls = [
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

urlpatterns = app_urls + swagger_urls
