#!/usr/bin/env python3

Goal = '''
to create an internet gateway for vpc
Author: Pat@Maendeleolab
'''

#Module imports
import logging, sys, os, json
from datetime import datetime
from time import sleep

#Path to local home and user folder
FPATH = os.environ.get('ENV_FPATH')

#logging
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p ',\
                        filename=FPATH+'/maendeleolab_internetGateway/igw.log', level=logging.INFO)

#adding flexibility for regions
def region_id(name='us-east-1'):
		return name # e.g: 'us-east-1'

#verifying if the internet gateway exist already
def verify_igw(igw_name, region='us-east-1'):
	''' Verifies if Internet Gateway name already exists '''
	try:
		output = os.popen('aws ec2 describe-internet-gateways --filters Name=tag:Name,Values=' + igw_name + ' --region '+ region).read()
		igw_data = json.loads(str(output))
		if len(igw_data['InternetGateways']) > 0:
			print(f'{igw_name} already exists in {region}...')
			return 1
	except Exception as err:
		logging.info(f'{err} happened in verify_igw() in {region}...')
		print(f'Logging "verify_igw()" error in igw.log in {region}...')

#create internet gateway
def make_igw(**kwargs):
	''' Creates internet gateway if it doesn't exist yet'''
	try:
		if verify_igw(kwargs['Igw_name'],kwargs['Region']) == 1:
			pass
		else:
			os.system("aws ec2 create-internet-gateway \
				--tag-specifications 'ResourceType=internet-gateway,Tags=[{Key=Name,Value=" + kwargs['Igw_name'] + "},\
									  {Key=" + kwargs['Tag_key'] + ",Value=" + kwargs['Tag_value'] + "}]'\
				--region " + kwargs['Region']
			)
			logging.info(f'Created IGW: {kwargs["Igw_name"]} in {kwargs["Region"]}...')
			print(f'Created IGW: {kwargs["Igw_name"]} in {kwargs["Region"]}...')
	except Exception as err:
		logging.info(f'{err} happened in make_igw() in {kwargs["Region"]}...')
		print(f'Logging "make_igw()" error to igw.log in {kwargs["Region"]}...')

#return internet gateway ID
def get_IgwId(Igw_name, region='us-east-1'):
	''' Gets resource id from json output and can be used in deploy scripts '''
	try:
		output = os.popen('aws ec2 describe-internet-gateways --filters Name=tag:Name,Values=' + Igw_name + ' --region '+ region).read()
		igw_data = json.loads(str(output))
		data = igw_data['InternetGateways']
		for item in data:
			return item['InternetGatewayId']
	except Exception as err:
		logging.info(f'{err} happened in get_IgwId() in {region}...')
		print(f'Logging "get_IgwId()" error in igw.log in {region}...')

#attach internet gateway to VPC
def make_association(**kwargs):
	try:
		os.system("aws ec2 attach-internet-gateway \
					--internet-gateway-id " + kwargs['Igw_Id'] + \
					" --vpc-id "  + kwargs['Vpc_Id'] +	\
					" --region " + kwargs['Region']
		)
		logging.info(f'Created igw association for: {kwargs["Vpc_name"]} in {kwargs["Region"]}...')
		print(f'Created igw association for: {kwargs["Vpc_name"]} in {kwargs["Region"]}...')
	except Exception as err:
		logging.info(f'{err} happened in make_association() in {kwargs["Region"]}...')
		print(f'Logging "make_association()" error in igw.log in {kwargs["Region"]}...')
	
#detach internet gateway from VPC
def remove_association(**kwargs):
	try:
		os.system("aws ec2 detach-internet-gateway \
					--internet-gateway-id " + kwargs['Igw_Id'] + \
					" --vpc-id " + kwargs['Vpc_Id'] + \
					" --region " + kwargs['Region'] 
		)
		logging.info('Removed igw association for {kwargs["Vpc_name"]} in {kwargs["Region"]}...')
		print(f'Removed igw association for {kwargs["Vpc_name"]} in {kwargs["Region"]}...')
	except Exception as err:
		logging.info(f'{err} happened in remove_association() in {kwargs["Region"]}...')
		print(f'Logging "remove_association()" error to igw.log in {kwargs["Region"]}...')

#delete internet gateway
def destroy_igw(Igw_Id, region='us-east-1'):
	try:
		os.system("aws ec2 delete-internet-gateway --internet-gateway-id " + Igw_Id + " --region " +region)
		logging.info(f'Deleted IGW Id: {Igw_Id} in region: {region}...')
		print(f'Deleted IGW Id: {Igw_Id} in region: {region}...')
	except Exception as err:
		logging.info(f'{err} happened in destroy_igw() in {region}...')
		print(f'Logging "destroy_igw()" to igw.log in {region}...')

#remove all internet gateways that do not have any dependencies
def erase_igw(region='us-east-1'):
	try:
		''' Deletes all Internet Gateways that are not tagged with "do-not-delete" '''
		output = os.popen('aws ec2 describe-internet-gateways  --region ' + region).read()
		igw_data = json.loads(str(output))
		for data in igw_data['InternetGateways']:
			destroy_igw(data['InternetGatewayId'], region=region)
			logging.info('Logging erase_igw: ' + data['InternetGatewayId'] + ' in region: '+ region)
			print(f'Logging erase_igw: {data["InternetGatewayId"]} in region: {region}...')
	except Exception as err:
		logging.info(f'{err} happened in erase_igw() in {region}...')
		print(f'Logging "erase_igw()" error to igw.log in {region}...')
# ------------------------------- End ---------------------------------

