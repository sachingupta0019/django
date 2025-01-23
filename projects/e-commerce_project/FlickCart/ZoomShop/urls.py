from django.urls import path
from ZoomShop import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import UserLoginForm, UserPasswordChangeForm

urlpatterns = [
    path('', views.ProductView.as_view()),
    path('product-detail/<int:id>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('mobile/', views.MobileView.as_view(), name='mobile'),
    path('mobile/<slug:slug>', views.MobileView.as_view(), name='mobile_page'),
    path('clothes/', views.ClothWearView.as_view(), name='clothes'),
    path('clothes/<slug:slug>', views.ClothWearView.as_view(), name='clothes_page'),
    path('registration/', views.UserRegistrationFormView.as_view(), name='customerregistration'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='customer/login.html', authentication_form=UserLoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('password-change/', auth_views.PasswordChangeView.as_view(template_name='customer/changepassword.html', form_class=UserPasswordChangeForm, success_url='/password-change-done/'), name='change-password'),
    path('password-change-done/', auth_views.PasswordChangeDoneView.as_view(template_name='customer/changepassworddone.html')),
    path('checkout/', views.checkout, name='checkout'),

] + static(settings.MEDIA_URL,  document_root = settings.MEDIA_ROOT)