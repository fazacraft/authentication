from django.urls import path

from authentication.views import UserViewSet, UserLoginViewSet
from payment.views import PaymeViewSet

urlpatterns = [
    path('payment/payme/', PaymeViewSet.as_view({'post': 'post'}), name='payment'),

]
