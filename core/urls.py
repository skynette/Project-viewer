from django.urls import path
from . import views

urlpatterns = [

	path('payments/', views.initiate_payment, name="initiate-payment"),
	path('payments/<str:ref>/', views.verify_payment, name="verify-payment"),
]
