from django.shortcuts import render
from .forms import CreateVendorForm,AllThree
from rest_framework import generics
from rest_framework.response import Response
from .models import VendorModel,PurchaseOrderModel, HistoricalPerformanceModel
from .serializers import VendorSerializer, PurchaseOrderSerializer, VendorPerformanceSerializer
import json
from rest_framework.views import APIView
from django.db import connection
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

def three(request):
    return render(request,"all_three.html")
        
    

class RetrieveVendorView(APIView):
    def get(self, request, pachi):
        vendors = VendorModel.objects.filter(vendor_code=pachi)
        serializer = VendorSerializer(vendors, many=True)
        return Response({"vendors": serializer.data})
    
    def put(self, request, pachi):
        saved_article = get_object_or_404(VendorModel.objects.all(), pk=pachi)
        vendors = {
            "vendor_code": request.data.get('vendor_code'),
            "name": request.data.get('name'),
            "contact_details": request.data.get('contact_details'),
            "address": request.data.get('address'),
            # "on_time_delivery_rate": request.data.get('on_time_delivery_rate'),
            # "quality_rating_avg": request.data.get('quality_rating_avg'),
            # "average_response_time": request.data.get('average_response_time'),
            # "fulfillment_rate":request.data.get('fulfillment_rate')
        }
        serializer = VendorSerializer(instance=saved_article, data=vendors, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "{}".format(vendors)})

    def delete(self, request, pachi):
        article = get_object_or_404(VendorModel.objects.all(), pk=pachi)
        article.delete()
        return Response({"message": "Article with id `{}` has been deleted.".format(pachi)},status=204)


class GetVendorView(APIView):
    def get(self, request):
        vendors = VendorModel.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = VendorSerializer(vendors, many=True)
        return Response({"vendors": serializer.data})
    
    def post(self, request):
        # d={"name":"adi"}
        vendors = {
            "vendor_code": request.data.get('vendor_code'),
            "name": request.data.get('name'),
            "contact_details": request.data.get('contact_details'),
            "address": request.data.get('address'),
            # "on_time_delivery_rate": request.data.get('on_time_delivery_rate'),
            # "quality_rating_avg": request.data.get('quality_rating_avg'),
            # "average_response_time": request.data.get('average_response_time'),
            # "fulfillment_rate":request.data.get('fulfillment_rate')
        }
        serializer = VendorSerializer(data=vendors)
        if serializer.is_valid(raise_exception=True):
            vendor_saved = serializer.save()
        # return HttpResponse("hello")
        return Response({"success": "{}".format(vendors)})




class GetPurchaseOrderView(APIView):
    def get(self, request):
        pos = PurchaseOrderModel.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = PurchaseOrderSerializer(pos, many=True)
        return Response({"purchase_orders": serializer.data})
    
    def post(self, request):
        # d={"name":"adi"}
        pos = {
            "po_number": request.data.get('po_number'),
            "order_date": request.data.get('order_date'),
            "delivery_date": request.data.get('delivery_date'),
            "items": request.data.get('items'),
            "quantity": request.data.get('quantity'),
            "status": request.data.get('status'),
            "quality_rating": request.data.get('quality_rating'),
            "issue_date": request.data.get('issue_date'),
            "acknowledgment_date": request.data.get('acknowledgment_date'),
            "vendor_code": request.data.get('vendor_code')
        }
        serializer = PurchaseOrderSerializer(data=pos)
        if serializer.is_valid(raise_exception=True):
            vendor_saved = serializer.save()
        # return HttpResponse("hello")
        return Response({"success": "{}".format(pos)})

class RetrievePurchaseView(APIView):
    def get(self, request, pachi):
        pos = PurchaseOrderModel.objects.filter(po_number=pachi)
        serializer = PurchaseOrderSerializer(pos, many=True)
        return Response({"purchase_orders": serializer.data})
    
    def put(self, request, pachi):
        saved_article = get_object_or_404(PurchaseOrderModel.objects.all(), pk=pachi)
        pos = {
            "po_number": request.data.get('po_number'),
            "order_date": request.data.get('order_date'),
            "delivery_date": request.data.get('delivery_date'),
            "items": request.data.get('items'),
            "quantity": request.data.get('quantity'),
            "status": request.data.get('status'),
            "quality_rating": request.data.get('quality_rating'),
            "issue_date": request.data.get('issue_date'),
            "acknowledgment_date": request.data.get('acknowledgment_date'),
            "vendor_code": request.data.get('vendor_code')
        }
        serializer = PurchaseOrderSerializer(instance=saved_article, data=pos, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "{}".format(pos)})

    def delete(self, request, pachi):
        article = get_object_or_404(PurchaseOrderModel.objects.all(), pk=pachi)
        article.delete()
        return Response({"message": "Article with id `{}` has been deleted.".format(pachi)},status=204)


class GetPerformanceView(APIView):
    def get(self, request,pachi):
        pos = VendorModel.objects.filter(vendor_code=pachi)
        serializer = VendorPerformanceSerializer(pos, many=True)
        return Response({"performance_metrics": serializer.data})

# class VendorCreateListView(generics.ListCreateAPIView):
#     queryset = VendorModel.objects.all()
#     serializer_class = VendorSerializer

# class VendorRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = VendorModel.objects.all()
#     serializer_class = VendorSerializer

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
    

def home(request):
    return render(request, 'home.html')

# def avg_quality_rating(request):
#     average_quantities = Vend.objects.values('group__group_id', 'group__group_name').annotate(
#     average_quantity=Avg('quantity')
# )

# def UpdateThirdTable(request):
    
#     #On-Time Delivery Rate
#     with connection.cursor() as cursor:
#         sql_query = "SELECT COUNT(*) FROM mainApp_purchaseordermodel WHERE status='completed' AND vendor_code=%s"
#         # sql_query = "INSERT INTO med_stock(doses,med_name,quantity,mrp,batch_no,expiry_date) VALUES (%s,%s,%s,%s,%s,%s)"
#         cursor.execute(sql_query,[str(vendor_code)])
#         res = cursor.fetchall()
#     den = res[0][0]
    
#     with connection.cursor() as cursor:
#         sql_query = "SELECT COUNT(*) FROM mainApp_purchaseordermodel WHERE status='completed' AND vendor_code=%s"
#         # sql_query = "INSERT INTO med_stock(doses,med_name,quantity,mrp,batch_no,expiry_date) VALUES (%s,%s,%s,%s,%s,%s)"
#         cursor.execute(sql_query,[str(vendor_code)])
#         res = cursor.fetchall()
#     den = res[0][0]
    
    
    
    
#     if (c1,c2,c5) in b1:
#                 with connection.cursor() as cursor:
#                     sql_query = "SELECT quantity FROM med_stock WHERE batch_no=%s"
#                     # sql_query = "INSERT INTO med_stock(doses,med_name,quantity,mrp,batch_no,expiry_date) VALUES (%s,%s,%s,%s,%s,%s)"
#                     cursor.execute(sql_query,[str(c5)])
#                     res = cursor.fetchall()
#                 temp = res[0][0]
#                 qty = int(temp)+int(c3)
#                 with connection.cursor() as cursor:
#                     sql_query = "UPDATE med_stock SET quantity=%s WHERE batch_no=%s"
#                     cursor.execute(sql_query,[str(qty),str(c5)])
#                 connection.commit()
            
#             if (c1,c2,c5) not in b1:
#                 with connection.cursor() as cursor:
#                     sql_query = "INSERT INTO med_stock(doses,med_name,quantity,mrp,batch_no,expiry_date,amount) VALUES (%s,%s,%s,%s,%s,%s,%s)"
#                     cursor.execute(sql_query,[str(c1),str(c2),str(c3),str(c4),str(c5),str(c6),str(c7)])
#                 connection.commit()