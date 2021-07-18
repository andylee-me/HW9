#給予牌相對應的能力
def rule(card):
    if card == "A":
        total.append(total[-1]-total[-1])
    if card == "2":
        total.append(total[-1]+2)
    if card == "3":
        total.append(total[-1]+3)
    if card == "4":
        total.append(total[-1]*2)
    if card == "5":
        total.append(total[-1]+5)
    if card == "6":
        total.append(total[-1]+6)
    if card == "7":
        for i in range(1,151):
            player1.append(i)
            shuffle(player1)
            total.append(player1[0])
    if card == "8":
        shuffle(random)
        total.append(total[-1]+int(random[0]))
        print("你抽到",random[0],"點")
    if card == "9":
        total.append(total[-1]+9)
    if card == "-10":
        total.append(total[-1]-10)
    if card == "+10":
        total.append(total[-1]+10)
    if card == "10":
        choose = input("要+10還是-10:")
        while choose != "+10" and choose != "-10":
            choose = input("請輸入'+10'或是'-10'")
        if choose == "+10":
            total.append(total[-1]+10)
        if choose == "-10":
            total.append(total[-1]-10)
    if card == "j":
        pass
    if card == "-20":
        total.append(total[-1]-20)
    if card == "+20":
        total.append(total[-1]+20)
    if card == "q":
        choose = input("要+20還是-20:")
        while choose != "+20" and choose != "-20":
            choose = input("請輸入'+20'或是'-20'")
        if choose == "+20":
            total.append(total[-1]+20)
        if choose == "-20":
            total.append(total[-1]-20)
    if card == "k":
        total.append(boom[0])
    if total[-1] < 0:
        total.append(zero)

#電腦思考
def com(card):
    if len(number) == 0:
        for j in order:
            number.append(j)
            shuffle(number)
        for i in range(0,5):
            number.remove(player[i])
            number.remove(p2[i])
            number.remove(p3[i])
            number.remove(p4[i])

    if total[-1] >= 90:
        if "9" in card and total[-1] == 90:
            card.remove("9")
            play.append("9")
            play.pop(0)
            card.append(number.pop())
        elif "8" in card and total[-1] <= 92:
            card.remove("8")
            play.append("8")
            play.pop(0)
            card.append(number.pop())
        elif "6" in card and total[-1] <= 93:
            card.remove("6")
            play.append("6")
            play.pop(0)
            card.append(number.pop())
        elif "5" in card and total[-1] <= 94:
            card.remove("5")
            play.append("5")
            play.pop(0)
            card.append(number.pop())
        elif "3" in card and total[-1] <= 96:
            card.remove("3")
            play.append("3")
            play.pop(0)
            card.append(number.pop())
        elif "2" in card and total[-1] <= 97:
            card.remove("2")
            play.append("2")
            play.pop(0)
            card.append(number.pop())
        else:
            if "10" in card:
                card.remove("10")
                play.append("-10")
                play.pop(0)
                card.append(number.pop())
            elif "q" in card:
                card.remove("q")
                play.append("-20")
                play.pop(0)
                card.append(number.pop())
            elif "j" in card:
                card.remove("j")
                play.append("j")
                play.pop(0)
                card.append(number.pop())
            elif "k" in card:
                card.remove("k")
                play.append("k")
                play.pop(0)
                card.append(number.pop())
            elif "A" in card:
                card.remove("A")
                play.append("A")
                play.pop(0)
                card.append(number.pop())
            elif "7" in card:
                card.remove("7")
                play.append("7")
                play.pop(0)
                card.append(number.pop())
            elif "4" in card:
                card.remove("4")
                play.append("4")
                play.pop(0)
                card.append(number.pop())
            else:
                play.append(card.pop())
                play.pop(0)
    elif total[-1] >= 50:
        if "4" in card and total[-1] * 2 < 99:
            card.remove("4")
            play.append("4")
            play.pop(0)
            card.append(number.pop())        
        elif "9" in card:
            card.remove("9")
            play.append("9")
            play.pop(0)
            card.append(number.pop())
        elif "8" in card:
            card.remove("8")
            play.append("8")
            play.pop(0)
            card.append(number.pop())
        elif "6" in card:
            card.remove("6")
            play.append("6")
            play.pop(0)
            card.append(number.pop())
        elif "5" in card:
            card.remove("5")
            play.append("5")
            play.pop(0)
            card.append(number.pop())
        elif "3" in card:
            card.remove("3")
            play.append("3")
            play.pop(0)
            card.append(number.pop())
        elif "2" in card:
            card.remove("2")
            play.append("2")
            play.pop(0)
            card.append(number.pop())
        else:
            if "k" in card:
                card.remove("k")
                play.append("k")
                play.pop(0)
                card.append(number.pop())
            elif "10" in card:
                card.remove("10")
                play.append("+10")
                play.pop(0)
                card.append(number.pop())
            elif "q" in card and total[-1] + 20 <= 99:
                card.remove("q")
                play.append("+20")
                play.pop(0)
                card.append(number.pop())
            elif "j" in card:
                card.remove("j")
                play.append("j")
                play.pop(0)
                card.append(number.pop())
                card.append(number.pop())
            elif "A" in card:
                card.remove("A")
                play.append("A")
                play.pop(0)
                card.append(number.pop())
            elif "7" in card:
                card.remove("7")
                play.append("7")
                play.pop(0)
                card.append(number.pop())
            else:
                play.append(card.pop())
                play.pop(0)
    elif total[-1] < 50:
        if "k" in card:
            card.remove("k")
            play.append("k")
            play.pop(0)
            card.append(number.pop())
        if "4" in card:
            card.remove("4")
            play.append("4")
            play.pop(0)
            card.append(number.pop())        
        elif "9" in card:
            card.remove("9")
            play.append("9")
            play.pop(0)
            card.append(number.pop())
        elif "8" in card:
            card.remove("8")
            play.append("8")
            play.pop(0)
            card.append(number.pop())
        elif "6" in card:
            card.remove("6")
            play.append("6")
            play.pop(0)
            card.append(number.pop())
        elif "5" in card:
            card.remove("5")
            play.append("5")
            play.pop(0)
            card.append(number.pop())
        elif "3" in card:
            card.remove("3")
            play.append("3")
            play.pop(0)
            card.append(number.pop())
        elif "2" in card:
            card.remove("2")
            play.append("2")
            play.pop(0)
            card.append(number.pop())
        else:
            if "10" in card:
                card.remove("10")
                play.append("+10")
                play.pop(0)
                card.append(number.pop())
            elif "q" in card:
                card.remove("q")
                play.append("+20")
                play.pop(0)
                card.append(number.pop())
            elif "j" in card:
                card.remove("j")
                play.append("j")
                play.pop(0)
                card.append(number.pop())
                card.append(number.pop())
            elif "A" in card:
                card.remove("A")
                play.append("A")
                play.pop(0)
                card.append(number.pop())
            elif "7" in card:
                card.remove("7")
                play.append("7")
                play.pop(0)
                card.append(number.pop())
            else:
                play.append(card.pop())
                play.pop(0)
                

#抽牌
def doro(card):
    card.remove(ans)
    card.append(number.pop(0))

#重洗牌
def wash(card):
    for i in range(0,5):
        number.remove(player[i])
        number.remove(p2[i])
        number.remove(p3[i])
        number.remove(p4[i])
            
#轉成數字
def num(card):
    for i in range(0,5):
        if card[i] == "j":
            card[i] = '11'
        if card[i] == "q":
            card[i] = '12'
        if card[i] == "k":
            card[i] = '13'
        if card[i] == "A":
            card[i] = '1'

#轉成字母
def letter(card):
    for o in range(0,5):
        if player[o] == "11":
            player[o] = "j"
        if player[o] == "12":
            player[o] = "q"
        if player[o] == "13":
            player[o] = "k"
        if player[o] == "1":
            player[o] = "A"
#規則
print("RULE:","\n","每人有五張牌,牌有各種能力,當數大於99時,使數大於99的那人就輸了,並使數歸0","\n","(註:數的最小值為0)","\n","牌的能力:","\n","A:使數歸零","\n","2:數+2","\n","3:數+3","\n","4:把數x2","\n","5:數+5","\n","6:數+6","\n","7:數變為1~150的隨機數","\n","8:數+1~9的隨機數字","\n","9:數+9","\n","10:數+10/-10","\n","j:跳過自己回合","\n","q:數+20/-20","\n","k:使數變為99")

from random import shuffle
order = ["A","A","A","A", "2", "2", "2","2", "3", "3", "3","3", "4","4", "4", "4","5","5","5" ,"5","6","6","6", "6","7","7","7", "7","8","8","8", "8", "9", "9", "9","9","10","10","10", "10","j","j","j", "j","q","q","q", "q","k","k","k", "k"]
random = ["1","2","3","4","5","6","7","8","9"]
turn = ["player","p2","p3","p4"]
number = []
total = [0]
boom = [99]
player1 = []
player = []
p2 = []
p2_die = []
p3 = []
p3_die = []
p4 = []
p4_die = []
play = [0]
zero = 0
#洗牌
for j in order:
    number.append(j)
    shuffle(number)
#發牌
for i in range(0,5):
    player1.append(number.pop(i))
    p2.append(number.pop(i))
    p3.append(number.pop(i))
    p4.append(number.pop(i))
#整理
num(player1)
player1 = list(map(int,player1))
while len(player1) != 0:
    player.insert(0,max(player1))
    player1.remove(max(player1))
for i in range(0,5):
    player = list(map(str,player))
letter(player)
while True:
    print("\n","目前",total[-1],"點","\n")
    print(player)
    ans = input("打出你想出的牌:")
    while player[0] != ans and player[1] != ans and player[2] != ans and player[3] != ans and player[4] != ans:
        print("你沒有這張牌,重選一張")
        ans = input("打出你想出的牌:")
    rule(ans)
    if total[-1] > 99:
        print("\n","目前",total[-1],"點","\n")
        total.append(zero)
        print("你炸了")
        break
    doro(player)
    if len(number) == 0:
        for j in order:
            number.append(j)
            shuffle(number)
        wash("card")
    num(player)
    print("\n","目前",total[-1],"點","\n")
    player = list(map(int,player))
    player.sort()
    player = list(map(str,player))
    letter(player)
    if len(p2_die) == 0:
        com(p2)
        if len(number) == 0:
            for j in order:
                number.append(j)
                shuffle(number)
            wash("card")
        print("\n","電腦 2 出",play,"\n")
        rule(play[0])
        print("目前",total[-1],"點","\n")
        if total[-1] > 99:
            total.append(zero)
            input("p2炸了")
            p2_die.append("0")
            if len(p2_die) != 0 and len(p3_die) != 0 and len(p4_die) != 0:
                print("YOU WIN","你殺了所有人")
                break
    if len(p3_die) == 0:
        com(p3)
        if len(number) == 0:
            for j in order:
                number.append(j)
                shuffle(number)
            wash("card")
        print("\n"," 電腦3 出",play,"\n")
        rule(play[0])
        print("目前",total[-1],"點","\n")
        if total[-1] > 99:
            total.append(zero)
            input("p3炸了")
            p3_die.append("0")
            if len(p2_die) != 0 and len(p3_die) != 0 and len(p4_die) != 0:
                print("YOU WIN","你殺了所有人")
                break
    if len(p4_die) == 0:
        com(p4)
        if len(number) == 0:
            for j in order:
                number.append(j)
                shuffle(number)
            wash("card")
        print("\n","電腦 4 出",play,"\n")
        rule(play[0])
        print("目前",total[-1],"點","\n")
        if total[-1] > 99:
            total.append(zero)
            input("p4炸了")
            p4_die.append("0")
            if len(p2_die) != 0 and len(p3_die) != 0 and len(p4_die) != 0:
                print("YOU WIN","你殺了所有人")
                break








