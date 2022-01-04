from modules.first.views import hello_world, hi
from django.contrib import admin
from django.urls import path
from modules.Users import views as users_view
from modules.posts import views as post_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello_world', hello_world),
    path('hi/<str:name>/<int:age>', hi),

    path('posts/', post_view.list_posts, name="feed"),
    path('users/login/', users_view.login_view, name="login"),
    path('users/logout/', users_view.logout_view, name="logout"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
