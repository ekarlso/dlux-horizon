BRIDGE = {"table": {"headers": {
    "uuid": "UUID",
    "name": "Name",
    "ports": "Ports",
    "mirrors": "Mirrors",
    "controller": "Controller",
    "datapath_id": "DPID",
    "datapath_type": "Datapath Type",
    "sflow": "sFlow",
    "netflow": "NetFlow",
    "protocols": "Protocols",
    "status": "Status",
    "stp_enable": "STP Enable",
    "other_config": "Other Config",
    "external_ids": "External IDs",
    "columns": "Columns",
}}}

OVS = {"table": {"headers": {
    "bridges": "Bridges",
    "ssl": "SSL",
    "next_cfg": "Next Config",
    "curr_cfg": "Current Config",
    "statistics": "Statistics",
    "ovs_version": "OVS Version",
    "db_version": "DB Version",
    "system_type": "System Type",
    "system_version": "System Version",
    "manager_options": "Manager Options",
    "other_config": "Other Config",
    "external_ids": "External IDs",
}}}

PORT = {"table": {"headers": {
    "name": "Name",
    "interfaces": "Interfaces",
    "vlan_mode": "VLAN Mode",
    "native-untagged": "Native VLAN",
    "tag": "Tag",
    "trunks": "Trunks",
    "other_config": "Other Config",
    "bond_mode": "Bond Mode",
    "bond_updelay": "Bond Up Delay",
    "bond_downdelay": "Bond Down Delay",
    "lacp": "LACP ",
    "bond_fake_iface": "Bond Fake Interface",
    "qos": "QiS",
    "mac": "MAC",
    "fake_bridge": "Fake Bridge",
    "status": "Status"
}}}

INTERFACE = {"table": {"headers": {
    "name": "Name",
    "ifindex": "ifindex",
    "mac_in_use": "MAC in Use?",
    "mac": "MAC",
    "ofport": "OF Port",
    "ofport_request": "OF Port Request",
    "type": "Type",
    "options": "Options",
    "admin_state": "Admin State",
    "link_state": "Link State",
    "link_resets": "Link Resets",
    "link_speed": "Link Speed",
    "duplex": "Duplex",
    "mtu": "MTU",
    "lacp_current": "LACP Current",
    "status": "Status",
    "statistics": "Statistics",
    "ingress_policing_rate": "Ingress Policing Rate",
    "ingress_policing_burst": "Ingress Policing Burst",
    "bfd": "BFD",
    "bfd_status": "BFD Status",
    "cfm_mpid": "CFM MPID",
    "cfm_fault": "CFM Fault",
    "cfm_fault_status": "CFM Fault Status",
    "cfm_remote_opstate": "CFM Remote Op State",
    "cfm_health": "CFM Health",
    "cfm_remote_mpids": "CFM Remote MPIDs",
    "other_config": "Other Config",
    "external_ids": "External IDs",
}}}

FLOW_TABLE = {"table": {"headers": {
    "name": "Name",
    "flow_limit": "Flow Limit",
    "overflow_policy": "Overflow Policy",
    "groups": "Groups",
}}}

QOS = {"table": {"headers": {
    "type": "Type",
    "queues": "Queues",
    "other_config ": "Other Config",
    "external_ids ": "External IDs",
}}}

QUEUE = {"table": {"headers": {
    "dscp": "DSCP",
    "other_config": "Other Config",
    "external_ids": "External IDs",
}}}

MIRROR = {"table": {"headers": {
    "name": "Name",
    "select_all": "Select All",
    "select_dst_port ": "Select Source Port",
    "select_src_port": "Select Destination Port",
    "select_vlan": "Select Vlan",
    "output_port": "Output Port",
    "output_vlan": "Output VLAN",
    "statistics": "Statistics",
    "external_ids": "External IDs"
}}}

CONTROLLER = {"table": {"headers": {
    "target ": "Target",
    "connection_mode": "Connection Mode",
    "max_backoff": "Max. Backoff",
    "inactivity_probe": "Inactivity Probe",
    "enable_async_messages": "Enable Async Messages",
    "controller_rate_limit": "Controller Rate Limit",
    "controller_burst_limit": "Controller Burst Limit",
    "local_ip": "Local IP",
    "local_netmask": "Local Netmask",
    "local_gateway": "Local Gateway",
    "is_connected": "Connected",
    "role": "Role",
    "status": "Status",
    "other_config": "Other Config",
    "external_ids": "External IDs",
}}}

MANAGER = {"table": {"headers": {
    "target": "Target",
    "connection_mode": "Connection Mode",
    "max_backoff": "Max. Backoff",
    "inactivity_probe": "Inactivity Probe",
    "is_connected": "Connected",
    "status": "Status",
    "external_ids": "External IDs",
    "other_config": "Other Config",
}}}

NETFLOW = {"table": {"headers": {
    "targets": "Targets",
    "engine_id": "Engine ID",
    "engine_type": "Engine Type",
    "active_timeout": "Active Timeout",
    "add_id_to_interface": "Add ID to Interface",
    "external_ids": "External IDs",
}}}

SSL = {"table": {"headers": {
    "private_key": "Private Key",
    "certificate": "Certificate",
    "ca_cert": "CA Cert",
    "bootstrap_ca_cert": "Bootstrap CA Cert",
    "external_ids": "External IDs",
}}}

SFLOW = {"table": {"headers": {
    "agent": "Agent",
    "header": "Header",
    "polling": "Polling",
    "sampling": "Sampling",
    "targets": "Targets",
    "external_ids": "External IDs",
}}}

IPFIX = {"table": {"headers": {
    "targets": "Targets",
    "sampling": "Sampling",
    "obs_domain_id": "Obs Domain ID",
    "obs_point_id": "Obs Point Id",
    "cache_active_timeout": "Cache Active Timeout",
    "cache_max_flows": "Cache Max Flows",
    "external_ids": "External IDs",
}}}

FLOW_SET = {"table": {"headers": {
    "id": "ID",
    "bridge": "Bridge",
    "ipfix": "IPFIX",
    "external_ids": "External IDs",
}}}

TABLES = {"open_vswitch": OVS,
          "bridge": BRIDGE,
          "port": PORT,
          "interface": INTERFACE,
          "flow_table": FLOW_TABLE,
          "qos": QOS,
          "queue": QUEUE,
          "mirror": MIRROR,
          "controller": CONTROLLER,
          "manager": MANAGER,
          "netflow": NETFLOW,
          "ssl": SSL,
          "sflow": SFLOW,
          "ipfix": IPFIX,
          "flow_sample_collector_set": FLOW_SET,
}

