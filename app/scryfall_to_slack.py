import re

def make_attachment_from_card(card):
  attachment = {}
  attachment['title'] = card['name'] + ' ' + manaify(card['mana_cost'])
  attachment['title_link'] = card['scryfall_uri']
  attachment['thumb_url'] = card['image_uris']['small']
  lines = [card['type_line'], manaify(card['oracle_text'])]
  if 'flavor_text' in card:
    lines.append('\n'.join(map(lambda s: '_' + s + '_', card['flavor_text'].split('\n'))))
  if 'power' in card and 'toughness' in card:
    lines.append('*' + card['power'] + '/' + card['toughness'] + '*')
  if 'loyalty' in card:
    lines.append('*Loyalty: ' + card['loyalty'] + '*')
  attachment['text'] = '\n'.join(lines)
  attachment['mrkdwn_in'] = ['text']
  attachment['footer'] = card['set_name'] + ' #' + card['collector_number']
  return attachment

def manaify(string):
  return re.sub(r'{([^}]*)}',
         r':mana-\1:',
	 string)
