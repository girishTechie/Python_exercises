Lucky = 9
Guess = 5

if Guess < Lucky-2 :
    print("Too Low")
elif Guess > Lucky+2 :
    print("Too High")
elif Guess == Lucky :
    print("Correct Answer")
elif (Guess >= Lucky-2) and (Guess <= Lucky+2):
    print("Almost There")
