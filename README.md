# maendeleolab_subnet
![GitHub commit activity](https://img.shields.io/github/last-commit/maendeleolab/maendeleolab_internetGateway)

<img src="/images/banner.png" width=400>

```
├── build_igw.py
├── delete_resources.py
├── deploy_NetworkDev1.py
├── maendeleolab_lib.py
└── igw.log
```

## [Context](#Context)

- This repo was built to create an internet gateway for a VPC. 

- It can be used on any Linux environment in AWS or on-premises. 

- Install Python 3.6.9 (or higher) and awscli version 2.

- The scripts are idempotent.

- The line above means, if the resource is tagged with a name that already exists, it will not create another one.

## [Prerequisites](#Prerequisites)

- Please watch the [requirements steps](https://www.youtube.com/watch?v=gMM-d1uZ0Ks&t=12s)

- Clone [maendeleolab_vpc](https://github.com/maendeleolab/maendeleolab_vpc)

- It helps to be familiar with Linux basics commands.

- Must have awscli version 2 and Python 3.6.9 (or higher) installed.

- I recommend dedicating an instance (or on-premises server) to programmatically run the scripts.  

- Assign a role with programmatic access to the instance/server default profile.

- Run this command 'export ENV_FPATH="folder-path" ' 

- Replace folder-path with your folder location (this is the folder, where you will download the repo). 

See the example below.

```
export ENV_FPATH="/home/ubuntu"
```

## [Walk-through](#Walk-through)

Watch [tutorial](Coming Soon) on youtube for step by step instructions.

**1**  - Make sure to comply with the prerequisites mentioned above.

**2**  - Update and install the latest packages of your Linux distribution system.

**3**  - Clone this repo to the instance/server using the syntax below.

```
git clone https://github.com/maendeleolab/maendeleolab_internetGateway.git
```

**4**  - cd to folder maendeleolab_internetGateway

```
cd maendeleolab_internetGateway
```

**5**  - List the files in the folder with the **ls** command. It should match the files below.

**Note:** A file named **igw.log** will be created to store the scripts logs, when you run the script for the first time.

Remember to use it to monitor your environment or troubleshoot an issue.

```
README.md
LICENSE
images
build_igw.py
delete_resources.py
deploy_NetworkDev1.py
maendeleolab_lib.py
```

**6**  - I recommend running the script **NetworkDev1.py** to see what the expected results look like.

**Notes: Your VPC must be tagged with the name "NetworkDev1" for the script to work, otherwise replace NetworkDev1 with your VPC name.**

The script will create an internet gateway in us-east-1 and us-east-2 regions.

This script will become your single source of truth for your internet gateways. 

```
./NetworkDev1.py or python3 NetworkDev1.py
```

**7**  - Verify the expected results are present in the VPC console. 

**8**  - Run the script again to verify idempotency is working as expected. 

**9**  - Internet gateway resources do not cost you anything, but in case you decide to delete them. You can run the script **delete_resources.py**
	
**Note:** The script deletes all the internet gateway resources that do not have any dependencies. 
	
This means, if internet gateway is not associated to a VPC route table, the subnets will be deleted. 

```
./delete_resources.py or python3 delete_resources.py
```

**11** - If you get to this step, congratulations for being brave to do it! 

## [Support](#Support)
If you find this script useful, please support it with a shout out on your favorite social media platform!

![Twitter](https://img.shields.io/twitter/follow/maendeleolab?style=social)
```
Twitter : @maendeleolab
Instagram : @maendeleolab
TitTok : @pat_maendeleolab
```
## [License](#License)
GNU GENERAL PUBLIC LICENSE

	
