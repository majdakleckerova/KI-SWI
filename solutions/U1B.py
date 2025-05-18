import random

def get_winner(player_choice: str, ai_choice: str) -> str:
    if player_choice == ai_choice:
        return "draw"
    if (player_choice == "rock" and ai_choice == "scissors") or \
       (player_choice == "scissors" and ai_choice == "paper") or \
       (player_choice == "paper" and ai_choice == "rock"):
        return "player"
    return "ai"

def play_game():
    player_score = 0
    ai_score = 0

    while player_score < 3 and ai_score < 3:
        player_choice = input("rock, paper, scissors: ").lower()
        ai_choice = random.choice(["rock", "paper", "scissors"])
        winner = get_winner(player_choice, ai_choice)
        print(f"You chose {player_choice}, AI chose {ai_choice}. Result: {winner}")

        if winner == "player":
            player_score += 1
        elif winner == "ai":
            ai_score += 1
        
        print(f"Score - You: {player_score}, AI: {ai_score}")

    print("Game over!")

# play_game()  # Volání vypnuto pro testování