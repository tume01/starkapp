from django.db import models
from memberships.models import MembershipType
from bungalow_type.models import BungalowType
from events_type.models import EventsType
# Create your models here.
class Promotion(models.Model):
    description = models.TextField(max_length=200)
    percentage = models.FloatField()
    status = models.IntegerField()
    #status 0 if the promotion isn't valid anymore
    membership_promotions = models.ManyToManyField(
        MembershipType,
        through="MembershipPromotion",
        through_fields=('promotion', 'membership_type'),
    )
    bungalow_reservation_promotions = models.ManyToManyField(
        BungalowType,
        through="BungalowReservationPromotion",
        through_fields=('promotion', 'bungalow_type'),
    )
    event_promotions = models.ManyToManyField(
        EventsType,
        through="EventPromotion",
        through_fields=('promotion', 'event_type'),
    )

class MembershipPromotion(models.Model):
    membership_type = models.ForeignKey(MembershipType, on_delete=models.CASCADE)
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)
    deleted_at = models.DateTimeField(null=True)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    percentage = models.DateTimeField()

class BungalowReservationPromotion(models.Model):
    membership_type = models.ForeignKey(MembershipType, on_delete=models.CASCADE)
    bungalow_type = models.ForeignKey(BungalowType, on_delete=models.CASCADE)
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)
    deleted_at = models.DateTimeField(null=True)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    percentage = models.DateTimeField()

class EventPromotion(models.Model):
    membership_type = models.ForeignKey(MembershipType, on_delete=models.CASCADE)
    event_type = models.ForeignKey(EventsType, on_delete=models.CASCADE)
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)
    deleted_at = models.DateTimeField(null=True)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    percentage = models.DateTimeField()