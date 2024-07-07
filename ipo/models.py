from django.db import models

class IPOInfo(models.Model):
    company_name = models.CharField(max_length=255)
    company_logo_path = models.TextField()
    price_band = models.CharField(max_length=255)
    open = models.CharField(max_length=255)
    close = models.CharField(max_length=255)
    issue_size = models.CharField(max_length=255)
    issue_type = models.CharField(max_length=255)
    listing_date = models.CharField(max_length=255)
    status = models.IntegerField()
    ipo_price = models.CharField(max_length=255)
    listing_price = models.CharField(max_length=255)
    listing_gain = models.CharField(max_length=255)
    listing_dathr = models.CharField(max_length=255)
    cmp = models.CharField(max_length=255)
    current_return = models.CharField(max_length=255)
    rhp = models.CharField(max_length=255)
    drhp = models.CharField(max_length=255)

    def __str__(self):
        return self.company_name
