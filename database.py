import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account to connect to database
cred = credentials.Certificate('/Users/natejhome/projects/Cloud Database/my-monster-manual-c54dbafe3cb7.json')
firebase_admin.initialize_app(cred)

db = firestore.client()


# Write a new document into the database
# Goblin stat block
Goblin_data = {
    u'AC': 11,
    u'ATK': u'1d6',
    u'CR': 1,
    u'HP': 15,
    u'SPD': 30,
    u'TYPE': u'Undead'
}

db.collection(u'monster_stats').document(u'Goblin').set(Goblin_data)

# Zombie stat block
Zombie_data = {
    u'AC': 13,
    u'ATK': u'1d6',
    u'CR': 1,
    u'HP': 25,
    u'SPD': 30,
    u'TYPE': u'Undead'
}

db.collection(u'monster_stats').document(u'Zombie').set(Zombie_data)

# Gnoll stat block
Gnoll_data = {
    u'AC': 13,
    u'ATK': u'2d4',
    u'CR': 1,
    u'HP': 20,
    u'SPD': 30,
    u'TYPE': u'Creature'
}

db.collection(u'monster_stats').document(u'Gnoll').set(Gnoll_data)

# Bandit stat block
Bandit_data = {
    u'AC': 15,
    u'ATK': u'2d6',
    u'CR': 1,
    u'HP': 28,
    u'SPD': 30,
    u'TYPE': u'Humanoid'
}

db.collection(u'monster_stats').document(u'Bandit').set(Bandit_data)

# Griffon stat block
Griffon_data = {
    u'AC': 12,
    u'ATK': u'1d8 + 4 x 2',
    u'CR': 2,
    u'HP': 60,
    u'SPD': 30,
    u'FLY': 80,
    u'TYPE': u'Creature'
}

db.collection(u'monster_stats').document(u'Griffon').set(Griffon_data)

# Werewolf stat block
Werewolf_data = {
    u'AC': 12,
    u'ATK': u'1d8 + 2 x 2',
    u'CR': 3,
    u'HP': 60,
    u'SPD': 40,
    u'STATUS': u'Lycanthropy',
    u'TYPE': u'Humanoid'
}

db.collection(u'monster_stats').document(u'Werewolf').set(Werewolf_data)

# Manticore stat block
Manticore_data = {
    u'AC': 14,
    u'ATK': u'1d8 + 3 x 2',
    u'CR': 3,
    u'HP': 70,
    u'SPD': 30,
    u'FLY': 50,
    u'TYPE': u'Monster'
}

db.collection(u'monster_stats').document(u'Manticore').set(Manticore_data)

# Mimic stat block
Mimic_data = {
    u'AC': 12,
    u'ATK': u'2d8 + 3',
    u'CR': 2,
    u'HP': 55,
    u'SPD': 15,
    u'STATUS': u'Shapechanger',
    u'TYPE': u'Monster'
}

db.collection(u'monster_stats').document(u'Mimic').set(Mimic_data)

# Mind Flayer stat block
Flayer_data = {
    u'AC': 15,
    u'ATK': u'10d10',
    u'CR': 7,
    u'HP': 75,
    u'SPD': 30,
    u'STATUS': u'Mind Blast',
    u'TYPE': u'Abberation'
}

db.collection(u'monster_stats').document(u'Mind Flayer').set(Flayer_data)

# Owlbear stat block
Owlbear_data = {
    u'AC': 13,
    u'ATK': u'1d10 + 5 x 2',
    u'CR': 3,
    u'HP': 60,
    u'SPD': 40,
    u'TYPE': u'Monster'
}

db.collection(u'monster_stats').document(u'Owlbear').set(Owlbear_data)

#  Purple Worm stat block
Worm_data = {
    u'AC': 18,
    u'ATK': u'3d8 + 9 x 2',
    u'CR': 15,
    u'HP': 250,
    u'SPD': 50,
    u'SIZE': u'Gargantuan',
    u'TYPE': u'Monster'
}

db.collection(u'monster_stats').document(u'Purple Worm').set(Worm_data)

#  Zuggtmoy stat block
Zugg_data = {
    u'AC': 18,
    u'ATK': u'4d8 + 6 x 3',
    u'CR': 23,
    u'HP': 310,
    u'SPD': 30,
    u'STATUS': u'Madness of Zuggtmoy',
    u'TYPE': u'Fiend'
}

db.collection(u'monster_stats').document(u'Zuggtmoy').set(Zugg_data)

# Add to an existing document
gob_add = db.collection(u'monster_stats').document(u'Goblin')

# Adds the creature type to the document
gob_add.set({
    u'TYPE': u'Creature'
}, merge = True)

# Modify an Existing Document
gob_edit = db.collection(u'monster_stats').document(u'Goblin')

# changes the goblin attack damage to 1d4
gob_edit.update({
    u'ATK': u'1d4'
})

# Getting Data

# Get one Document
doc_get = db.collection(u'monster_stats').document(u'Zombie')

doc = doc_get.get()
if doc.exists:
    print(f'Document Data: {doc.to_dict()}')
else:
    print(u'Document does not exist...')

# retrieve all documents in the database

manual_ref = db.collection(u'monster_stats')
docs = manual_ref.stream()

for doc in docs:
    print(f' {doc.id} => {doc.to_dict()}')


# Deleting Data
# Delete the full Zombie Document

db.collection(u'monster_stats').document(u'Zombie').delete()

