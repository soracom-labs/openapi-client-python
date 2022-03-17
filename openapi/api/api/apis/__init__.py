
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.audit_log_api import AuditLogApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from api.api.audit_log_api import AuditLogApi
from api.api.auth_api import AuthApi
from api.api.billing_api import BillingApi
from api.api.cell_location_api import CellLocationApi
from api.api.credential_api import CredentialApi
from api.api.data_entry_api import DataEntryApi
from api.api.device_api import DeviceApi
from api.api.device_object_model_api import DeviceObjectModelApi
from api.api.diagnostic_api import DiagnosticApi
from api.api.email_api import EmailApi
from api.api.event_handler_api import EventHandlerApi
from api.api.file_entry_api import FileEntryApi
from api.api.files_api import FilesApi
from api.api.gadget_api import GadgetApi
from api.api.group_api import GroupApi
from api.api.lagoon_api import LagoonApi
from api.api.log_api import LogApi
from api.api.lora_device_api import LoraDeviceApi
from api.api.lora_gateway_api import LoraGatewayApi
from api.api.lora_network_set_api import LoraNetworkSetApi
from api.api.operator_api import OperatorApi
from api.api.order_api import OrderApi
from api.api.payment_api import PaymentApi
from api.api.port_mapping_api import PortMappingApi
from api.api.query_api import QueryApi
from api.api.role_api import RoleApi
from api.api.shipping_address_api import ShippingAddressApi
from api.api.sigfox_device_api import SigfoxDeviceApi
from api.api.sim_api import SimApi
from api.api.soralet_api import SoraletApi
from api.api.stats_api import StatsApi
from api.api.subscriber_api import SubscriberApi
from api.api.system_notification_api import SystemNotificationApi
from api.api.user_api import UserApi
from api.api.virtual_private_gateway_api import VirtualPrivateGatewayApi
