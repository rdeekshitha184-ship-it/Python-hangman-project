import random

# ------------------------------
# ASCII HANGMAN STAGES
# ------------------------------
HANGMAN_PICS = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """
]

# ------------------------------
# WORD CATEGORIES
# ------------------------------
categories = {
    "animals": ["tiger", "elephant", "rabbit", "giraffe", "panda", "monkey", "zebra"],
    "fruits": ["apple", "banana", "mango", "orange", "papaya", "grapes"],
    "technology": ["python", "laptop", "internet", "keyboard", "software", "program"],
    "countries": ["india", "france", "brazil", "japan", "canada", "germany"],
    "school": ["teacher", "notebook", "library", "student", "classroom"],
}

# ------------------------------
# CHOOSE CATEGORY
# ------------------------------
print("🎯 Welcome to HANGMAN with Categories!")
print("\nAvailable categories:")

for category in categories:
    print(" -", category)

chosen_category = input("\nChoose a category: ").lower()

while chosen_category not in categories:
    chosen_category = input("❌ Invalid category. Choose again: ").lower()

# Pick random word
word = random.choice(categories[chosen_category])
guessed = ["_"] * len(word)
attempts = len(HANGMAN_PICS) - 1
used_letters = []

print(f"\n📌 Category selected: {chosen_category.upper()}")
print("🔤 Word to guess:", "_ " * len(word))

# ------------------------------
# GAME LOOP
# ------------------------------
while attempts >= 0:
    print(HANGMAN_PICS[len(HANGMAN_PICS) - 1 - attempts])
    print("Word:", " ".join(guessed))
    print("Attempts left:", attempts)
    print("Used letters:", ", ".join(used_letters))

    guess = input("\nEnter a letter: ").lower()

    # Validation
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Enter only a single letter!")
        continue

    if guess in used_letters:
        print("⚠️ You've already used this letter!")
        continue

    used_letters.append(guess)

    # Check if correct
    if guess in word:
        print("✔️ Correct letter!")
        for i, ch in enumerate(word):
            if ch == guess:
                guessed[i] = guess
    else:
        print("❌ Wrong guess.")
        attempts -= 1

    # Win condition
    if "_" not in guessed:
        print("\n🎉 YOU WON! The word was:", word)
        break

# Lose condition
if "_" in guessed:
    print(HANGMAN_PICS[-1])
    print("\n💀 GAME OVER! The word was:", word)
