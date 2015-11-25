import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError
import sys
import requests

# Get the keys from a specific url and then use them to connect to AWS Service
response = requests.get("http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key").text
key = response.split(":")
access_key_id = key[0]
secret_access_key = key[1]

# Set up a connection to the AWS service. 
conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

my_queue = conn.get_queue(sys.argv[1])
print "Messages in the queue = " + str(my_queue.count())
