# we can Inherite that class and we can set rate for every child class

from rest_framework.throttling import UserRateThrottle

class StudentRateThrottle(UserRateThrottle):
    scope = 'student'