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
  payload['channel'] = set_channel(is_funny)
  payload['text'] = message
  payload['username'], payload['icon_url'] = puns.select_bot()
  data = {'payload': json.dumps(payload)}

  session = requests.session()
  session.post(SLACK_WEBHOOK_URL, data=data)

def make_attachment_from_card(card):
  attachment = {}
  attachment['title'] = card['name']
  attachment['title_link'] = card['scryfall_uri']
  attachment['thumb_url'] = card['image_uris']['small']
  lines = [card['type_line'], card['oracle_text']]
  if 'flavor_text' in card:
    lines.append('\n'.join(map(lambda s: '_' + s + '_', card['flavor_text'].split('\n'))))
  if 'power' in card and 'toughness' in card:
    lines.append('*' + card['power'] + '/' + card['toughness'] + '*')
  if 'loyalty' in card:
    lines.append('*' + card['loyalty'] + '*')
  attachment['text'] = '\n'.join(lines)
  attachment['mrkdwn_in'] = ['text']
  attachment['footer'] = card['set_name']
  return attachment

def post_attachments(attachments, is_funny):
  payload = {}
  payload['channel'] = set_channel(is_funny)
  payload['username'], payload['icon_url'] = puns.select_bot()

  payload['attachments'] = attachments
  data = {'payload': json.dumps(payload)}

  session = requests.session()
  session.post(SLACK_WEBHOOK_URL, data=data)
