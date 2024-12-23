from django.urls import path
from PostsVault import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name = 'home'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('blog/create/', views.add_post, name = 'createPost'),
    path('blog/search/', views.search_post, name="search-results"),
    path('blog/<slug:slug>/', views.viewPost, name = "viewPost"),
    path('about-us/', views.about_us, name = 'about-us'),
    path('contact-us/', views.contact_us, name = 'contact-us'),
    path('signup/', views.user_registration, name = 'signup'),
    path('login/', views.user_login, name = 'login'),
    path('logout/', views.user_logout, name = 'logout'),
    # path('change-password/', views.user_changePassword, name = "changePassword"),
    path('blog/edit/<int:id>/', views.edit_post, name = 'edit'),
    path('blog/delete/<slug:slug>/', views.delete_post, name = 'delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)