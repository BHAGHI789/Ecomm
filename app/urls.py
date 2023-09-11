from django.urls import path
from app.views import *
from django.conf import settings
from django.conf.urls.static import static
from .forms import LoginForm
from django.contrib.auth import views as auth_view
urlpatterns = [
    path("",home,name="home"),
    path("about",about,name="about"),
    path("contact",contact,name="contact"),
    path("category/<slug:val>/",CategoryView.as_view(),name="category"),
    path("category-title/<str:val>/",CategoryTitle.as_view(),name="category-title"),
    path("product-detail/<int:pk>/",ProductDetail.as_view(),name="product-detail"),
    path("profile",ProfileView.as_view(),name="profile"),
    path("address",Address,name="address"),
    path("updateaddress/<int:pk>/",Updateaddress.as_view(),name="updateaddress"),
    
    
    #authenticstion
    path("customer-Registation",CustomerRegistatinView.as_view(),name="customer-Registation"),
    path("login",auth_view.LoginView.as_view(template_name="login.html",authentication_form=LoginForm),name="login"),
    path("logout",auth_view.LogoutView.as_view(next_page='login'),name="logout"),
    
    
    
    path("passwordchange",auth_view.PasswordChangeView.as_view(template_name="passwordchange.html",form_class=MypasswordChangeForm,success_url='/passwordchangedone'),name="passwordchange"),
    path("passwordchangedone",auth_view.PasswordChangeDoneView.as_view(template_name="passwordchangedone.html"),name="passwordchangedone"),
    
    
path('password-reset/',auth_view.PasswordResetView.as_view(template_name='password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),
path('password-reset/done/',auth_view.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
path('password-reset-confirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html',form_class=MySetPasswordForm),name='password_reset_confirm'),
path('password-reset-complete/',auth_view.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
 
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

"""
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html',form_class=MySetPasswordForm),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'),name='password_reset_complete'),
"""