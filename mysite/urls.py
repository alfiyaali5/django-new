from django.contrib import admin
from django.urls import path
from myapp import views
from . import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/',views.book,name='book'),
    path('main/',views.main,name='main'),
    path('book/detail/<int:id>',views.detail,name='detail'),
    path('add_newbook/',views.add_newbook,name='add_newbook'),
    path('book/detail/update/<int:id>',views.update,name="update"),
    path('book/detail/delete/<int:id>',views.delete,name="delete"),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

