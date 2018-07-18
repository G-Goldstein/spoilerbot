import scryfall, spoiled, slack, timer

def spoil_cards(set, cards):
  card_tags = ['[[{}]]'.format(card['name']) for card in cards]
  message = '{}: {}'.format(set['name'], ', '.join(card_tags))
  slack.post(message, is_funny=scryfall.funny_set(set))

def spoil_new_cards():
  for set in scryfall.upcoming_sets():
    set_code = set['code']
    new_spoilers = [card for card in scryfall.spoiled_cards(set_code) if card['name'] not in spoiled.previously_spoiled_names(set_code)][:5]
    try:
      spoil_cards(set, new_spoilers)
    except:
      print('Something went wrong')
    else:
      spoiled.store_spoiled_cards(set_code, new_spoilers) 

if __name__ == '__main__':
  while True:
    timer.sleep_until_next_time()
    spoil_new_cards()
 
