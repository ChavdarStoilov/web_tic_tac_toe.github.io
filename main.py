import random
from browser import document



places = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " ", "wins": {"computer": 0, "you": 0}}

def reset(ev):
    places[1] = " "
    places[2] = " "
    places[3] = " "
    places[4] = " "
    places[5] = " "
    places[6] = " "
    places[7] = " "
    places[8] = " "
    places[9] = " "
    places['wins']['computer'] = 0
    places['wins']['you'] = 0
    document['aaa'].text = " "
    document.getElementById("btn").style.visibility = "hidden"
    document.getElementById("reset").style.visibility = "hidden"
    document.getElementById("result").style.visibility = "hidden"
    board()

def clear(ev):
    places[1] = " "
    places[2] = " "
    places[3] = " "
    places[4] = " "
    places[5] = " "
    places[6] = " "
    places[7] = " "
    places[8] = " "
    places[9] = " "
    document['aaa'].text = " "
    document.getElementById("btn").style.visibility = "hidden"
    document.getElementById("reset").style.visibility = "hidden"
    document.getElementById("result").style.visibility = "hidden"
    board()

def board():
    if places.get(1) == "o":
        document.getElementById('first').style.color = "red"
    elif places.get(1) == "x":
        document.getElementById('first').style.color = "blue"

    if places.get(2) == "o":
        document.getElementById('second').style.color = "red"
    elif places.get(2) == "x":
        document.getElementById('second').style.color = "blue"

    if places.get(3) == "o":
        document.getElementById('third').style.color = "red"
    elif places.get(3) == "x":
        document.getElementById('third').style.color = "blue"

    if places.get(4) == "o":
        document.getElementById('four').style.color = "red"
    elif places.get(4) == "x":
        document.getElementById('four').style.color = "blue"

    if places.get(5) == "o":
        document.getElementById('five').style.color = "red"
    elif places.get(5) == "x":
        document.getElementById('five').style.color = "blue"

    if places.get(6) == "o":
        document.getElementById('six').style.color = "red"
    elif places.get(6) == "x":
        document.getElementById('six').style.color = "blue"

    if places.get(7) == "o":
        document.getElementById('seven').style.color = "red"
    elif places.get(7) == "x":
        document.getElementById('seven').style.color = "blue"

    if places.get(8) == "o":
        document.getElementById('eight').style.color = "red"
    elif places.get(8) == "x":
        document.getElementById('eight').style.color = "blue"

    if places.get(9) == "o":
        document.getElementById('nine').style.color = "red"
    elif places.get(9) == "x":
        document.getElementById('nine').style.color = "blue"

    document['first'].text = f"{places.get(1)}"
    document['second'].text = f"{places.get(2)}"
    document['third'].text = f"{places.get(3)}"
    document['four'].text = f"{places.get(4)}"
    document['five'].text = f"{places.get(5)}"
    document['six'].text = f"{places.get(6)}"
    document['seven'].text = f"{places.get(7)}"
    document['eight'].text = f"{places.get(8)}"
    document['nine'].text = f"{places.get(9)}"

    if winner() == "Computer win" or winner() == "You win":
        document["aaa"].text = winner()
        document.getElementById("btn").style.visibility = "visible"
        document.getElementById("reset").style.visibility = "visible"
        document.getElementById("result").style.visibility = "visible"
        document['result'].text = f"Computer {places['wins']['computer']} | {places['wins']['you']} You"



def winner():

    if places[1] == "x" and places[2] == "x" and places[3] == "x":
        return "Computer win"
    elif places[1] == "o" and places[2] == "o" and places[3] == "o":
        return "You win"

    if places[4] == "x" and places[5] == "x" and places[6] == "x":
        return "Computer win"
    elif places[4] == "o" and places[5] == "o" and places[6] == "o":
        return "You win"

    if places[7] == "x" and places[8] == "x" and places[9] == "x":
        return "Computer win"
    elif places[7] == "o" and places[8] == "o" and places[9] == "o":
        return "You win"

    if places[1] == "x" and places[4] == "x" and places[7] == "x":
        return "Computer win"
    elif places[1] == "o" and places[4] == "o" and places[7] == "o":
        return "You win"

    if places[2] == "x" and places[5] == "x" and places[8] == "x":
        return "Computer win"
    elif places[2] == "o" and places[5] == "o" and places[8] == "o":
        return "You win"

    if places[3] == "x" and places[6] == "x" and places[9] == "x":
        return "Computer win"
    elif places[3] == "o" and places[6] == "o" and places[9] == "o":
        return "You win"

    if places[1] == "x" and places[5] == "x" and places[9] == "x":
        return "Computer win"
    elif places[1] == "o" and places[5] == "o" and places[9] == "o":
        return "You win"

    if places[7] == "x" and places[5] == "x" and places[3] == "x":
        return "Computer win"
    elif places[7] == "o" and places[5] == "o" and places[3] == "o":
        return "You win"



def choose(computer_choice):

    if places[computer_choice] == " ":
        places[computer_choice] = "x"
    else:
        computer_choosing()



def computer_choosing():


    computer = random.randrange(1, 9)

    choose(computer)

def new_computer_choose():

    if places[9] == "o" and places[5] == "o" or places[4] == "o" and places[7] == "o" or places[3] == "o" and places[2] == "o":
        if places[1] == " ":
            places[1] = "x"
        else:
            computer_choosing()

    elif places[1] == "о" and places[3] == "o" or places[8] == "o" and places[5] == "o":
        if places[2] == " ":
            places[2] = "x"
        else:
            computer_choosing()

    elif places[7] == "o" and places[5] == "o" or places[1] == "o" and places[2] == "o" or places[9] == "o" and places[6] == "o":
        if places[3] == " ":
            places[3] = "x"
        else:
            computer_choosing()

    elif places[6] == "o" and places[5] == "o" or places[1] == "o" and places[7] == "o":
        if places[4] == " ":
            places[4] = "x"
        else:
            computer_choosing()

    elif places[9] == "o" and places[1] == "o" or places[7] == "o" and places[3] == "o" or places[4] == "о" and places[6] == "o" or places[2] == "о" and places[8] == "o":
        if places[5] == " ":
            places[5] = "x"
        else:
            computer_choosing()

    elif places[4] == "o" and places[5] == "o" or places[3] == "0" and places[9] == "o":
        if places[6] == " ":
            places[6] = "x"
        else:
            computer_choosing()

    elif places[3] == "o" and places[5] == "o" or places[8] == "0" and places[9] == "o" or places[1] == "o" and places[4] == "o":
        if places[7] == " ":
            places[7] = "x"
        else:
            computer_choosing()

    elif places[9] == "o" and places[7] == "o" or places[2] == "o" and places[5] == "o":
        if places[8] == " ":
            places[8] = "x"
        else:
            computer_choosing()

    elif places[1] == "o" and places[5] == "o" or places[7] == "o" and places[8] == "o" or places[3] == "o" and places[6] == "o":
        if places[9] == " ":
            places[9] = "x"
        else:
            computer_choosing()

    else:
        computer_choosing()

    board()

def your_choosing():

    if winner() == "Computer win" or winner() == "You win":
        if winner() == "Computer win":
            places['wins']['computer'] += 1
        else:
            places['wins']['you'] += 1

        document["aaa"].text = winner()
        board()
        document.getElementById("btn").style.visibility = "visible"
        document.getElementById("reset").style.visibility = "visible"
        document.getElementById("result").style.visibility = "visible"
        document['result'].text = f"Computer {places['wins']['computer']} | {places['wins']['you']} You"


    elif places[1] == " " or places[2] == " " or places[3] == " " or places[4] == " " or places[5] == " " or \
            places[6] == " " or places[7] == "" or places[8] == " " or places[9] == " ":

        new_computer_choose()

    else:
        document["aaa"].text = "There no winner"
        document.getElementById("btn").style.visibility = "visible"
        document.getElementById("reset").style.visibility = "visible"
        document.getElementById("result").style.visibility = "visible"
        document['result'].text = f"Computer {places['wins']['computer']} | {places['wins']['you']} You"



def first(ev):
    if places[1] == " ":
        places[1] = "o"
        your_choosing()


def second(ev):
    if places[2] == " ":
        places[2] = "o"
        your_choosing()

def third(ev):
    if places[3] == " ":
        places[3] = "o"
        your_choosing()

def four(ev):
    if places[4] == " ":
        places[4] = "o"
        your_choosing()

def five(ev):
    if places[5] == " ":
        places[5] = "o"
        your_choosing()

def six(ev):
    if places[6] == " ":
        places[6] = "o"
        your_choosing()

def seven(ev):
    if places[7] == " ":
        places[7] = "o"
        your_choosing()

def eight(ev):
    if places[8] == " ":
        places[8] = "o"
        your_choosing()

def nine(ev):
    if places[9] == " ":
        places[9] = "o"
        your_choosing()

document['btn'].bind("click", clear)
document['reset'].bind("click", reset)
document["first"].bind("click", first)
document["second"].bind("click", second)
document["third"].bind("click", third)
document["four"].bind("click", four)
document["five"].bind("click", five)
document["six"].bind("click", six)
document["seven"].bind("click", seven)
document["eight"].bind("click", eight)
document["nine"].bind("click", nine)


