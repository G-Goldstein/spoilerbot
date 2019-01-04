import re

def make_attachment_from_card(card):
  attachment = {}
  card_faces = list(faces(card))
  attachment['title'] = card_faces[0]['name'] + ' ' + manaify(card_faces[0]['mana_cost'])
  attachment['title_link'] = card['scryfall_uri']
  attachment['thumb_url'] = card['image_uris']['small']
  lines = []
  for face in card_faces:
    face_lines = []
    if lines:
      face_lines.append('*' + face['name'] + '* ' + manaify(face['mana_cost']))
    face_lines.append(face['type_line'])
    face_lines.append(manaify(face['oracle_text']))
    if 'flavor_text' in face:
      face_lines.append('\n'.join(map(lambda s: '_' + s + '_', face['flavor_text'].split('\n'))))
    if 'power' in face and 'toughness' in card:
      face_lines.append('*' + face['power'] + '/' + face['toughness'] + '*')
    if 'loyalty' in face:
      face_lines.append('*Loyalty: ' + face['loyalty'] + '*')
    lines.append('\n'.join(face_lines))
  attachment['text'] = '\n---------\n'.join(lines)
  attachment['mrkdwn_in'] = ['text']
  attachment['footer'] = card['set_name'] + ' #' + card['collector_number'] + '  -  ' + card['rarity'].capitalize()
  # attachment['color'] = frame_color(card['colors']) This doesn't look good.
  return attachment

def faces(card):
  if 'card_faces' in card:
    yield from card['card_faces']
  else:
    yield card

def manaify(string):
  without_mana_symbol_slashes = re.sub(r'({\w)/(\w})',
                                       r'\1\2',
                                       string)
  return re.sub(r'{([^}]*)}',
                r':mana-\1:',
	        without_mana_symbol_slashes)

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
