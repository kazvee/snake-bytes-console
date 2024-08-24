from greet_user import greet_user
from shuffle_meals import shuffle_meals
from input_is_valid import input_is_valid

greet_user()

def quit_and_restart(user_input):
  if user_input.upper() == "Q":
    print("\nRestarting the meal planning process...\n")
    return True
  return False

def main():
  while True:
    meal_ideas = []

    while len(meal_ideas) < 6:
      user_input = input(
          "Enter a dinner meal idea, or `Q` to quit and restart: \n")

      if quit_and_restart(user_input):
        break

      if input_is_valid(user_input):
        meal_ideas.append(user_input)
      else:
        print(
            "Invalid input. Meal ideas cannot be blank or contain only numbers. Please try again.\n"
        )
    else:
      meal_ideas.append(
          "Treat Night - Visit or order from your favorite restaurant")

      shuffled_meals = shuffle_meals(meal_ideas)

      days_of_week = [
          "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
          "Sunday"
      ]

      print("\nYour randomly-generated dinner plans for the week are:\n")
      for day, meal in zip(days_of_week, shuffled_meals):
        print(f"{day}: {meal}")

      print("\nThank you for using Snake Bytes Dinner Planner!")
      restart_input = input(
          "\nEnter `R` to restart the meal planning process, or enter any other character to exit: \n"
      )

      if restart_input.upper() == "R":
        print("\nRestarting the meal planning process...\n")
        continue
      else:
        print("\nExiting...\n")
        break

if __name__ == "__main__":
  main()