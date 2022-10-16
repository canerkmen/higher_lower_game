import art
import game_data
import random
import os


def choiceFunc():
    return random.randint(0, len(game_data.data) - 1)


def printComparison(A, B):

    nameA = game_data.data[A].get("name")
    descriptionA = game_data.data[A].get("description")
    countryA = game_data.data[A].get("country")

    nameB = game_data.data[B].get("name")
    descriptionB = game_data.data[B].get("description")
    countryB = game_data.data[B].get("country")
  
    print("Compare A : " + nameA + ", a " + descriptionA + " from " + countryA)
    print(art.vs)
    print("Against B : " + nameB + ", a " + descriptionB + " from " + countryB)


def dataComparison(A, B, answer):
    if game_data.data[A].get("follower_count") >= game_data.data[B].get("follower_count") and answer == 'a':
        return 1
    elif game_data.data[B].get("follower_count") > game_data.data[A].get("follower_count") and answer == 'b':
        return 2
    return 0


def chooseComparison(A):

    B = choiceFunc()
    while A == B:
        B = choiceFunc()
    return B

def answerFunc():
  
    answer = ""
    while answer.lower() != 'a' and answer.lower() != 'b':
        answer = input("Who has more follower ? Type 'A' or 'B' : ")
    answer = answer.lower()
    return answer

final_result = 0
finish = False
A = choiceFunc()
B = chooseComparison(A)

while finish == False:
    print(art.logo)
    print(f"Your Current Score : {final_result}")
    printComparison(A, B)
    answer = answerFunc()
    if dataComparison(A, B, answer) == 0:
        finish = True
    elif dataComparison(A, B, answer) == 1:
        B = chooseComparison(A)
        final_result += 1
    elif dataComparison(A, B, answer) == 2:
        temp = chooseComparison(B)
        A = B
        B = temp
        final_result += 1

    os.system("cls")

print(f"Your final score : {final_result}")
