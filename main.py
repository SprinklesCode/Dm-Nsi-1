import random
import math


def tema_le_jeu():
    #initialisation des variables pour le nombre de boules de départ
    white_balls = 25
    black_balls = 25
    red_balls = 2
    green_balls = 1
    #initialisations des variables pour le nombre de boules récuperé
    white_pick = 0
    black_pick = 0
    green_pick = 0
    #initialisation de la variable qui va compter le nombre de coups dans la partie
    count = 0

    #ma boucle de jeu qui dit que tant qu'on a pas récuperer 13 boule noir on continue (et on compte chaque boule verte comme une boule noire egalement)
    while black_pick + green_pick < 12:
        #on compte le nombre de tours
        count += 1
        #pour les calculs on défini une variable qui nous donne le nombre total de boule encore en jeu
        all_balls = white_balls + black_balls + green_balls + red_balls
        #on donne une proba de tirage pour chaque boule apres chaque tour
        probas = [white_balls/all_balls, black_balls/all_balls, red_balls/all_balls, green_balls/all_balls]
        #on choisi la couleur de la boule tirer de maniere aléatoire en prenant en compte les probas
        ball = random.choices(["white", "black", "red", "green"], weights=probas)[0]
        #bille blanche → mise de côté, on ajoute 1 a boule tirer (white pick) et on enleve 1 au total des boules blanches
        if ball == "white":
            white_balls -= 1
            white_pick += 1
        #bille noire → mise de côté et on remet toutes les billes blanches dans le sac, donc on reinitialise les deux variables qui correspondent
        # aux boules blanches et on ajoute la boule noire de la meme manière que la blanche
        elif ball == "black":
            white_balls = 25
            white_pick = 0
            black_balls -= 1
            black_pick += 1
        #bille rouge → on remet la bille rouge dans le sac ainsi que la moitié des billes
        #noires mises de côtés arrondie au supérieur. (sauf bille verte), meme chose que bille blanche mais avec la moitié arrondi au superieur + on ne touche pas aux billes 
        # rouges car elle re part direct dans le sac
        elif ball == "red":
            black_balls = black_balls + math.ceil(black_pick / 2)
            black_pick -= math.ceil(black_pick / 2)
        #Bille verte → on remet toutes les billes noires. La bille verte est ensuite mise de
        #côté et compte comme une bille noire acquise définitivement. donc on reinitialise les deux variables qui correspondent
        # aux boules noires et on ajoute la boule verte de la meme manière que la blanche
        elif ball == "green":
            green_pick += 1
            green_balls -= 1
            black_balls = 25
            black_pick = 0
    #on retourne count qui a compter le nombre de tour avant que l'on puisse sortir de la boucle
    return count


def main():
    while True:
        try:
            #on demande le nombre N de parties que l'on veut simuler
            N = int(input('Combien de parties voulez-vous simuler ? '))
            if N > 0:
                break
            else:
                print("Veuillez entrer un nombre positif.")
        #on prend en compte le prof qui va essayer de casser le jeu
        except ValueError:
            print("Veuillez entrer un nombre valide.")

    #on initialise la variable qui comptera le nombre de coup de toute les parties
    total_moves = 0
    #on simule N partie, et on incrémente total_moves de ce que retourne ma fonction de jeu (donc le nombre de coup qu'il a fallu)
    for i in range(N):
        total_moves += tema_le_jeu()

    #enfin on divise le total de coups par le nombre de partie pour obtenir une approximation de combien de coups il faudra pour qu'une partie se fasse en moyenne
    average_moves = total_moves / N
    #on print le résultat
    print(f"Nombre moyen de coups pour gagner en {N} parties : {average_moves:.2f}")

#fonction conventionnelle de début de script qui nous redirige vers la fonction main()
if __name__ == "__main__":
    main()
