import json
import requests
import credentials

slack_token = credentials.slack_token
slack_channel = credentials.slack_channel_id
slack_icon_url = 'https://zappysys.com/blog/wp-content/uploads/2019/08/amazon-sqs_512.png'
slack_user_name = 'SQS Queue Alert Manager'
slack_text = ''

# slack_blocks = [{
#   "type": "header",
#   "text": {
#     "type": "plain_text",
#     "text": "ALERT",
#     }
# }]
success_message = [
  {
    "mrkdwn_in": [
        "text"
    ],
    "color": "good",
    # "pretext": "Optional pre-text that appears above the attachment block",
    "author_name": "AWS Queue Monitoring",
    "author_icon": slack_icon_url,
    # "title": "AWS Queue Alert",
    # "title_link": "https://api.slack.com/",
    "text": "`Checking if there are messages in the queue`",
    "fields": [
        {
            "title": "*Status*",
            "value": "`OK`",
            "short": 'false'
        },
        {
            "title": "",
            "value": "",
            "short": 'true'
        },
        {
            "title": "*MetricName*",
            "value": "ApproximateNumberOfMessagesVisible",
            # "short": 'false'
        },
        {
            "title": "",
            "value": "",
            # "short": 'true'
        },
        {
            "title": "*QueueName*",
            "value": "equipment-positioning-manager-accounting.fifo",
            # "short": 'true'
        },
        {
            "title": "",
            "value": "",
            # "short": 'true'
        },
        {
            "title": "*Action*",
            "value": "All fine, no need to worry!",
            # "short": 'true'
        }
    ]
  }
]
failure_message = [
  {
    "mrkdwn_in": [
        "text"
    ],
    "color": "danger",
    # "pretext": "Optional pre-text that appears above the attachment block",
    # "author_name": "AWS Queue Monitoring",
    # "author_icon": slack_icon_url,
    "title": "AWS Queue Alert",
    "title_link": "https://api.slack.com/",
    "text": "`Checking if there are messages in the queue`",
    "fields": [
        {
            "title": "*Status*",
            "value": "`ALARM`",
            "short": 'false'
        },
        {
            "title": "",
            "value": "",
            "short": 'true'
        },
        {
            "title": "*MetricName*",
            "value": "ApproximateNumberOfMessagesVisible",
            # "short": 'false'
        },
        {
            "title": "",
            "value": "",
            # "short": 'true'
        },
        {
            "title": "*QueueName*",
            "value": "equipment-positioning-manager-accounting.fifo",
            # "short": 'true'
        },
        {
            "title": "",
            "value": "",
            # "short": 'true'
        },
        {
            "title": "*Action*",
            "value": "Tagging entire channel to notify ASAP!\n<!here>",
            # "short": 'true'
        }
    ]
  }
]


def post_message_to_slack(message):
    return requests.post('https://slack.com/api/chat.postMessage', {
        'token': slack_token,
        'channel': slack_channel,
        'text': slack_text,
        'icon_url': slack_icon_url,
        'username': slack_user_name,
        # 'blocks': json.dumps(slack_blocks),
        'attachments': json.dumps(message)
    }).json()
