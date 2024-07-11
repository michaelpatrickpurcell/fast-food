import numpy as np
from itertools import combinations, product
from scipy.special import comb

preferences_components = np.array([
[2,1,0],
[1,2,0],
[2,0,1],
[1,0,2],
[0,2,1],
[0,1,2],
])

preferences_component_pairs = list(product(preferences_components, repeat=2))
preferences_vectors = [np.concatenate(x) for x in preferences_component_pairs]

food_sets3 = combinations(np.arange(6), 3)
food_vectors3 = np.zeros((comb(6,3, exact=True), 6), dtype=int)
for i, x in enumerate(food_sets3):
    food_vectors3[i][np.array(x)] = 1

def compute_score(preferences_vector, food_vector):
    raw_score = preferences_vector @ food_vector
    if raw_score > 4:
        score = 1
    else:
        score = 0
    return score


if __name__ == "__main__":
    target_vector = preferences_vectors[np.random.choice(np.arange(len(preferences_vectors)))]

    print("I have chosen a secret target vector.")

    print("\nHere's a list of the possible target vectors I might have chosen:")
    for i,x in enumerate(preferences_vectors):
        print("%2i: %s" % (i,x))
              
    print("\nCan you guess what my secret target vector is?")
    print("Let's play and find out!")
    print("When you're ready to guess, type 'g' to continue.")

    guesses = []
    scores = []

    print("\nGive me some meals and I'll tell you what I like.")
    print("\nHere's a list of possible meals:")
    for i,x in enumerate(food_vectors3):
        print("%2i: %s" % (i,x))

    ans = 'n'
    while ans == 'n':
        print("\nWhich meal do you want to give me?")
        try:
            order_number = int(input())
            # print("You chose order number: %i" % order_number)
            food_vector = food_vectors3[order_number]
            guesses.append(food_vector)
            # print("That order number corresponds to the meal: %s" % food_vectors3[order_number])

            score = compute_score(target_vector, food_vector)
            scores.append(score)
            # print("I give that meal a score of: %i" % score)

            print("\nHere's a list of all of your guesses and the scores that I gave them:")
            for g,s in zip(guesses, scores):
                print("%s: %i" % (g,s))

        except:
            ans = 'y'

    print("\nHere's a list of the possible target vectors I might have chosen:")
    for i,x in enumerate(preferences_vectors):
        print(i,x)
 
    print("Enter the number for your guess:")
    index = int(input())

    if all(preferences_vectors[index] == target_vector):
        print("That's right! Good work.")
    else:
        print("Sorry, that's not right.")

    print("\nThe target vector was:")
    print(target_vector)