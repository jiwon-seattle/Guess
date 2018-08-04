from random import randint

ANSWER = randint(0, 9)

i = 4
while i >= 1:
    guess = int(input("기회가 %d번 남았습니다. 1-20 사이의 숫자를 맞춰보세요." % i))
    if ANSWER < guess:
        print("Up")
    elif ANSWER > guess:
        print("Down")
    elif ANSWER == guess:
        print("축하합니다. %d번만에 숫자를 맞추셨습니다." % (5 - i))
        break
    i = i - 1
else:
    print("아쉽습니다. 정답은 %d였습니다." % ANSWER)
