from activities.models import Activities, ActivityCategory


class ActivitiesService(object):

    def get_activities(self, filter):

        try:

            if bool(filter):
                results = Activities.objects.filter(**filter)
                return results
            else:
                raise Exception('dictionary is null')
            
        except Exception as e:
            print("\nExeption: \n{}".format(e))


    def get_activity_categories(self, activity_id):

        try:

            if bool(filter):
                results = ActivityCategory.objects.filter(**{"status": 1, "activity": activity_id})
                return results
            else:
                raise Exception('dictionary is null')
            
        except Exception as e:
            print("\nExeption: \n{}".format(e))