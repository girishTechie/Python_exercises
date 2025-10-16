Lucky = 9
Guess = int(input("what is your Lucky number? "))

if Guess > Lucky+2 :
    print("TOO HIGH")
if Guess < Lucky-2 :
    print("TOO LOW")
if Guess == Lucky:
    print("Correct Answer")
if (Guess >= Lucky-2) and (Guess <= Lucky+2):
    print("Almost There")
