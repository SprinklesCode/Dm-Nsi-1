import random
import math


def tema_le_jeu():
    white_balls = 25
    black_balls = 25
    red_balls = 2
    green_balls = 1
    white_pick = 0
    black_pick = 0
    green_pick = 0
    count = 0

    while black_pick + green_pick < 12:
        count += 1
        all_balls = white_balls + black_balls + green_balls + red_balls
        probas = [white_balls/all_balls, black_balls/all_balls, red_balls/all_balls, green_balls/all_balls]
        ball = random.choices(["white", "black", "red", "green"], weights=probas)[0]
        if ball == "white":
            white_balls -= 1
            white_pick += 1
        elif ball == "black":
            white_balls = 25
            white_pick = 0
            black_balls -= 1
            black_pick += 1
        elif ball == "red":
            black_balls = black_balls + math.ceil(black_pick / 2)
            black_pick -= math.ceil(black_pick / 2)
        elif ball == "green":
            green_pick += 1
            green_balls -= 1
            black_balls = 25
            black_pick = 0
    return count


def main():
    while True:
        try:
            N = int(input('Combien de parties voulez-vous simuler ? '))
            if N > 0:
                break
            else:
                print("Veuillez entrer un nombre positif.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

    total_moves = 0
    for i in range(N):
        total_moves += tema_le_jeu()

    average_moves = total_moves / N
    print(f"Nombre moyen de coups pour gagner en {N} parties : {average_moves:.2f}")


if __name__ == "__main__":
    main()
