import random
import math

q0 = input("dia famous (terkenal) kaga? [terkenal jir / b aja] ")
if q0 == "b aja":
    score_diasuka =+ 10
    print("")
else:
    score_diasuka =- 10
    print("")

q1 = input("lu udh kasi dia coklat blm? [udh / blm] ")
    
if q1 == "udh":
    score_diasuka =+ 5
    print("gacor kang, tpi dia masih blm tertarik sama lu :v")
    print("")
else:
    score_diasuka =- 5
    print("yahh... sayang bet, emng lu kaga effort samsek -_-")
    print("")

q2 = input("lu udh send dia bunga kah? [udh / blm] ")

if q2 == "udh" and q0 != "b aja":
    score_diasuka =+ 1
    print("")
elif q2 == "udh" and q0 == "b aja":
    score_diasuka =+ 10
    print("")
elif q2 == "blm" and q0 != "b aja":
    score_diasuka =- 45
    print("")
elif q2 == "blm" and q0 == "b aja":
    score_diasuka =- 2
    print("")

q3 = input("dia tertarik sama lu gasih? [tertarik / g] ")
if q3 == "tertarik":
    score_diasuka =+ 200
else:
    score_diasuka =-10

if score_diasuka <= 80:
    dia_suka_sama_lu = False
else:
    dia_suka_sama_lu = True


if dia_suka_sama_lu == False:
    print("SUDAHILAH MEMBADUTNYA KAWAN")
else:
    print("ANJAY, PUNYA CEWE.")