import scryfall, spoiled, slack, timer, time, scryfall_to_slack

never_post_card_names = ['Forest', 'Island', 'Mountain', 'Plains', 'Swamp']

def spoil_cards(set, cards):
  attachments = []
  for card in cards:
    attachments.append(scryfall_to_slack.make_attachment_from_card(card))
  slack.post_attachments(attachments, is_funny=scryfall.funny_set(set))

def spoil_new_cards():
  upcoming_sets = scryfall.upcoming_sets()
  if not upcoming_sets:
    time.sleep(60*60*4) # No new sets, check again in 4 hours
  for set in upcoming_sets:
    set_code = set['code']
    new_spoilers = [card for card in scryfall.spoiled_cards(set_code) if card['name'] not in spoiled.previously_spoiled_names(set_code) and card['name'] not in never_post_card_names][:5]
    if not new_spoilers:
      continue
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
 
