
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.coupon_api import CouponApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from sandbox.api.coupon_api import CouponApi
from sandbox.api.operator_api import OperatorApi
from sandbox.api.order_api import OrderApi
from sandbox.api.stats_api import StatsApi
from sandbox.api.subscriber_api import SubscriberApi
