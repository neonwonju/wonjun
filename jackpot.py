import random

balance = int(input("초기 자금을 입력하세요 (10000원부터): "))
while True:
    if balance < 1:
        print("자금이 부족하여 게임을 종료합니다.")
        break

    bet = int(input("베팅 금액을 입력하세요: "))
    slots = [random.choice(['7', 'BAR', 'BELL', 'CHERRY', 'LEMON', 'ORANGE', 'cocoa']) for _ in range(3)]
    print("슬롯머신의 결과는", slots, "입니다.")

    if slots[0] == slots[1] == slots[2]:
        balance += bet * 10
        print("JACKPOT! 베팅 금액의 10배인", bet * 10, "원을 얻으셨습니다.")
    elif set(slots) == {'BAR'}:
        balance += bet * 5
        print("BAR! 베팅 금액의 5배인", bet * 5, "원을 얻으셨습니다.")
    elif slots.count('7') == 3:
        balance += bet * 3
        print("777! 베팅 금액의 3배인", bet * 3, "원을 얻으셨습니다.")
    elif slots.count('CHERRY') == 2:
        balance += bet * 2
        print("CHERRY! 베팅 금액의 2배인", bet * 2, "원을 얻으셨습니다.")
    elif 'CHERRY' in slots:
        balance += bet
        print("CHERRY! 베팅 금액과 같은", bet, "원을 얻으셨습니다.")
    else:
        balance -= bet
        print("아쉽습니다. 베팅 금액인", bet, "원을 잃으셨습니다.")

    print("현재 자금은", balance, "원입니다.")
    play_again = input("게임을 계속 하시겠습니까? (y/n): ")
    if play_again.lower() == 'n':
        print("게임을 종료합니다.")
        break
