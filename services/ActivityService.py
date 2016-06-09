from datetime import datetime
from repositories import ActivityRepository

class ActivityService(object):

    """docstring for ActivityService"""

    __activity_repository = ActivityRepository.ActivityRepository()

    def create(self, insert_data):
        return self.__activity_repository.create(insert_data)

    def update(self, id, update_data):
        return self.__activity_repository.update(id, update_data)

    def delete(self, id):
        return self.__activity_repository.delete(id)

    def getActivities(self):
        return self.__activity_repository.all()

    def filter(self, filters):
        return self.__activity_repository.filter(filters)

    def getActivity(self, id):
        return self.__activity_repository.find(id)

    def removeMember(self, activity_id, member_id):

        activity = self.getActivity(activity_id)

        return activity.activityregistration_set.filter(member_id=member_id).update(deleted_at=datetime.now())

    def getActivityMembers(self, activity_id):

        activity = self.getActivity(activity_id)

        return activity.activityregistration_set.filter(deleted_at=None)

    def addMember(self, activity_id, member):
        activity = self.getActivity(activity_id)

        assistants = activity.activityregistration_set.filter(deleted_at=None).count()

        if activity.attendance > assistants:

            if not activity.activityregistration_set.filter(member_id=member.id, deleted_at=None):
                return self.__activity_repository.addMember(activity, member)

        return None