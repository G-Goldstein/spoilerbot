import random

choices = [
('Awaken the Scry Tyrant', 'https://www.fgrecservices.com/wp-content/uploads/2015/11/WS108369.jpg'),
('Call the Scrybreaker', 'https://s3-us-west-2.amazonaws.com/echomage/cards/CMD/247202.crop.hq.jpg'),
('Daring Scryjek', 'http://www.artofmtg.com/wp-content/uploads/2014/01/Daring-Skyjek-Art.jpg'),
('Eldrazi Scryspawner', 'https://pre00.deviantart.net/2752/th/pre/i/2015/363/9/2/eldrazi_skyspawner_by_chasestone-d9lxx91.jpg'),
("Isperia's Scrywatch", 'http://1.bp.blogspot.com/-9X3uUpJR38c/UG80gSsqrtI/AAAAAAAAA0Q/aQXgqfVoqHY/s1600/Isperia%27s+Skywatch.png'),
('Kor Scryfisher', 'http://magic.wizards.com/sites/mtg/files/image_legacy_migration/mtg/images/daily/arcana/332_final.jpg'),
('Leonin Scryhunter', 'https://orig00.deviantart.net/0cf1/f/2011/070/a/6/mtg__leonin_skyhunter_by_algenpfleger-d3bdmy7.jpg'),
('Merfolk Scryscout', 'https://i.pinimg.com/originals/c9/e7/f0/c9e7f08c1879b0215271e8796a69c06c.jpg'),
('Simic Scry Swallower', 'https://cdn.pucatrade.com/cards/crops/sm/27470.jpg'),
('Scry Terror', 'https://scentofagamer.files.wordpress.com/2017/11/johannbodin_skyterror.jpg'),
('Scryknight Legionnaire', 'https://media-dominaria.cursecdn.com/attachments/103/61/635032499073490380.jpg'),
('Scrywatcher Adept', 'https://magic.wizards.com/sites/mtg/files/image_legacy_migration/mtg/images/daily/wallpapers/WP_SkywatcherAdept_2560x1600.jpg'),
('Scrywise Teachings', 'https://52f4e29a8321344e30ae-0f55c9129972ac85d6b1f4e703468e6b.ssl.cf2.rackcdn.com/products/pictures/1109131.png'),
('Talrand, Scry Summoner', 'https://d1u5p3l4wpay3k.cloudfront.net/mtgsalvation_gamepedia/thumb/f/f1/Talrand.jpg/1200px-Talrand.jpg'),
]

def select_bot():
  return random.choice(choices)

