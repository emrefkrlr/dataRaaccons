from urllib.parse import ParseResultBytes
from package.models import UserPackage, Package, PackagePrice
from datetime import datetime, timedelta
import pytz


class PackageService(object):

    def __init__(self):

        self.utc=pytz.UTC
        self.now_date = self.utc.localize(datetime.now())


    def get_package(self, package):

        try:
            
            package = Package.objects.get(name=package)

            return package if package else False
            
        except Exception as e:
            print(" PackageService get_package Exeption \n {} \n PackageID".format(e, package))


    def get_all_packages(self):

        try:

            packages = Package.objects.all()
            
            return packages if packages else False

        except Exception as e:
            print(" PackageService get_all_packages Exeption: {}".format(e))


    def get_package_info(self, package):

        try:

            package_info = PackagePrice.objects.get(package=package)

            return package_info if package_info else False

        except Exception as e:
            print(" PackageService get_packages_info Exeption: {}".format(e))





    
    def get_user_package(self, user):

        try:

            package = UserPackage.objects.get(user=user)

            return package if package else False

        except Exception as e:
            print(" PackageService get_user_package Exeption \n {} \n UserID {}".format(e, user))


    def set_user_package(self, user, package):

        try:
            
            package_days = PackagePrice.objects.get(package=package)
            expired_date = datetime.now() + timedelta(days = int(package_days.days))
            package = UserPackage.objects.update_or_create(user=user, package=package, expired_at=expired_date)

            return package if package else False

        except Exception as e:
            print(" PackageService set_user_package Exeption \n {} \n UserID {} \n PackageID {}".format(e, user, package))


    def get_user_package_warning(self, user):

        try:

            DASHBOARD_STATUS = False
            PACKAGE_MESSAGE = "The package defined for the user could not be found."

            package = self.get_user_package(user=user)
            
            if package:

                PACKAGE_TYPE = package.package

                if self.now_date > package.expired_at:
                    
                    PACKAGE_MESSAGE = "Your defined package has expired, please renew."

                elif (package.expired_at - self.now_date).days < 4:

                    DASHBOARD_STATUS = True
                    PACKAGE_MESSAGE = "Your defined package will expire after {} days. If you want to continue to benefit from our product, you must renew it.".format((package.expired_at - self.now_date).days)

                else:

                    DASHBOARD_STATUS = True
                    PACKAGE_MESSAGE = None

            return DASHBOARD_STATUS, PACKAGE_MESSAGE, PACKAGE_TYPE

        except Exception as e:
            print(" PackageService get_user_package_warning Exeption \n {} \n UserID {} \n PackageID {}".format(e, user, package))



        