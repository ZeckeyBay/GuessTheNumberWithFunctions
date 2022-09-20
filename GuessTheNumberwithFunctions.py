import random
#You guess here
def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"1 ile {x} arasında bir sayı tahmin et:"))
        if guess < random_number:
            print("Tahminini arttır")
        elif guess > random_number:
            print("Tahminini azalt")
    print(f" Tebrikler, sayıyı buldun. Sayımız: {random_number}")
guess(100)
#Computer tries to guess your number
def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "D":
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f"Tahmininim {guess} çok mu yüksek (Y) yoksa çok mu az (A), yoksa doğrumu(D)?").lower()
        if feedback == "Y":
             high = guess -1
        elif feedback == "A":
            low = guess +1
    print(f"Tahmin ettiğim sayıyı,{guess} buldun!")
computer_guess(100)
