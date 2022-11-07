from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from sns.token import slack_token

client = WebClient(token=slack_token)

channel = 'urop'
text = 'test'  # 추후에 그림일기의 텍스트부분을 전달받는걸로 변경

try:
    response = client.chat_postMessage(channel=channel,
                                       text=text)
except SlackApiError as e:
    print('Error: {}'.format(e.response['error']))