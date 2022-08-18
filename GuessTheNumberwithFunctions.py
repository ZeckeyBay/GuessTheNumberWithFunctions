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
    while feedback != "c":
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f"Tahmininim {guess} çok mu yüksek (H) yoksa çok mu az (L), yoksa doğrumu(C)?").lower()
        if feedback == "h":
             high = guess -1
        elif feedback == "l":
            low = guess +1
    print(f"Tahmin ettiğin sayıyı,{guess} buldun!")
computer_guess(100)
