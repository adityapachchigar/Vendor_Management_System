from django.db import models

# Create your models here.

class VendorModel(models.Model):
    vendor_code = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=30)
    contact_details = models.TextField(blank = True)
    address = models.TextField(blank = True)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField(default=0.0)
    
    def get_performance_metrics(self):
        performance_metrics = {
            'on_time_delivery_rate': self.on_time_delivery_rate,
            'quality_rating_avg': self.quality_rating_avg,
            'average_response_time': self.average_response_time,
            'fulfillment_rate': self.fulfillment_rate,
        }
        return performance_metrics
    
class PurchaseOrderModel(models.Model):
    po_number = models.CharField(primary_key=True,max_length=20)
    vendor_code = models.ForeignKey(VendorModel, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField(blank=True, null=True)
    quantity = models.IntegerField()
    status = models.CharField(max_length=20)
    quality_rating = models.FloatField(null=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField()
    
class HistoricalPerformanceModel(models.Model):
    vendor_code = models.ForeignKey(VendorModel, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()
    
    
    