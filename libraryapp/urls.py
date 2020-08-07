from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = "libraryapp"

urlpatterns = [
    path('', home, name='home'),
    path('books/', book_list, name='books'),
    path('books/<int:book_id>/', book_details, name='book'),
    path('books/<int:book_id>/form/', book_edit_form, name='book_edit_form'),
    path('librarians/', librarian_list, name='librarians'),
    path('librarians/<int:librarian_id>/', librarian_details, name='librarian'),
    path('libraries/', library_list, name='libraries'),
    path('libraries/<int:library_id>/', library_details, name='library'),
    path('library/form/', library_form, name='library_form'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('book/form/', book_form, name='book_form'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
