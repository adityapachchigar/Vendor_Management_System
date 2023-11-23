from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home),
    # path('create',views.CreateVendor),
    # path('api/vendors/', views.VendorCreateView.as_view()),
    path('api/vendors/', views.VendorCreateListView.as_view()),
    path('api/vendors/<str:pk>/', views.VendorRetrieveUpdateDeleteView.as_view()),
    path('api/vendors/<str:pk>/performance/', views.VendorPerformanceListView.as_view()),
    # path('api/vendors/<str:pk>/', views.VendorUpdateView.as_view()),
    path('api/purchase_orders/', views.PurchaseOrderCreateListView.as_view()),
    path('api/purchase_orders/<str:pk>/', views.PurchaseOrderRetrieveUpdateDeleteView.as_view()),
    
]
