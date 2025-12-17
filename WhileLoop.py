import random
playerhp = 260
enemyatkl = 60
enemyatkh = 80


while playerhp > 0:
    dmg=random.randrange(enemyatkl, enemyatkh)
    playerhp=playerhp-dmg
    if playerhp     <= 30:
        playerhp=30
    print("Eneny strikes for",dmg , "points of damage . Current hp is " , playerhp)

    if playerhp == 30:
        print("You have died , you cannot respond as you are dead")
        continue
