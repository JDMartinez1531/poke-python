import random
from enum import IntEnum

class Action(IntEnum):
    Charmander = 0
    Squirtle = 1
    Bulbasaur = 2

def get_trainer_selection():
  choices = [f"{action.name}[{action.value}]" for action in Action]
  choices_str = ", ".join(choices)
  selection = int(input(f"You're late! Your rival has already chosen their pokemon.\nThese are all I have left:\n({choices_str}.\nHurry and pick one to start your first battle!\n"))
  action = Action(selection)
  return action

def get_rival_selection():
  selection = random.randint(0, len(Action) - 1)
  action = Action(selection)
  return action

def determine_winner(trainer_action, rival_action):
    victories = {
        Action.Charmander: [Action.Bulbasaur],
        Action.Squirtle: [Action.Charmander],
        Action.Bulbasaur: [Action.Squirtle]
    }

    defeats = victories[trainer_action]
    if trainer_action == rival_action:
        print(f"Both trainers selected {trainer_action.name}. They give it their all, but they're too evenly matched. It's a tie!")
    elif rival_action in defeats:
        print(f"{trainer_action.name}'s type advantage is too much for {rival_action.name}! You win!")
    else:
        print(f"{rival_action.name}'s type advantage is too much for {trainer_action.name}! You lose...")

while True:
  try:
    trainer_action = get_trainer_selection()
  except ValueError as e:
    range_str = f"[0, {len(Action) - 1}]"
    print(f"Invalid selection. Enter a value in range {range_str}")
    continue

  rival_action = get_rival_selection()
  determine_winner(trainer_action, rival_action)

  play_again = input("Play again? (y/n): ")
  if play_again.lower() != "y":
    break