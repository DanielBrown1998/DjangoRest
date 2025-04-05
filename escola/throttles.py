from rest_framework.throttling import AnonRateThrottle

class MatriculaThrottle(AnonRateThrottle):
    rate = '5/day'
