# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from soracom_api.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from soracom_api.model.api_audit_log_entry import APIAuditLogEntry
from soracom_api.model.api_call_error import APICallError
from soracom_api.model.api_call_error_message import APICallErrorMessage
from soracom_api.model.action_config import ActionConfig
from soracom_api.model.action_config_property import ActionConfigProperty
from soracom_api.model.air_stats_response import AirStatsResponse
from soracom_api.model.arc_credential_attach_request import ArcCredentialAttachRequest
from soracom_api.model.arc_credential_attach_response import ArcCredentialAttachResponse
from soracom_api.model.arc_credential_renew_request import ArcCredentialRenewRequest
from soracom_api.model.arc_credential_renew_response import ArcCredentialRenewResponse
from soracom_api.model.arc_session_create_response import ArcSessionCreateResponse
from soracom_api.model.arc_session_status import ArcSessionStatus
from soracom_api.model.attach_role_request import AttachRoleRequest
from soracom_api.model.attribute_update import AttributeUpdate
from soracom_api.model.auth_key_response import AuthKeyResponse
from soracom_api.model.auth_request import AuthRequest
from soracom_api.model.auth_response import AuthResponse
from soracom_api.model.available_long_term_discount_model import AvailableLongTermDiscountModel
from soracom_api.model.available_long_term_discount_response import AvailableLongTermDiscountResponse
from soracom_api.model.beam_stats_response import BeamStatsResponse
from soracom_api.model.capabilities import Capabilities
from soracom_api.model.cell import Cell
from soracom_api.model.cell_identifier import CellIdentifier
from soracom_api.model.cell_location import CellLocation
from soracom_api.model.company_information_model import CompanyInformationModel
from soracom_api.model.contract_updated_response import ContractUpdatedResponse
from soracom_api.model.contract_updating_request import ContractUpdatingRequest
from soracom_api.model.coupon_response import CouponResponse
from soracom_api.model.create_and_update_credentials_model import CreateAndUpdateCredentialsModel
from soracom_api.model.create_estimated_coupon_request import CreateEstimatedCouponRequest
from soracom_api.model.create_estimated_order_request import CreateEstimatedOrderRequest
from soracom_api.model.create_estimated_volume_discount_request import CreateEstimatedVolumeDiscountRequest
from soracom_api.model.create_event_handler_request import CreateEventHandlerRequest
from soracom_api.model.create_group_request import CreateGroupRequest
from soracom_api.model.create_or_update_role_request import CreateOrUpdateRoleRequest
from soracom_api.model.create_port_mapping_request import CreatePortMappingRequest
from soracom_api.model.create_role_response import CreateRoleResponse
from soracom_api.model.create_sim_request import CreateSimRequest
from soracom_api.model.create_soralet_request import CreateSoraletRequest
from soracom_api.model.create_user_password_request import CreateUserPasswordRequest
from soracom_api.model.create_user_request import CreateUserRequest
from soracom_api.model.create_virtual_private_gateway_request import CreateVirtualPrivateGatewayRequest
from soracom_api.model.create_vpc_peering_connection_request import CreateVpcPeeringConnectionRequest
from soracom_api.model.credentials_model import CredentialsModel
from soracom_api.model.credit_card import CreditCard
from soracom_api.model.daily_bill import DailyBill
from soracom_api.model.daily_bill_response import DailyBillResponse
from soracom_api.model.data_entry import DataEntry
from soracom_api.model.data_source_resource_metadata import DataSourceResourceMetadata
from soracom_api.model.data_traffic_stats import DataTrafficStats
from soracom_api.model.device import Device
from soracom_api.model.device_object_model import DeviceObjectModel
from soracom_api.model.diagnostic_request import DiagnosticRequest
from soracom_api.model.diagnostic_response import DiagnosticResponse
from soracom_api.model.downlink_ping_request import DownlinkPingRequest
from soracom_api.model.downlink_ping_response import DownlinkPingResponse
from soracom_api.model.emails_model import EmailsModel
from soracom_api.model.enable_mfaotp_response import EnableMFAOTPResponse
from soracom_api.model.error import Error
from soracom_api.model.estimated_coupon_model import EstimatedCouponModel
from soracom_api.model.estimated_order_item_model import EstimatedOrderItemModel
from soracom_api.model.estimated_order_model import EstimatedOrderModel
from soracom_api.model.estimated_volume_discount_model import EstimatedVolumeDiscountModel
from soracom_api.model.event_handler_model import EventHandlerModel
from soracom_api.model.execute_soralet_request import ExecuteSoraletRequest
from soracom_api.model.execute_soralet_response import ExecuteSoraletResponse
from soracom_api.model.expiry_time import ExpiryTime
from soracom_api.model.export_request import ExportRequest
from soracom_api.model.file_entry import FileEntry
from soracom_api.model.file_export_response import FileExportResponse
from soracom_api.model.funnel_aws_firehose_destination import FunnelAWSFirehoseDestination
from soracom_api.model.funnel_awsio_t_destination import FunnelAWSIoTDestination
from soracom_api.model.funnel_aws_kinesis_destination import FunnelAWSKinesisDestination
from soracom_api.model.funnel_acroquest_torrentio_destination import FunnelAcroquestTorrentioDestination
from soracom_api.model.funnel_appresso_data_spider_destination import FunnelAppressoDataSpiderDestination
from soracom_api.model.funnel_azure_event_hub_destination import FunnelAzureEventHubDestination
from soracom_api.model.funnel_brains_tech_impulse_destination import FunnelBrainsTechImpulseDestination
from soracom_api.model.funnel_configuration import FunnelConfiguration
from soracom_api.model.funnel_content_type import FunnelContentType
from soracom_api.model.funnel_destination import FunnelDestination
from soracom_api.model.funnel_esrij_arcgis_online_destination import FunnelEsrijArcgisOnlineDestination
from soracom_api.model.funnel_fusic_mockmock_datarecorder_destination import FunnelFusicMockmockDatarecorderDestination
from soracom_api.model.funnel_google_pub_sub_destination import FunnelGooglePubSubDestination
from soracom_api.model.funnel_infoteria_platio_destination import FunnelInfoteriaPlatioDestination
from soracom_api.model.funnel_kii_thingif_destination import FunnelKiiThingifDestination
from soracom_api.model.funnel_landlog_destination import FunnelLandlogDestination
from soracom_api.model.funnel_optim_cloudiotos_destination import FunnelOptimCloudiotosDestination
from soracom_api.model.funnel_sensor_corpus_destination import FunnelSensorCorpusDestination
from soracom_api.model.funnel_teradata_intellicloud_destination import FunnelTeradataIntellicloudDestination
from soracom_api.model.funnel_wingarc_motionboard_destination import FunnelWingarcMotionboardDestination
from soracom_api.model.funnel_yaskawa_mmcloud_destination import FunnelYaskawaMmcloudDestination
from soracom_api.model.gadget import Gadget
from soracom_api.model.gadget_registration_request import GadgetRegistrationRequest
from soracom_api.model.gate_peer import GatePeer
from soracom_api.model.generate_operators_auth_key_response import GenerateOperatorsAuthKeyResponse
from soracom_api.model.generate_token_request import GenerateTokenRequest
from soracom_api.model.generate_token_response import GenerateTokenResponse
from soracom_api.model.generate_user_auth_key_response import GenerateUserAuthKeyResponse
from soracom_api.model.get_billing_history_response import GetBillingHistoryResponse
from soracom_api.model.get_default_permissions_response import GetDefaultPermissionsResponse
from soracom_api.model.get_exported_file_response import GetExportedFileResponse
from soracom_api.model.get_latest_bill import GetLatestBill
from soracom_api.model.get_operator_response import GetOperatorResponse
from soracom_api.model.get_order_response import GetOrderResponse
from soracom_api.model.get_payment_method_result import GetPaymentMethodResult
from soracom_api.model.get_payment_transaction_result import GetPaymentTransactionResult
from soracom_api.model.get_shipping_address_response import GetShippingAddressResponse
from soracom_api.model.get_user_password_response import GetUserPasswordResponse
from soracom_api.model.get_user_permission_response import GetUserPermissionResponse
from soracom_api.model.get_volume_discount_response import GetVolumeDiscountResponse
from soracom_api.model.global_sim_applet_plmn_record import GlobalSimAppletPLMNRecord
from soracom_api.model.group import Group
from soracom_api.model.group_configuration_update_request import GroupConfigurationUpdateRequest
from soracom_api.model.harvest_exported_data_stats_response import HarvestExportedDataStatsResponse
from soracom_api.model.imei_lock import ImeiLock
from soracom_api.model.individual_information_model import IndividualInformationModel
from soracom_api.model.inline_object import InlineObject
from soracom_api.model.inline_object1 import InlineObject1
from soracom_api.model.inline_object2 import InlineObject2
from soracom_api.model.inline_object3 import InlineObject3
from soracom_api.model.insight import Insight
from soracom_api.model.ip_address_map_entry import IpAddressMapEntry
from soracom_api.model.issue_add_email_token_request import IssueAddEmailTokenRequest
from soracom_api.model.issue_password_reset_token_request import IssuePasswordResetTokenRequest
from soracom_api.model.issue_subscriber_transfer_token_request import IssueSubscriberTransferTokenRequest
from soracom_api.model.issue_subscriber_transfer_token_response import IssueSubscriberTransferTokenResponse
from soracom_api.model.junction_inspection_configuration import JunctionInspectionConfiguration
from soracom_api.model.junction_mirroring_configuration import JunctionMirroringConfiguration
from soracom_api.model.junction_mirroring_peer import JunctionMirroringPeer
from soracom_api.model.junction_redirection_configuration import JunctionRedirectionConfiguration
from soracom_api.model.lagoon_dashboard_permissions_response import LagoonDashboardPermissionsResponse
from soracom_api.model.lagoon_dashboard_permissions_response_permissions import LagoonDashboardPermissionsResponsePermissions
from soracom_api.model.lagoon_dashboard_permissions_updating_request import LagoonDashboardPermissionsUpdatingRequest
from soracom_api.model.lagoon_dashboard_permissions_updating_request_permissions import LagoonDashboardPermissionsUpdatingRequestPermissions
from soracom_api.model.lagoon_license_pack_status_response import LagoonLicensePackStatusResponse
from soracom_api.model.lagoon_license_packs_updating_request import LagoonLicensePacksUpdatingRequest
from soracom_api.model.lagoon_license_packs_updating_request_license_pack_quantities import LagoonLicensePacksUpdatingRequestLicensePackQuantities
from soracom_api.model.lagoon_migration_from_classic_request import LagoonMigrationFromClassicRequest
from soracom_api.model.lagoon_plan_changing_request import LagoonPlanChangingRequest
from soracom_api.model.lagoon_registration_request import LagoonRegistrationRequest
from soracom_api.model.lagoon_registration_response import LagoonRegistrationResponse
from soracom_api.model.lagoon_user import LagoonUser
from soracom_api.model.lagoon_user_creation_request import LagoonUserCreationRequest
from soracom_api.model.lagoon_user_creation_response import LagoonUserCreationResponse
from soracom_api.model.lagoon_user_email_updating_request import LagoonUserEmailUpdatingRequest
from soracom_api.model.lagoon_user_password_updating_request import LagoonUserPasswordUpdatingRequest
from soracom_api.model.lagoon_user_permission_updating_request import LagoonUserPermissionUpdatingRequest
from soracom_api.model.last_seen import LastSeen
from soracom_api.model.list_coupon_response import ListCouponResponse
from soracom_api.model.list_order_response import ListOrderResponse
from soracom_api.model.list_ordered_subscriber_response import ListOrderedSubscriberResponse
from soracom_api.model.list_payment_statement_response import ListPaymentStatementResponse
from soracom_api.model.list_product_response import ListProductResponse
from soracom_api.model.list_roles_response import ListRolesResponse
from soracom_api.model.list_shipping_address_response import ListShippingAddressResponse
from soracom_api.model.list_volume_discount_response import ListVolumeDiscountResponse
from soracom_api.model.log_entry import LogEntry
from soracom_api.model.lora_data import LoraData
from soracom_api.model.lora_device import LoraDevice
from soracom_api.model.lora_gateway import LoraGateway
from soracom_api.model.lora_network_set import LoraNetworkSet
from soracom_api.model.mfa_authentication_request import MFAAuthenticationRequest
from soracom_api.model.mfa_issue_revoking_token_request import MFAIssueRevokingTokenRequest
from soracom_api.model.mfa_revoking_token_verify_request import MFARevokingTokenVerifyRequest
from soracom_api.model.mfa_status_of_use_response import MFAStatusOfUseResponse
from soracom_api.model.mapping_entries import MappingEntries
from soracom_api.model.monthly_bill import MonthlyBill
from soracom_api.model.napter_audit_log_direction import NapterAuditLogDirection
from soracom_api.model.napter_audit_log_entry import NapterAuditLogEntry
from soracom_api.model.napter_audit_logs_exported_data_stats_response import NapterAuditLogsExportedDataStatsResponse
from soracom_api.model.object_instance import ObjectInstance
from soracom_api.model.open_gate_request import OpenGateRequest
from soracom_api.model.operator_mfa_verifying_response import OperatorMFAVerifyingResponse
from soracom_api.model.order_item_model import OrderItemModel
from soracom_api.model.ordered_subscriber import OrderedSubscriber
from soracom_api.model.packet_capture_session import PacketCaptureSession
from soracom_api.model.packet_capture_session_request import PacketCaptureSessionRequest
from soracom_api.model.payment_amount import PaymentAmount
from soracom_api.model.payment_description import PaymentDescription
from soracom_api.model.payment_statement_response import PaymentStatementResponse
from soracom_api.model.placement import Placement
from soracom_api.model.port_mapping import PortMapping
from soracom_api.model.port_mapping_destination import PortMappingDestination
from soracom_api.model.port_mapping_source import PortMappingSource
from soracom_api.model.previous_session_status import PreviousSessionStatus
from soracom_api.model.price_by_quantity import PriceByQuantity
from soracom_api.model.product_model import ProductModel
from soracom_api.model.put_ip_address_map_entry_request import PutIpAddressMapEntryRequest
from soracom_api.model.reference_url import ReferenceUrl
from soracom_api.model.register_gate_peer_request import RegisterGatePeerRequest
from soracom_api.model.register_lora_device_request import RegisterLoraDeviceRequest
from soracom_api.model.register_operators_request import RegisterOperatorsRequest
from soracom_api.model.register_payer_information_model import RegisterPayerInformationModel
from soracom_api.model.register_sim_request import RegisterSimRequest
from soracom_api.model.register_subscribers_request import RegisterSubscribersRequest
from soracom_api.model.resource_instance import ResourceInstance
from soracom_api.model.role_response import RoleResponse
from soracom_api.model.routing_filter_entry import RoutingFilterEntry
from soracom_api.model.rule_config import RuleConfig
from soracom_api.model.rule_config_property import RuleConfigProperty
from soracom_api.model.session_event import SessionEvent
from soracom_api.model.session_status import SessionStatus
from soracom_api.model.set_device_object_model_scope_request import SetDeviceObjectModelScopeRequest
from soracom_api.model.set_group_request import SetGroupRequest
from soracom_api.model.set_imei_lock_request import SetImeiLockRequest
from soracom_api.model.set_network_set_request import SetNetworkSetRequest
from soracom_api.model.set_system_notifications_request import SetSystemNotificationsRequest
from soracom_api.model.set_user_permission_request import SetUserPermissionRequest
from soracom_api.model.shipping_address_model import ShippingAddressModel
from soracom_api.model.shipping_cost_model import ShippingCostModel
from soracom_api.model.sigfox_data import SigfoxData
from soracom_api.model.sigfox_device import SigfoxDevice
from soracom_api.model.sigfox_registration_request import SigfoxRegistrationRequest
from soracom_api.model.sim import Sim
from soracom_api.model.sim_profile import SimProfile
from soracom_api.model.simplified_subscriber import SimplifiedSubscriber
from soracom_api.model.sms_forwarding_report import SmsForwardingReport
from soracom_api.model.sms_forwarding_request import SmsForwardingRequest
from soracom_api.model.soracom_beam_stats import SoracomBeamStats
from soracom_api.model.soralet import Soralet
from soracom_api.model.soralet_data_source import SoraletDataSource
from soracom_api.model.soralet_log import SoraletLog
from soracom_api.model.soralet_version import SoraletVersion
from soracom_api.model.subscriber import Subscriber
from soracom_api.model.subscription_container import SubscriptionContainer
from soracom_api.model.subscription_container_status import SubscriptionContainerStatus
from soracom_api.model.subscription_container_status_country_mapping import SubscriptionContainerStatusCountryMapping
from soracom_api.model.subscription_container_status_mapping_record import SubscriptionContainerStatusMappingRecord
from soracom_api.model.support_token_response import SupportTokenResponse
from soracom_api.model.system_notifications_model import SystemNotificationsModel
from soracom_api.model.tag_set import TagSet
from soracom_api.model.tag_update_request import TagUpdateRequest
from soracom_api.model.traffic_volume_ranking import TrafficVolumeRanking
from soracom_api.model.update_default_permissions_request import UpdateDefaultPermissionsRequest
from soracom_api.model.update_event_handler_request import UpdateEventHandlerRequest
from soracom_api.model.update_password_request import UpdatePasswordRequest
from soracom_api.model.update_permission_request import UpdatePermissionRequest
from soracom_api.model.update_speed_class_request import UpdateSpeedClassRequest
from soracom_api.model.update_user_request import UpdateUserRequest
from soracom_api.model.user_detail_response import UserDetailResponse
from soracom_api.model.verify_add_email_token_request import VerifyAddEmailTokenRequest
from soracom_api.model.verify_operators_request import VerifyOperatorsRequest
from soracom_api.model.verify_password_reset_token_request import VerifyPasswordResetTokenRequest
from soracom_api.model.verify_subscriber_transfer_token_request import VerifySubscriberTransferTokenRequest
from soracom_api.model.verify_subscriber_transfer_token_response import VerifySubscriberTransferTokenResponse
from soracom_api.model.virtual_private_gateway import VirtualPrivateGateway
from soracom_api.model.volume_discount_model import VolumeDiscountModel
from soracom_api.model.vpc_peering_connection import VpcPeeringConnection