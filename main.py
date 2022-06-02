import boto3
import sys
from datetime import datetime, timedelta
import credentials
import slack

queue_name = credentials.sqs_queue_name
success = slack.success_message
failure = slack.failure_message

client = boto3.client(
    'cloudwatch',
    region_name=credentials.region,
    aws_access_key_id=credentials.key_id,
    aws_secret_access_key=credentials.access_key
)

response = client.get_metric_statistics(
    Namespace='AWS/SQS',
    MetricName='ApproximateNumberOfMessagesVisible',
    Dimensions=[
        {
            'Name': 'QueueName',
            'Value': queue_name
        }
    ],
    StartTime=datetime.utcnow() - timedelta(seconds=60),
    EndTime=datetime.utcnow(),
    Period=60,
    Statistics=[
        'Sum'
    ]
)

datapoint = response['Datapoints']
for item in datapoint:
    message_count = int(item['Sum'])
    if message_count == 0:
        slack.post_message_to_slack(success)
    else:
        slack.post_message_to_slack(failure)
    print(f'Message count in the queue:{message_count}')

sys.exit(0)
