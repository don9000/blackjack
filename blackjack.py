import random


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cpu_cards = []
player_cards = []


invitation = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
if invitation == "y":
    cpu_cards = random.sample(cards, 2)
    sum_of_cpu = sum(cpu_cards)
    player_cards = random.sample(cards, 2)
    sum_of_player = sum(player_cards)

    print(f"cpu drew {cpu_cards[1]} and player drew {player_cards}")
    print(f"the sum of the cards in playes hand is {sum_of_player}")

    if sum_of_player == 21:
        print("You Win!")
    else:
        hit_me = input("Would you like another card? (y/n): ")   
    if hit_me == "y":
        while hit_me == "y":
            if sum_of_player < 21:
                next_card_dealt = random.sample(cards, 1)
                next_card = next_card_dealt[0]
                player_cards.append(next_card)
                sum_of_player = sum(player_cards)
                print(f"The next card value is {next_card}, taking your total to {sum_of_player}")
            if sum_of_player < 21:
                hit_me = input("Would you like another card? (y/n): ") 
            else:
                if sum_of_player > 21:
                    print(f"Your total is {sum_of_player}, you lose")
                hit_me = "n"    

    if sum_of_player == 21:
        print("YOU WIN!!")

    elif sum_of_player <21:    
        print(f"You have decided to stay at {sum_of_player} ")    
        while sum_of_cpu < sum_of_player:
            next_card_dealt = random.sample(cards, 1)
            next_card = next_card_dealt[0]    
            cpu_cards.append(next_card)
            sum_of_cpu = sum(cpu_cards)
            print(f"The cpu total is {sum_of_cpu} ")
        if sum_of_cpu > sum_of_player and sum_of_cpu <= 21:
            print(f"CPU total is {sum_of_cpu} and your total is {sum_of_player}, CPU WINS")    
        else:
            print(f"CPU total is {sum_of_cpu} and your total is {sum_of_player}, YOU WIN!!") 
else:
    print("OK, goodbye")    

   







