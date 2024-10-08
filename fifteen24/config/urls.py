from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='user/login/')),
    path('user/', include('user.urls')),
    path('fifteen/', include('fifteen.urls')),
    path('admin/', admin.site.urls),
]
