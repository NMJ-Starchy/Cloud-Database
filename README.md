## Cloud Database Module 

In this project, I was tasked with creating my own cloud database to create data in and manage it. I'm an avid player of Dungeons and Dragons 5th Edition, I run games often and often have trouble getting quick numbers for encounters to run against the players in my game. To help with this, I created a monster manual of my own, while there are many reference books that have been made for this, I just need something for quick reference. So, I have made a small database filled with different stat blocks that will help me out. 

## Running the Program
I used Google Firestore to create this database, and Python 3 to interact with it. The Firebase_admin package for python, as well as the credentials and firestore packages from Firebase_admin, are needed to interact with the database. I created a data frame for each monster, and used the set() operator to create new documents for each monster in the database. This program should run through creating several different monsters, edit some information in the Goblin stat block, shows the zombie stat block, grabs all stat blocks in the database, and then finally deletes the zombie statblock.

## Output
### This Should be the output in the console generated by the code
!(Screenshot)['Output.png']

### View of the Firestore Console

!(Firestore)['Firestore.png']

## Helpful tools

The Firebase guide website was very helpful to me, it was able to walk me through eerything that I needed to do. Setting up the database itself and getting the proper permissions to edit it was probably the toughest part, but more reading into the site was able to help me out with that as well.

https://firebase.google.com/docs/firestore