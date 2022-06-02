import os

region = os.getenv('AWS_REGION')
key_id = os.getenv('AWS_ACCESS_KEY_ID')
access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
slack_token = os.getenv('SLACK_TOKEN')
sqs_queue_name = os.getenv('QUEUE_NAME')
slack_channel_id = os.getenv('SLACK_CHANNEL_ID')