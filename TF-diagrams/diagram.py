from diagrams import Diagram,Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.aws.network import VPC
from diagrams.aws.network import PrivateSubnet
from diagrams.aws.network import PublicSubnet
from diagrams.aws.database import RDS
with Diagram("EX", show=False):
    with Cluster("VPC"):
        with Cluster("VPC"):
            vpc = VPC("vpc")
        with Cluster("Subnet-1"):
            ec2 = EC2("EC2_1")
            vpc >> EC2("EC2_2")
            vpc >> ec2
            ec2-RDS("RDS")
        with Cluster("Subnet-2"):
            vpc >> EC2("EC2_3")
