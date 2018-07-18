import os.path

def previously_spoiled_names(set):
  storage_file = 'spoiled/{}'.format(set)
  if not os.path.isfile(storage_file):
    return []
  with open(storage_file, 'r') as f:
    return f.read().splitlines()

def store_spoiled_cards(mtg_set, cards):
  storage_file = 'spoiled/{}'.format(mtg_set)
  old_spoiled_names = previously_spoiled_names(mtg_set)
  new_spoiled_names = [card['name'] for card in cards]
  all_spoiled_names = set(old_spoiled_names + new_spoiled_names)
  with open(storage_file, 'w+') as f:
    for name in all_spoiled_names:
      f.write(name + '\r\n')

def file_for_set(set):
  return 'spoiled/{}'.format(set)
