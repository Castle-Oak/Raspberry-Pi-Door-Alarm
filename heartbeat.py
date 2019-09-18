import boto3
import json

client = boto3.client('cloudwatch')
client.put_metric_data(Namespace='is_alive',MetricData=[{'MetricName':'DoorAlarm','Value': 1}])
