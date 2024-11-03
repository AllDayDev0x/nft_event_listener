# events/models.py
from django.db import models

class TransferEvent(models.Model):
    token_id = models.BigIntegerField()
    from_address = models.CharField(max_length=42)
    to_address = models.CharField(max_length=42)
    transaction_hash = models.CharField(max_length=66)
    block_number = models.IntegerField()

    def __str__(self):
        return f"Token {self.token_id} from {self.from_address} to {self.to_address}"