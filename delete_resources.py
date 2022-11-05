#!/usr/bin/env python3

from maendeleolab_lib import *

maendeleolab_infra=[
        'us-east-1',
        'us-west-2'
        ]

maendeleolab_vpcs=[
        'NetworkDev1',
        ]

#detach internet gateways associations from VPCs
for vpc in maendeleolab_vpcs:
        remove_association(
                Igw_Id=get_IgwId(vpc,'us-east-1'),
                Vpc_Id=build_vpc.get_VpcId(vpc,'us-east-1'),
                Region='us-east-1',
                Vpc_name=vpc,
        )
        remove_association(
                Igw_Id=get_IgwId(vpc,'us-west-2'),
                Vpc_Id=build_vpc.get_VpcId(vpc,'us-west-2'),
                Region='us-west-2',
                Vpc_name=vpc,
        )

#delete internet gateway
for region in maendeleolab_infra:
	erase_igw(region)

# ------------------ End ------------------
