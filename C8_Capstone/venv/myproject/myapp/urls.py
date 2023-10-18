# define URL route for index() view
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from django.views.generic import TemplateView


# class IndexView(TemplateView):
# template_name = 'index.html'


urlpatterns = [
    # path('', views.index, name='index'),
    path('', TemplateView.as_view(
        template_name='index.html'), name='index'),
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token)
]
