from unicodedata import name
from activities.models import Activities, ActivityCategory


class ActivitiesService(object):


    def get_all_activities(self):

        try:

            activities = Activities.objects.filter(status=1)

            # return active activities
            return activities if activities else False
            
        except Exception as e:
            print(" ActivitiesService get_all_activities Exveption: {}".format(e))


    def get_activity(self, activity):

        try:

            activity = Activities.objects.get(status=1, name=activity)

            # return active activities
            return activity if activity else False
            
        except Exception as e:
            print(" ActivitiesService get_all_activities Exveption: {}".format(e))


    def get_activity_categories(self, activity):

        try:

            activity_categories = ActivityCategory.objects.filter(status=1, activity=activity)

            # return active activity categories
            return activity_categories if activity_categories else False
            
        except Exception as e:
            print("\nExeption: \n{}".format(e))


    def get_activity_category(self, activity, activity_category):

        try:
            
            activity_category = ActivityCategory.objects.get(status=1, activity=activity, name=activity_category)

            # return activity category
            return activity_category if activity_category else False

        except Exception as e:
            print("ActivitiesService get_activity_category Exception: \n{}".format(e))




    def get_personal_activities(self):

        try:

            activities = Activities.objects.filter(use_personal=1)

            return activities if activities else False

        except Exception as e:
            print(" ActivitiesService get_personal_activities Exception: {}".format(e))

