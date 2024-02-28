from django.urls import path, include
from core.api import quiz_list_api, quiz_detail_api


urlpatterns = [
    path('quiz/api/', include([
        path('list/', quiz_list_api),
        path('detail/<int:pk>/', quiz_detail_api)
    ])),
]