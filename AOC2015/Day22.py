import time
bHP = 51
bD = 9
hHP = 50
hMP = 500
hA = 0
spells = ["MM","Drain","Shield","Poison","Recharge"]
win = [1000000,[]]
hard = False

#Input: Spell to cast, Boss HP, Hero HP, hero MP, hero Armour, Shield timer, Poison timer, Recharge Timer, MP Spent
def recurseRound(spell,bHP,hHP,hMP,hA,sT,pT,rT, spent):
    def effects(bHP,hHP,hMP,hA,sT,pT,rT):
        if sT > 0:
            sT -= 1
            if sT == 0: hA = 0
        if pT > 0:
            bHP -= 3
            pT -= 1
        if rT > 0:
            hMP += 101
            if hMP > 500: hMP = 500
            rT -= 1
        return bHP,hHP,hMP,hA,sT,pT,rT
    def alive(spell,bHP,hHP,hMP,spent):
        global win
        if hHP <= 0:
            return False
        if bHP <= 0:
            if spent < win[0]: win = [spent,spell]
            return False
        return True
    #print(spell,bHP,hHP,hMP,hA,sT,pT,rT)
    if spent > win[0]: return
    #print(win)

    #PLAYER TURN
    #If hard mode deduct a hp
    if hard == True:
        hHP -= 1
        if alive(spell,bHP,hHP,hMP,spent) == False: return 
    #Apply Effects
    bHP,hHP,hMP,hA,sT,pT,rT = effects(bHP,hHP,hMP,hA,sT,pT,rT)

    #Check if boss alive
    if alive(spell,bHP,hHP,hMP,spent) == False: return

    #Cast Spell
    if spell[len(spell)-1] == "MM":
        hMP -= 53
        spent += 53
        if hMP < 0:
            #outcomesLoss.append([500-hMP,spell]) #Cant cast cheapest spell == a loss
            return
        bHP -= 4
    elif spell[len(spell)-1] == "Drain":
        hMP -= 73
        spent += 73
        if hMP < 0: return #Illegal move, so end this branch
        bHP -= 2
        hHP += 2
        if hHP > 50: hHP = 50 #Assuming cant heal over initial hp
    elif spell[len(spell)-1] == "Shield":
        hMP -= 113
        spent += 113
        if hMP < 0: return #Illegal move, so end this branch
        hA = 7
        sT = 6
    elif spell[len(spell)-1] == "Poison":
        hMP -= 173
        spent += 173
        if hMP < 0: return #Illegal move, so end this branch
        pT = 6
    elif spell[len(spell)-1] == "Recharge":
        hMP -= 229
        spent += 229
        if hMP < 0: return #Illegal move, so end this branch
        rT = 5

    #BOSS TURN
    #Apply Effects
    bHP,hHP,hMP,hA,sT,pT,rT = effects(bHP,hHP,hMP,hA,sT,pT,rT)

    #Check if boss alive
    if alive(spell,bHP,hHP,hMP,spent) == False: return

    #Attack
    hHP -= (bD - hA)

    #Check if hero alive
    if alive(spell,bHP,hHP,hMP,spent) == False: return

    #Start next round
    #print(spell,bHP,hHP,hMP,hA,sT,pT,rT)
    newSpell = spell.copy()
    newSpell.append("MM")
    recurseRound(newSpell,bHP,hHP,hMP,hA,sT,pT,rT,spent)
    newSpell = spell.copy()
    newSpell.append("Drain")
    recurseRound(newSpell,bHP,hHP,hMP,hA,sT,pT,rT,spent)
    if sT <= 1:
        newSpell = spell.copy()
        newSpell.append("Shield")
        recurseRound(newSpell,bHP,hHP,hMP,hA,sT,pT,rT,spent)
    if pT <= 1:
        newSpell = spell.copy()
        newSpell.append("Poison")
        recurseRound(newSpell,bHP,hHP,hMP,hA,sT,pT,rT,spent)
    if rT <= 1:
        newSpell = spell.copy()
        newSpell.append("Recharge")
        recurseRound(newSpell,bHP,hHP,hMP,hA,sT,pT,rT,spent)

def Part1():
    now = time.time()
    for i in spells:
        recurseRound([i],bHP,hHP,hMP,hA,0,0,0,0)
    print("Part 1:", win)
    print("Time taken: " + str(time.time() - now))

def Part2():
    now = time.time()
    global hard, win
    win = [1000000,[]]
    hard = True
    for i in spells:
        recurseRound([i],bHP,hHP,hMP,hA,0,0,0,0)
    print("Part 2:", win)
    print("Time taken: " + str(time.time() - now))

Part1()
Part2()