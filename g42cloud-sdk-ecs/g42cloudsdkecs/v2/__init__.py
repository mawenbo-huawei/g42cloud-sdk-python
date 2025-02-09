# coding: utf-8

from __future__ import absolute_import

# import EcsClient
from g42cloudsdkecs.v2.ecs_client import EcsClient
from g42cloudsdkecs.v2.ecs_async_client import EcsAsyncClient
# import models into sdk package
from g42cloudsdkecs.v2.model.add_server_group_member_request import AddServerGroupMemberRequest
from g42cloudsdkecs.v2.model.add_server_group_member_request_body import AddServerGroupMemberRequestBody
from g42cloudsdkecs.v2.model.add_server_group_member_response import AddServerGroupMemberResponse
from g42cloudsdkecs.v2.model.associate_server_virtual_ip_option import AssociateServerVirtualIpOption
from g42cloudsdkecs.v2.model.associate_server_virtual_ip_request import AssociateServerVirtualIpRequest
from g42cloudsdkecs.v2.model.associate_server_virtual_ip_request_body import AssociateServerVirtualIpRequestBody
from g42cloudsdkecs.v2.model.associate_server_virtual_ip_response import AssociateServerVirtualIpResponse
from g42cloudsdkecs.v2.model.attach_server_volume_option import AttachServerVolumeOption
from g42cloudsdkecs.v2.model.attach_server_volume_request import AttachServerVolumeRequest
from g42cloudsdkecs.v2.model.attach_server_volume_request_body import AttachServerVolumeRequestBody
from g42cloudsdkecs.v2.model.attach_server_volume_response import AttachServerVolumeResponse
from g42cloudsdkecs.v2.model.batch_add_server_nic_option import BatchAddServerNicOption
from g42cloudsdkecs.v2.model.batch_add_server_nics_request import BatchAddServerNicsRequest
from g42cloudsdkecs.v2.model.batch_add_server_nics_request_body import BatchAddServerNicsRequestBody
from g42cloudsdkecs.v2.model.batch_add_server_nics_response import BatchAddServerNicsResponse
from g42cloudsdkecs.v2.model.batch_attach_sharable_volumes_option import BatchAttachSharableVolumesOption
from g42cloudsdkecs.v2.model.batch_attach_sharable_volumes_request import BatchAttachSharableVolumesRequest
from g42cloudsdkecs.v2.model.batch_attach_sharable_volumes_request_body import BatchAttachSharableVolumesRequestBody
from g42cloudsdkecs.v2.model.batch_attach_sharable_volumes_response import BatchAttachSharableVolumesResponse
from g42cloudsdkecs.v2.model.batch_create_server_tags_request import BatchCreateServerTagsRequest
from g42cloudsdkecs.v2.model.batch_create_server_tags_request_body import BatchCreateServerTagsRequestBody
from g42cloudsdkecs.v2.model.batch_create_server_tags_response import BatchCreateServerTagsResponse
from g42cloudsdkecs.v2.model.batch_delete_server_nic_option import BatchDeleteServerNicOption
from g42cloudsdkecs.v2.model.batch_delete_server_nics_request import BatchDeleteServerNicsRequest
from g42cloudsdkecs.v2.model.batch_delete_server_nics_request_body import BatchDeleteServerNicsRequestBody
from g42cloudsdkecs.v2.model.batch_delete_server_nics_response import BatchDeleteServerNicsResponse
from g42cloudsdkecs.v2.model.batch_delete_server_tags_request import BatchDeleteServerTagsRequest
from g42cloudsdkecs.v2.model.batch_delete_server_tags_request_body import BatchDeleteServerTagsRequestBody
from g42cloudsdkecs.v2.model.batch_delete_server_tags_response import BatchDeleteServerTagsResponse
from g42cloudsdkecs.v2.model.batch_reboot_servers_request import BatchRebootServersRequest
from g42cloudsdkecs.v2.model.batch_reboot_servers_request_body import BatchRebootServersRequestBody
from g42cloudsdkecs.v2.model.batch_reboot_servers_response import BatchRebootServersResponse
from g42cloudsdkecs.v2.model.batch_reboot_severs_option import BatchRebootSeversOption
from g42cloudsdkecs.v2.model.batch_reset_servers_password_request import BatchResetServersPasswordRequest
from g42cloudsdkecs.v2.model.batch_reset_servers_password_request_body import BatchResetServersPasswordRequestBody
from g42cloudsdkecs.v2.model.batch_reset_servers_password_response import BatchResetServersPasswordResponse
from g42cloudsdkecs.v2.model.batch_start_servers_option import BatchStartServersOption
from g42cloudsdkecs.v2.model.batch_start_servers_request import BatchStartServersRequest
from g42cloudsdkecs.v2.model.batch_start_servers_request_body import BatchStartServersRequestBody
from g42cloudsdkecs.v2.model.batch_start_servers_response import BatchStartServersResponse
from g42cloudsdkecs.v2.model.batch_stop_servers_option import BatchStopServersOption
from g42cloudsdkecs.v2.model.batch_stop_servers_request import BatchStopServersRequest
from g42cloudsdkecs.v2.model.batch_stop_servers_request_body import BatchStopServersRequestBody
from g42cloudsdkecs.v2.model.batch_stop_servers_response import BatchStopServersResponse
from g42cloudsdkecs.v2.model.batch_update_servers_name_request import BatchUpdateServersNameRequest
from g42cloudsdkecs.v2.model.batch_update_servers_name_request_body import BatchUpdateServersNameRequestBody
from g42cloudsdkecs.v2.model.batch_update_servers_name_response import BatchUpdateServersNameResponse
from g42cloudsdkecs.v2.model.block_device_attachable_quantity import BlockDeviceAttachableQuantity
from g42cloudsdkecs.v2.model.change_server_os_with_cloud_init_option import ChangeServerOsWithCloudInitOption
from g42cloudsdkecs.v2.model.change_server_os_with_cloud_init_request import ChangeServerOsWithCloudInitRequest
from g42cloudsdkecs.v2.model.change_server_os_with_cloud_init_request_body import ChangeServerOsWithCloudInitRequestBody
from g42cloudsdkecs.v2.model.change_server_os_with_cloud_init_response import ChangeServerOsWithCloudInitResponse
from g42cloudsdkecs.v2.model.change_server_os_without_cloud_init_option import ChangeServerOsWithoutCloudInitOption
from g42cloudsdkecs.v2.model.change_server_os_without_cloud_init_request import ChangeServerOsWithoutCloudInitRequest
from g42cloudsdkecs.v2.model.change_server_os_without_cloud_init_request_body import ChangeServerOsWithoutCloudInitRequestBody
from g42cloudsdkecs.v2.model.change_server_os_without_cloud_init_response import ChangeServerOsWithoutCloudInitResponse
from g42cloudsdkecs.v2.model.change_severs_os_metadata import ChangeSeversOsMetadata
from g42cloudsdkecs.v2.model.cpu_options import CpuOptions
from g42cloudsdkecs.v2.model.create_post_paid_servers_request import CreatePostPaidServersRequest
from g42cloudsdkecs.v2.model.create_post_paid_servers_request_body import CreatePostPaidServersRequestBody
from g42cloudsdkecs.v2.model.create_post_paid_servers_response import CreatePostPaidServersResponse
from g42cloudsdkecs.v2.model.create_server_group_option import CreateServerGroupOption
from g42cloudsdkecs.v2.model.create_server_group_request import CreateServerGroupRequest
from g42cloudsdkecs.v2.model.create_server_group_request_body import CreateServerGroupRequestBody
from g42cloudsdkecs.v2.model.create_server_group_response import CreateServerGroupResponse
from g42cloudsdkecs.v2.model.create_server_group_result import CreateServerGroupResult
from g42cloudsdkecs.v2.model.create_servers_request import CreateServersRequest
from g42cloudsdkecs.v2.model.create_servers_request_body import CreateServersRequestBody
from g42cloudsdkecs.v2.model.create_servers_response import CreateServersResponse
from g42cloudsdkecs.v2.model.delete_server_group_member_request import DeleteServerGroupMemberRequest
from g42cloudsdkecs.v2.model.delete_server_group_member_request_body import DeleteServerGroupMemberRequestBody
from g42cloudsdkecs.v2.model.delete_server_group_member_response import DeleteServerGroupMemberResponse
from g42cloudsdkecs.v2.model.delete_server_group_request import DeleteServerGroupRequest
from g42cloudsdkecs.v2.model.delete_server_group_response import DeleteServerGroupResponse
from g42cloudsdkecs.v2.model.delete_server_metadata_request import DeleteServerMetadataRequest
from g42cloudsdkecs.v2.model.delete_server_metadata_response import DeleteServerMetadataResponse
from g42cloudsdkecs.v2.model.delete_server_password_request import DeleteServerPasswordRequest
from g42cloudsdkecs.v2.model.delete_server_password_response import DeleteServerPasswordResponse
from g42cloudsdkecs.v2.model.delete_servers_request import DeleteServersRequest
from g42cloudsdkecs.v2.model.delete_servers_request_body import DeleteServersRequestBody
from g42cloudsdkecs.v2.model.delete_servers_response import DeleteServersResponse
from g42cloudsdkecs.v2.model.detach_server_volume_request import DetachServerVolumeRequest
from g42cloudsdkecs.v2.model.detach_server_volume_response import DetachServerVolumeResponse
from g42cloudsdkecs.v2.model.disassociate_server_virtual_ip_option import DisassociateServerVirtualIpOption
from g42cloudsdkecs.v2.model.disassociate_server_virtual_ip_request import DisassociateServerVirtualIpRequest
from g42cloudsdkecs.v2.model.disassociate_server_virtual_ip_request_body import DisassociateServerVirtualIpRequestBody
from g42cloudsdkecs.v2.model.disassociate_server_virtual_ip_response import DisassociateServerVirtualIpResponse
from g42cloudsdkecs.v2.model.flavor import Flavor
from g42cloudsdkecs.v2.model.flavor_extra_spec import FlavorExtraSpec
from g42cloudsdkecs.v2.model.flavor_link import FlavorLink
from g42cloudsdkecs.v2.model.get_server_remote_console_option import GetServerRemoteConsoleOption
from g42cloudsdkecs.v2.model.hypervisor import Hypervisor
from g42cloudsdkecs.v2.model.interface_attachable_quantity import InterfaceAttachableQuantity
from g42cloudsdkecs.v2.model.interface_attachment import InterfaceAttachment
from g42cloudsdkecs.v2.model.ipv6_bandwidth import Ipv6Bandwidth
from g42cloudsdkecs.v2.model.job_entities import JobEntities
from g42cloudsdkecs.v2.model.link import Link
from g42cloudsdkecs.v2.model.list_flavors_request import ListFlavorsRequest
from g42cloudsdkecs.v2.model.list_flavors_response import ListFlavorsResponse
from g42cloudsdkecs.v2.model.list_resize_flavors_request import ListResizeFlavorsRequest
from g42cloudsdkecs.v2.model.list_resize_flavors_response import ListResizeFlavorsResponse
from g42cloudsdkecs.v2.model.list_resize_flavors_result import ListResizeFlavorsResult
from g42cloudsdkecs.v2.model.list_server_block_devices_request import ListServerBlockDevicesRequest
from g42cloudsdkecs.v2.model.list_server_block_devices_response import ListServerBlockDevicesResponse
from g42cloudsdkecs.v2.model.list_server_groups_page_info_result import ListServerGroupsPageInfoResult
from g42cloudsdkecs.v2.model.list_server_groups_request import ListServerGroupsRequest
from g42cloudsdkecs.v2.model.list_server_groups_response import ListServerGroupsResponse
from g42cloudsdkecs.v2.model.list_server_groups_result import ListServerGroupsResult
from g42cloudsdkecs.v2.model.list_server_interfaces_request import ListServerInterfacesRequest
from g42cloudsdkecs.v2.model.list_server_interfaces_response import ListServerInterfacesResponse
from g42cloudsdkecs.v2.model.list_server_tags_request import ListServerTagsRequest
from g42cloudsdkecs.v2.model.list_server_tags_response import ListServerTagsResponse
from g42cloudsdkecs.v2.model.list_servers_details_request import ListServersDetailsRequest
from g42cloudsdkecs.v2.model.list_servers_details_response import ListServersDetailsResponse
from g42cloudsdkecs.v2.model.migrate_server_option import MigrateServerOption
from g42cloudsdkecs.v2.model.migrate_server_request import MigrateServerRequest
from g42cloudsdkecs.v2.model.migrate_server_request_body import MigrateServerRequestBody
from g42cloudsdkecs.v2.model.migrate_server_response import MigrateServerResponse
from g42cloudsdkecs.v2.model.nova_add_security_group_option import NovaAddSecurityGroupOption
from g42cloudsdkecs.v2.model.nova_associate_security_group_request import NovaAssociateSecurityGroupRequest
from g42cloudsdkecs.v2.model.nova_associate_security_group_request_body import NovaAssociateSecurityGroupRequestBody
from g42cloudsdkecs.v2.model.nova_associate_security_group_response import NovaAssociateSecurityGroupResponse
from g42cloudsdkecs.v2.model.nova_attach_interface_fixed_ip import NovaAttachInterfaceFixedIp
from g42cloudsdkecs.v2.model.nova_attach_interface_option import NovaAttachInterfaceOption
from g42cloudsdkecs.v2.model.nova_attach_interface_request import NovaAttachInterfaceRequest
from g42cloudsdkecs.v2.model.nova_attach_interface_request_body import NovaAttachInterfaceRequestBody
from g42cloudsdkecs.v2.model.nova_attach_interface_response import NovaAttachInterfaceResponse
from g42cloudsdkecs.v2.model.nova_availability_zone import NovaAvailabilityZone
from g42cloudsdkecs.v2.model.nova_availability_zone_state import NovaAvailabilityZoneState
from g42cloudsdkecs.v2.model.nova_create_keypair_option import NovaCreateKeypairOption
from g42cloudsdkecs.v2.model.nova_create_keypair_request import NovaCreateKeypairRequest
from g42cloudsdkecs.v2.model.nova_create_keypair_request_body import NovaCreateKeypairRequestBody
from g42cloudsdkecs.v2.model.nova_create_keypair_response import NovaCreateKeypairResponse
from g42cloudsdkecs.v2.model.nova_create_servers_option import NovaCreateServersOption
from g42cloudsdkecs.v2.model.nova_create_servers_request import NovaCreateServersRequest
from g42cloudsdkecs.v2.model.nova_create_servers_request_body import NovaCreateServersRequestBody
from g42cloudsdkecs.v2.model.nova_create_servers_response import NovaCreateServersResponse
from g42cloudsdkecs.v2.model.nova_create_servers_result import NovaCreateServersResult
from g42cloudsdkecs.v2.model.nova_create_servers_scheduler_hint import NovaCreateServersSchedulerHint
from g42cloudsdkecs.v2.model.nova_delete_keypair_request import NovaDeleteKeypairRequest
from g42cloudsdkecs.v2.model.nova_delete_keypair_response import NovaDeleteKeypairResponse
from g42cloudsdkecs.v2.model.nova_delete_server_request import NovaDeleteServerRequest
from g42cloudsdkecs.v2.model.nova_delete_server_response import NovaDeleteServerResponse
from g42cloudsdkecs.v2.model.nova_disassociate_security_group_request import NovaDisassociateSecurityGroupRequest
from g42cloudsdkecs.v2.model.nova_disassociate_security_group_request_body import NovaDisassociateSecurityGroupRequestBody
from g42cloudsdkecs.v2.model.nova_disassociate_security_group_response import NovaDisassociateSecurityGroupResponse
from g42cloudsdkecs.v2.model.nova_keypair import NovaKeypair
from g42cloudsdkecs.v2.model.nova_keypair_detail import NovaKeypairDetail
from g42cloudsdkecs.v2.model.nova_link import NovaLink
from g42cloudsdkecs.v2.model.nova_list_availability_zones_request import NovaListAvailabilityZonesRequest
from g42cloudsdkecs.v2.model.nova_list_availability_zones_response import NovaListAvailabilityZonesResponse
from g42cloudsdkecs.v2.model.nova_list_keypairs_request import NovaListKeypairsRequest
from g42cloudsdkecs.v2.model.nova_list_keypairs_response import NovaListKeypairsResponse
from g42cloudsdkecs.v2.model.nova_list_keypairs_result import NovaListKeypairsResult
from g42cloudsdkecs.v2.model.nova_list_server_security_groups_request import NovaListServerSecurityGroupsRequest
from g42cloudsdkecs.v2.model.nova_list_server_security_groups_response import NovaListServerSecurityGroupsResponse
from g42cloudsdkecs.v2.model.nova_list_servers_details_request import NovaListServersDetailsRequest
from g42cloudsdkecs.v2.model.nova_list_servers_details_response import NovaListServersDetailsResponse
from g42cloudsdkecs.v2.model.nova_network import NovaNetwork
from g42cloudsdkecs.v2.model.nova_remove_security_group_option import NovaRemoveSecurityGroupOption
from g42cloudsdkecs.v2.model.nova_security_group import NovaSecurityGroup
from g42cloudsdkecs.v2.model.nova_security_group_common_group import NovaSecurityGroupCommonGroup
from g42cloudsdkecs.v2.model.nova_security_group_common_ip_range import NovaSecurityGroupCommonIpRange
from g42cloudsdkecs.v2.model.nova_security_group_common_rule import NovaSecurityGroupCommonRule
from g42cloudsdkecs.v2.model.nova_server import NovaServer
from g42cloudsdkecs.v2.model.nova_server_block_device_mapping import NovaServerBlockDeviceMapping
from g42cloudsdkecs.v2.model.nova_server_fault import NovaServerFault
from g42cloudsdkecs.v2.model.nova_server_flavor import NovaServerFlavor
from g42cloudsdkecs.v2.model.nova_server_image import NovaServerImage
from g42cloudsdkecs.v2.model.nova_server_interface_detail import NovaServerInterfaceDetail
from g42cloudsdkecs.v2.model.nova_server_interface_fixed_ip import NovaServerInterfaceFixedIp
from g42cloudsdkecs.v2.model.nova_server_network import NovaServerNetwork
from g42cloudsdkecs.v2.model.nova_server_scheduler_hints import NovaServerSchedulerHints
from g42cloudsdkecs.v2.model.nova_server_security_group import NovaServerSecurityGroup
from g42cloudsdkecs.v2.model.nova_server_volume import NovaServerVolume
from g42cloudsdkecs.v2.model.nova_show_keypair_request import NovaShowKeypairRequest
from g42cloudsdkecs.v2.model.nova_show_keypair_response import NovaShowKeypairResponse
from g42cloudsdkecs.v2.model.nova_show_server_request import NovaShowServerRequest
from g42cloudsdkecs.v2.model.nova_show_server_response import NovaShowServerResponse
from g42cloudsdkecs.v2.model.nova_simple_keypair import NovaSimpleKeypair
from g42cloudsdkecs.v2.model.page_link import PageLink
from g42cloudsdkecs.v2.model.post_paid_server import PostPaidServer
from g42cloudsdkecs.v2.model.post_paid_server_data_volume import PostPaidServerDataVolume
from g42cloudsdkecs.v2.model.post_paid_server_data_volume_extend_param import PostPaidServerDataVolumeExtendParam
from g42cloudsdkecs.v2.model.post_paid_server_data_volume_metadata import PostPaidServerDataVolumeMetadata
from g42cloudsdkecs.v2.model.post_paid_server_eip import PostPaidServerEip
from g42cloudsdkecs.v2.model.post_paid_server_eip_bandwidth import PostPaidServerEipBandwidth
from g42cloudsdkecs.v2.model.post_paid_server_eip_extend_param import PostPaidServerEipExtendParam
from g42cloudsdkecs.v2.model.post_paid_server_extend_param import PostPaidServerExtendParam
from g42cloudsdkecs.v2.model.post_paid_server_ipv6_bandwidth import PostPaidServerIpv6Bandwidth
from g42cloudsdkecs.v2.model.post_paid_server_nic import PostPaidServerNic
from g42cloudsdkecs.v2.model.post_paid_server_publicip import PostPaidServerPublicip
from g42cloudsdkecs.v2.model.post_paid_server_root_volume import PostPaidServerRootVolume
from g42cloudsdkecs.v2.model.post_paid_server_root_volume_extend_param import PostPaidServerRootVolumeExtendParam
from g42cloudsdkecs.v2.model.post_paid_server_scheduler_hints import PostPaidServerSchedulerHints
from g42cloudsdkecs.v2.model.post_paid_server_security_group import PostPaidServerSecurityGroup
from g42cloudsdkecs.v2.model.post_paid_server_tag import PostPaidServerTag
from g42cloudsdkecs.v2.model.pre_paid_server import PrePaidServer
from g42cloudsdkecs.v2.model.pre_paid_server_data_volume import PrePaidServerDataVolume
from g42cloudsdkecs.v2.model.pre_paid_server_data_volume_extend_param import PrePaidServerDataVolumeExtendParam
from g42cloudsdkecs.v2.model.pre_paid_server_data_volume_metadata import PrePaidServerDataVolumeMetadata
from g42cloudsdkecs.v2.model.pre_paid_server_eip import PrePaidServerEip
from g42cloudsdkecs.v2.model.pre_paid_server_eip_bandwidth import PrePaidServerEipBandwidth
from g42cloudsdkecs.v2.model.pre_paid_server_eip_extend_param import PrePaidServerEipExtendParam
from g42cloudsdkecs.v2.model.pre_paid_server_extend_param import PrePaidServerExtendParam
from g42cloudsdkecs.v2.model.pre_paid_server_ipv6_bandwidth import PrePaidServerIpv6Bandwidth
from g42cloudsdkecs.v2.model.pre_paid_server_nic import PrePaidServerNic
from g42cloudsdkecs.v2.model.pre_paid_server_publicip import PrePaidServerPublicip
from g42cloudsdkecs.v2.model.pre_paid_server_root_volume import PrePaidServerRootVolume
from g42cloudsdkecs.v2.model.pre_paid_server_root_volume_extend_param import PrePaidServerRootVolumeExtendParam
from g42cloudsdkecs.v2.model.pre_paid_server_scheduler_hints import PrePaidServerSchedulerHints
from g42cloudsdkecs.v2.model.pre_paid_server_security_group import PrePaidServerSecurityGroup
from g42cloudsdkecs.v2.model.pre_paid_server_tag import PrePaidServerTag
from g42cloudsdkecs.v2.model.project_flavor_limit import ProjectFlavorLimit
from g42cloudsdkecs.v2.model.project_tag import ProjectTag
from g42cloudsdkecs.v2.model.register_server_auto_recovery_request import RegisterServerAutoRecoveryRequest
from g42cloudsdkecs.v2.model.register_server_auto_recovery_request_body import RegisterServerAutoRecoveryRequestBody
from g42cloudsdkecs.v2.model.register_server_auto_recovery_response import RegisterServerAutoRecoveryResponse
from g42cloudsdkecs.v2.model.register_server_monitor_request import RegisterServerMonitorRequest
from g42cloudsdkecs.v2.model.register_server_monitor_request_body import RegisterServerMonitorRequestBody
from g42cloudsdkecs.v2.model.register_server_monitor_response import RegisterServerMonitorResponse
from g42cloudsdkecs.v2.model.reinstall_server_with_cloud_init_option import ReinstallServerWithCloudInitOption
from g42cloudsdkecs.v2.model.reinstall_server_with_cloud_init_request import ReinstallServerWithCloudInitRequest
from g42cloudsdkecs.v2.model.reinstall_server_with_cloud_init_request_body import ReinstallServerWithCloudInitRequestBody
from g42cloudsdkecs.v2.model.reinstall_server_with_cloud_init_response import ReinstallServerWithCloudInitResponse
from g42cloudsdkecs.v2.model.reinstall_server_without_cloud_init_option import ReinstallServerWithoutCloudInitOption
from g42cloudsdkecs.v2.model.reinstall_server_without_cloud_init_request import ReinstallServerWithoutCloudInitRequest
from g42cloudsdkecs.v2.model.reinstall_server_without_cloud_init_request_body import ReinstallServerWithoutCloudInitRequestBody
from g42cloudsdkecs.v2.model.reinstall_server_without_cloud_init_response import ReinstallServerWithoutCloudInitResponse
from g42cloudsdkecs.v2.model.reinstall_sever_metadata import ReinstallSeverMetadata
from g42cloudsdkecs.v2.model.reset_server_password_option import ResetServerPasswordOption
from g42cloudsdkecs.v2.model.reset_server_password_request import ResetServerPasswordRequest
from g42cloudsdkecs.v2.model.reset_server_password_request_body import ResetServerPasswordRequestBody
from g42cloudsdkecs.v2.model.reset_server_password_response import ResetServerPasswordResponse
from g42cloudsdkecs.v2.model.resize_post_paid_server_option import ResizePostPaidServerOption
from g42cloudsdkecs.v2.model.resize_post_paid_server_request import ResizePostPaidServerRequest
from g42cloudsdkecs.v2.model.resize_post_paid_server_request_body import ResizePostPaidServerRequestBody
from g42cloudsdkecs.v2.model.resize_post_paid_server_response import ResizePostPaidServerResponse
from g42cloudsdkecs.v2.model.resize_pre_paid_server_option import ResizePrePaidServerOption
from g42cloudsdkecs.v2.model.resize_server_extend_param import ResizeServerExtendParam
from g42cloudsdkecs.v2.model.resize_server_request import ResizeServerRequest
from g42cloudsdkecs.v2.model.resize_server_request_body import ResizeServerRequestBody
from g42cloudsdkecs.v2.model.resize_server_response import ResizeServerResponse
from g42cloudsdkecs.v2.model.server_address import ServerAddress
from g42cloudsdkecs.v2.model.server_attachable_quantity import ServerAttachableQuantity
from g42cloudsdkecs.v2.model.server_block_device import ServerBlockDevice
from g42cloudsdkecs.v2.model.server_detail import ServerDetail
from g42cloudsdkecs.v2.model.server_extend_volume_attachment import ServerExtendVolumeAttachment
from g42cloudsdkecs.v2.model.server_fault import ServerFault
from g42cloudsdkecs.v2.model.server_flavor import ServerFlavor
from g42cloudsdkecs.v2.model.server_group_member import ServerGroupMember
from g42cloudsdkecs.v2.model.server_id import ServerId
from g42cloudsdkecs.v2.model.server_image import ServerImage
from g42cloudsdkecs.v2.model.server_interface_fixed_ip import ServerInterfaceFixedIp
from g42cloudsdkecs.v2.model.server_limits import ServerLimits
from g42cloudsdkecs.v2.model.server_nic_security_group import ServerNicSecurityGroup
from g42cloudsdkecs.v2.model.server_remote_console import ServerRemoteConsole
from g42cloudsdkecs.v2.model.server_scheduler_hints import ServerSchedulerHints
from g42cloudsdkecs.v2.model.server_security_group import ServerSecurityGroup
from g42cloudsdkecs.v2.model.server_system_tag import ServerSystemTag
from g42cloudsdkecs.v2.model.server_tag import ServerTag
from g42cloudsdkecs.v2.model.show_job_request import ShowJobRequest
from g42cloudsdkecs.v2.model.show_job_response import ShowJobResponse
from g42cloudsdkecs.v2.model.show_reset_password_flag_request import ShowResetPasswordFlagRequest
from g42cloudsdkecs.v2.model.show_reset_password_flag_response import ShowResetPasswordFlagResponse
from g42cloudsdkecs.v2.model.show_server_auto_recovery_request import ShowServerAutoRecoveryRequest
from g42cloudsdkecs.v2.model.show_server_auto_recovery_response import ShowServerAutoRecoveryResponse
from g42cloudsdkecs.v2.model.show_server_block_device_request import ShowServerBlockDeviceRequest
from g42cloudsdkecs.v2.model.show_server_block_device_response import ShowServerBlockDeviceResponse
from g42cloudsdkecs.v2.model.show_server_group_request import ShowServerGroupRequest
from g42cloudsdkecs.v2.model.show_server_group_response import ShowServerGroupResponse
from g42cloudsdkecs.v2.model.show_server_group_result import ShowServerGroupResult
from g42cloudsdkecs.v2.model.show_server_limits_request import ShowServerLimitsRequest
from g42cloudsdkecs.v2.model.show_server_limits_response import ShowServerLimitsResponse
from g42cloudsdkecs.v2.model.show_server_password_request import ShowServerPasswordRequest
from g42cloudsdkecs.v2.model.show_server_password_response import ShowServerPasswordResponse
from g42cloudsdkecs.v2.model.show_server_remote_console_request import ShowServerRemoteConsoleRequest
from g42cloudsdkecs.v2.model.show_server_remote_console_request_body import ShowServerRemoteConsoleRequestBody
from g42cloudsdkecs.v2.model.show_server_remote_console_response import ShowServerRemoteConsoleResponse
from g42cloudsdkecs.v2.model.show_server_request import ShowServerRequest
from g42cloudsdkecs.v2.model.show_server_response import ShowServerResponse
from g42cloudsdkecs.v2.model.show_server_tags_request import ShowServerTagsRequest
from g42cloudsdkecs.v2.model.show_server_tags_response import ShowServerTagsResponse
from g42cloudsdkecs.v2.model.simple_flavor import SimpleFlavor
from g42cloudsdkecs.v2.model.sub_job import SubJob
from g42cloudsdkecs.v2.model.sub_job_entities import SubJobEntities
from g42cloudsdkecs.v2.model.update_server_address import UpdateServerAddress
from g42cloudsdkecs.v2.model.update_server_auto_terminate_time_request import UpdateServerAutoTerminateTimeRequest
from g42cloudsdkecs.v2.model.update_server_auto_terminate_time_request_body import UpdateServerAutoTerminateTimeRequestBody
from g42cloudsdkecs.v2.model.update_server_auto_terminate_time_response import UpdateServerAutoTerminateTimeResponse
from g42cloudsdkecs.v2.model.update_server_metadata_request import UpdateServerMetadataRequest
from g42cloudsdkecs.v2.model.update_server_metadata_request_body import UpdateServerMetadataRequestBody
from g42cloudsdkecs.v2.model.update_server_metadata_response import UpdateServerMetadataResponse
from g42cloudsdkecs.v2.model.update_server_option import UpdateServerOption
from g42cloudsdkecs.v2.model.update_server_request import UpdateServerRequest
from g42cloudsdkecs.v2.model.update_server_request_body import UpdateServerRequestBody
from g42cloudsdkecs.v2.model.update_server_response import UpdateServerResponse
from g42cloudsdkecs.v2.model.update_server_result import UpdateServerResult

