from django.shortcuts import render
from .forms import CreateVendorForm
from rest_framework import generics
from rest_framework.response import Response
from .models import VendorModel,PurchaseOrderModel, HistoricalPerformanceModel
from .serializers import VendorSerializer, PurchaseOrderSerializer, VendorPerformanceSerializer
import json

# class VendorCreateView(generics.CreateAPIView):
#     queryset = VendorModel.objects.all()
#     serializer_class = VendorSerializer

class VendorCreateListView(generics.ListCreateAPIView):
    queryset = VendorModel.objects.all()
    serializer_class = VendorSerializer

class VendorRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VendorModel.objects.all()
    serializer_class = VendorSerializer

class PurchaseOrderCreateListView(generics.ListCreateAPIView):
    # queryset = PurchaseOrderModel.objects.all()
    serializer_class = PurchaseOrderSerializer
    
    def get_queryset(self):
        queryset = PurchaseOrderModel.objects.all()
        vendor_code = self.request.query_params.get('vendor', None)
        if vendor_code is not None:
            queryset = queryset.filter(vendor_code=vendor_code)

        return queryset
    
class PurchaseOrderRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrderModel.objects.all()
    serializer_class = PurchaseOrderSerializer
    
class VendorPerformanceListView(generics.ListAPIView):
    queryset = VendorModel.objects.all()
    serializer_class = VendorPerformanceSerializer
    
# class VendorUpdateView(generics.UpdateAPIView):
#     queryset = VendorModel.objects.all()
#     serializer_class = VendorSerializer


def home(request):
    return render(request, 'home.html')

def CreateVendor(request):
    if request.method == "POST":
        f = CreateVendorForm(request.POST)
        if f.is_valid():
            f.save()
            return render(request,"home.html")
    f1 = CreateVendorForm()
    context = {'form':f1}
    return render(request,"create_vendor.html",context)