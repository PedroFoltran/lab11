import requests
import boto

response = requests.get('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key').text
keys = response.split(":")

print keys[0]
print keys[1]
print boto.Version
