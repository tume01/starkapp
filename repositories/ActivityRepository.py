from datetime import datetime
from activities.models import Activity
from .BaseRepository import BaseRepository
from activities.models import ActivityRegistration
from contracts.repositories import AbstractBaseRepository

class ActivityRepository(BaseRepository):

    def __init__(self):
        BaseRepository.__init__(self, Activity)

    def addMember(self, activity, member):
        registration = ActivityRegistration(activity=activity, member=member, registered_at=datetime.now())

        return not registration.save()