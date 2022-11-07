from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

slack_token = 'xoxb-4345153214417-4332552686770-ybP1ExZT0rzd96NfLDwf1M67'

client = WebClient(token=slack_token)

channel = 'urop'
text = 'test'  # 추후에 그림일기의 텍스트부분을 전달받는걸로 변경

try:
    response = client.chat_postMessage(channel=channel,
                                       text=text)
except SlackApiError as e:
    print('Error: {}'.format(e.response['error']))