from rest_framework import serializers
from .models import VendorModel,PurchaseOrderModel,HistoricalPerformanceModel

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorModel
        fields = ['vendor_code', 'name', 'contact_details','address']
    
    def create(self, validated_data):
        return VendorModel.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.vendor_code = validated_data.get('vendor_code', instance.vendor_code)
        instance.name = validated_data.get('name', instance.name)
        instance.contact_details = validated_data.get('contact_details', instance.contact_details)
        instance.address = validated_data.get('address', instance.address)
        # instance.on_time_delivery_rate = validated_data.get('on_time_delivery_rate', instance.on_time_delivery_rate)
        # instance.quality_rating_avg = validated_data.get('quality_rating_avg', instance.quality_rating_avg)
        # instance.average_response_time = validated_data.get('average_response_time', instance.average_response_time)
        # instance.fulfillment_rate = validated_data.get('fulfillment_rate', instance.fulfillment_rate)

        instance.save()
        return instance
        
class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrderModel
        fields = "__all__"
    
    def create(self, validated_data):
        return PurchaseOrderModel.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.po_number = validated_data.get('po_number', instance.po_number)
        instance.vendor_code = validated_data.get('vendor_code', instance.vendor_code)
        instance.order_date = validated_data.get('order_date', instance.order_date)
        instance.delivery_date = validated_data.get('delivery_date', instance.delivery_date)
        instance.items = validated_data.get('items', instance.items)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.status = validated_data.get('status', instance.status)
        instance.quality_rating = validated_data.get('quality_rating', instance.quality_rating)
        instance.issue_date = validated_data.get('issue_date', instance.issue_date)
        instance.acknowledgment_date = validated_data.get('acknowledgment_date', instance.acknowledgment_date)

        instance.save()
        return instance
        
class VendorPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorModel
        fields = ['vendor_code', 'on_time_delivery_rate', 'quality_rating_avg', 'average_response_time','fulfillment_rate']
