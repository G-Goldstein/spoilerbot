import os.path

def previously_spoiled_names(set):
  storage_file = file_for_set(set)
  if not os.path.isfile(storage_file):
    return []
  with open(storage_file, 'r') as f:
    return f.read().splitlines()

def store_spoiled_cards(mtg_set, cards):
  storage_file = file_for_set(mtg_set)
  old_spoiled_names = previously_spoiled_names(mtg_set)
  new_spoiled_names = [card['name'] for card in cards]
  all_spoiled_names = set(old_spoiled_names + new_spoiled_names)
  with open(storage_file, 'w+') as f:
    for name in all_spoiled_names:
      f.write(name + '\r\n')

def file_for_set(set):
  storage_dir = 'spoiled'
  if not os.path.exists(storage_dir):
    os.makedirs(storage_dir)
  return '{}/{}'.format(storage_dir, set)
