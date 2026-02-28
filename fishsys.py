import random
import loadassets
class fishtype:
    def __init__(self,name,image,value,weight):
        self.name = name
        self.image = image
        self.value = value
        self.weight = weight
    def showinfo(self):
        print(self.name,self.image,self.value,self.weight,self.chance)
# Name , Image , Value , Weight Class
commontable = [fishtype("Cod",loadassets.cod,5,1),fishtype("Salmon",loadassets.salmon,8,1),fishtype("Red Snapper",loadassets.redsnapper,11,1),fishtype("Bass",loadassets.bass,15,2),fishtype("Flounder",loadassets.flounder,18,1),fishtype("Sardine",loadassets.sardine,9,1),fishtype("Tilapia",loadassets.tilapia,15,2)]
raretable = [["Clownfish",loadassets.clownfish,25,1],["Koi",loadassets.koi,28,1],["Tuna",loadassets.tuna,30,2],["Mackeral",loadassets.mackeral,35,2],["Carp",loadassets.carp,40,2]]
legendarytable = [["Arapaima",loadassets.arapaima,75,3],["Surgeonfish",loadassets.surgeon,50,3],["Red Herring",loadassets.rederring,85,3],["Barb",loadassets.barb,80,3],["MaoMao",loadassets.maomao,83,3]]
def pickcommon():
    global commontable
    #Todo: 450+ for rare table
    chance = random.randint(1,550)
    if chance <= 150:
        return commontable[0]
    elif chance > 150 and chance <= 250:
        return commontable[1]
    elif chance > 250 and chance <= 325:
        return commontable[2]
    elif chance > 325 and chance <= 375:
        return commontable[3]
    elif chance > 375 and chance <= 415:
        return commontable[4]
    elif chance > 415 and chance <= 465:
        return commontable[5]
    elif chance > 465 and chance <= 500:
        return commontable[6]
    else:
        return commontable[0]


def pickrare():
    global commontable
    global raretable
    chance = random.randint(0,800)
    if chance <= 150:
        return raretable[0]
    elif chance > 150 and chance <= 250:
        return raretable[1]
    elif chance > 250 and chance <= 375:
        return raretable[2]
    elif chance > 375 and chance <= 425:
        return raretable[3]
    elif chance > 425 and chance <= 500:
        return raretable [4]
    else:
        return random.choice(commontable)
def picklegendary():
    global legendarytable
    global raretable
    chance = random.randint(0,500)
    if chance <= 50:
        return legendarytable[0]
    elif chance > 50 and chance <= 100:
        return legendarytable[1]
    elif chance > 100 and chance  <= 150:
        return legendarytable[2]
    elif chance > 150 and chance <= 200:
        return legendarytable[3]
    elif chance > 200 and chance <= 275:
        return legendarytable[4]
    else:
        return random.choice(raretable)