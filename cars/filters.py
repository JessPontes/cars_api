from dj_rql.filter_cls import AutoRQLFilterClass
from cars.models import Brand, Car

class BrandFilterClass(AutoRQLFilterClass):
    MODEL= Brand


class CarfilterClass(AutoRQLFilterClass):
    MODEL = Car
    FILTER = [
        {
            'filter': 'brand',
            'source': 'brand__name',
        },
        {
            'filter':'owner',
            'source': 'owner__username',
        },
    ]