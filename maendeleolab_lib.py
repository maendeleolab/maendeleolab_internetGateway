#!/usr/bin/env python3


import os, sys, pprint
from build_igw import region_id, make_igw, get_IgwId, make_association
from build_igw import destroy_igw, erase_igw, remove_association
FPATH = os.environ.get('ENV_FPATH') #ENV_FPATH should be set in your environment variable file
sys.path.append(FPATH+'/maendeleolab_vpc')
import build_vpc

# ----------------------- End --------------------------
