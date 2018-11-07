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
  attachment['footer'] = card['set_name'] + ' #' + card['collector_number'] + '  -  ' + card['rarity'].capitalize()
  # attachment['color'] = frame_color(card['colors']) This doesn't look good.
  return attachment

def manaify(string):
  return re.sub(r'{([^}]*)}',
         r':mana-\1:',
	 string).replace('/', '')

def frame_color(colors):
  if len(colors) == 0:
    return None
  if len(colors) > 1:
    return '#ffdf00'
  if colors[0] == 'W':
    return '#dfdfdf'
  if colors[0] == 'B':
    return '#dfdfdf'
  if colors[0] == 'U':
    return 'dfdfff#'
  if colors[0] == 'R':
    return '#ffdfdf'
  if colors[0] == 'G':
    return '#dfffdf'
  return None
