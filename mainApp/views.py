from django.shortcuts import render
from .forms import CreateVendorForm
from rest_framework import generics
from .models import VendorModel
from .serializers import VendorSerializer
import json


class VendorListView(generics.ListAPIView):
    queryset = VendorModel.objects.all()
    serializer_class = VendorSerializer

class VendorRetrieveView(generics.RetrieveAPIView):
    queryset = VendorModel.objects.all()
    serializer_class = VendorSerializer


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