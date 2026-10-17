import random
choices = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0
ties = 0

def get_computer_choice():
    """Computer picks randomly."""
    return random.choice(choices)

def determine_winner(player, computer):
    """Figure out who wins."""
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "player"
    else:
        return "computer"

def show_result(player, computer, result):
    """Display the round result with emojis."""
    emoji = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}
    
    print(f"\n  You chose:      {emoji[player]}  {player}")
    print(f"  Computer chose: {emoji[computer]}  {computer}")
    
    if result == "tie":
        print("  It's a tie! 🤝")
    elif result == "player":
        print("  You win! 🎉")
    else:
        print("  Computer wins! 🤖")

def show_scoreboard():
    """Display the current scores."""
    print(f"\n  📊 SCOREBOARD")
    print(f"  You:       {player_score}")
    print(f"  Computer:  {computer_score}")
    print(f"  Ties:      {ties}")

def show_history(history):
    """Show all rounds played."""
    if not history:
        print("\n  No rounds played yet!")
        return
    
    print(f"\n  📜 ROUND HISTORY")
    print("  " + "-" * 40)
    for i, round_info in enumerate(history, start=1):
        p = round_info["player"]
        c = round_info["computer"]
        r = round_info["result"].upper()
        print(f"  Round {i}: You={p}  Computer={c}  → {r}")
    print("  " + "-" * 40)



round_history = []

print("=" * 42)
print("    ROCK  PAPER  SCISSORS")
print("=" * 42)
print("  Type: rock, paper, or scissors")
print("  Type 'score' to see scoreboard")
print("  Type 'history' to see round history")
print("  Type 'quit' to stop playing")

while True:
    player_choice = input("\n  Your choice: ").lower().strip()
    
    if player_choice == "quit":
        print("\n  Final Scores:")
        show_scoreboard()
        if player_score > computer_score:
            print("  🏆 You are the champion!")
        elif computer_score > player_score:
            print("  🤖 Computer wins overall!")
        else:
            print("  🤝 It's an overall tie!")
        print("\n  Thanks for playing!")
        break
    
    elif player_choice == "score":
        show_scoreboard()
        continue
    
    elif player_choice == "history":
        show_history(round_history)
        continue
    
    elif player_choice not in choices:
        print("  Invalid choice! Pick rock, paper, or scissors.")
        continue
    

    computer_choice = get_computer_choice()
    result = determine_winner(player_choice, computer_choice)
    
    
    if result == "player":
        player_score += 1
    elif result == "computer":
        computer_score += 1
    else:
        ties += 1
    
    
    round_history.append({
        "player": player_choice,
        "computer": computer_choice,
        "result": result
    })
    
    
    show_result(player_choice, computer_choice, result)
    show_scoreboard()