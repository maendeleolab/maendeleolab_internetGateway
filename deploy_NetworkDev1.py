#!/usr/bin/env python3

from maendeleolab_lib import *

maendeleolab_infra = [
                'us-east-1',
                'us-west-2',
               ]

internet_gw1 = "NetworkDev1"

for region in (maendeleolab_infra):
	#creates internet gateway
	make_igw(
            Vpc_name=internet_gw1,
            Igw_name=internet_gw1,
            Tag_key="Type",
            Tag_value="not-billable",
            Region=region
        )
        #Associates internet gateway to vpc
	make_association(
            Vpc_name=internet_gw1,
            Vpc_Id=build_vpc.get_VpcId(internet_gw1,region),
            Igw_Id=get_IgwId(internet_gw1,region),
            Igw_name=internet_gw1,
            Region=region
        )

# ----------------------- End ------------------------
