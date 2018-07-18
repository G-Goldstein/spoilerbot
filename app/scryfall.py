import requests, time
from datetime import datetime, timedelta

never_post_card_names = ['Forest', 'Island', 'Mountain', 'Plains', 'Swamp']
never_post_set_types = ['promo', 'token']
funny_set_types = ['commander', 'funny', 'draft_innovation']

def get(url, data=None):
  time.sleep(0.5) # Don't overload the Scryfall API
  response = requests.get(url, params=data).json()
  response_list = response['data']
  if response['has_more']:
    response_list += get(response['next_page'])
  return response_list

def spoilerable_sets():
  all_sets = get('https://api.scryfall.com/sets')
  return [set for set in all_sets if len(set['code']) == 3 and set['set_type'] not in never_post_set_types]

def upcoming_set(set):
  set_release_date = release_date(set)
  return set_release_date is not None and set_release_date > todays_date()

def todays_date():
  return datetime.now().date()

def set_code(set):
  return set['code']

def funny_set(set):
  return set in funny_set_types

def release_date(set):
  if 'released_at' not in set:
    return None
  return datetime.strptime(set['released_at'], '%Y-%m-%d').date()

def upcoming_sets():
  return reversed(list(filter(upcoming_set, spoilerable_sets())))

def spoiled_cards(set):
  data = {
    'q': 'e:{}'.format(set)
  }
  return get('https://api.scryfall.com/cards/search', data=data)
