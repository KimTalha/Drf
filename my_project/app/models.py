from django.db import models
from django.contrib.auth.models import User


class NFT(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='images/nft/', blank=True)
    is_verified = models.BooleanField(default=False)
    minting_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Additional fields
    artist = models.ForeignKey(User, on_delete=models.CASCADE, related_name="get_artist")
    edition_size = models.PositiveIntegerField()
    royalties_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    external_link = models.URLField()
    ownership_history = models.TextField(null=True, blank=True)
    token_metadata_uri = models.URLField(blank=True)
    attributes = models.JSONField(default={"data": ""})
    is_sold = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    current_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="get_current_owner")

    def __str__(self):
        return self.name
