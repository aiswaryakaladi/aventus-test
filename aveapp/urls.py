from django.urls import path
from .views import *

urlpatterns=[
    path('fileupload/',fileupload),
    path('filedisplay/',filedisplay),
    path('edit1/<int:id>',editfile),
    path('delete1/<int:id>',deletefile),
]