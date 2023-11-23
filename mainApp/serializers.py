from rest_framework import serializers
from .models import VendorModel,PurchaseOrderModel,HistoricalPerformanceModel

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorModel
        fields = ['vendor_code', 'name', 'contact_details', 'address']
        
class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrderModel
        fields = "__all__"
        
class VendorPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorModel
        fields = ['vendor_code', 'on_time_delivery_rate', 'quality_rating_avg', 'average_response_time','fulfillment_rate']
