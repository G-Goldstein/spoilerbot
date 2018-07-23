import requests, os, json, puns

funny_set_channel = os.environ['FUN_CHANNEL']
main_set_channel = os.environ['MAIN_CHANNEL']

SLACK_WEBHOOK_URL = os.environ['SLACK_WEBHOOK_URL']

def set_channel(funny_channel):
  if funny_channel:
    return funny_set_channel
  return main_set_channel

def post(message, is_funny):
  payload = {}
  payload['channel_id'] = set_channel(is_funny)
  payload['text'] = message
  payload['username'], payload['icon_url'] = puns.select_bot()
  data = {'payload': json.dumps(payload)}

  session = requests.session()
  session.post(SLACK_WEBHOOK_URL, data=data)

