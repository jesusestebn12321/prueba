from django.urls import path
from core.views import *
app_name='core'
urlpatterns = [
    path('book', BookAPIView.as_view()),
    path('book/<int:pk>', BookAPIView.as_view()), # to capture our ids
	path('comments', CommentAPIView.as_view()),
    path('comments/<int:pk>', CommentAPIView.as_view()) # to capture our ids
]
