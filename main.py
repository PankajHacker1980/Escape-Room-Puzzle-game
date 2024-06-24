import random

class EscapeRoom:
    def __init__(self):
        self.puzzles = [
            self.puzzle1,
            self.puzzle2,
            self.puzzle3,
            self.puzzle4,
            self.puzzle5
        ]
        self.current_puzzle = random.choice(self.puzzles)
        self.completed_puzzles = set()
        self.max_attempts = 3
    
    def puzzle1(self):
        # Example puzzle: Word Jumble
        words = ["python", "algorithm", "programming", "code", "challenge"]
        secret_word = random.choice(words)
        scrambled_word = self.scramble_word(secret_word)
        
        print(f"Unscramble the word: {scrambled_word}")
        for attempt in range(self.max_attempts):
            guess = input("Your guess: ").strip().lower()
            if guess == secret_word:
                print("Correct! You unlocked the first puzzle.")
                return True
            else:
                print("Incorrect guess. Try again.")
        print(f"Sorry, you've run out of attempts. The word was '{secret_word}'.")
        return False
    
    def puzzle2(self):
        # Example puzzle: Math Puzzle
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        correct_answer = num1 + num2
        
        print(f"What is the sum of {num1} and {num2}?")
        for attempt in range(self.max_attempts):
            try:
                guess = int(input("Your answer: "))
                if guess == correct_answer:
                    print("Correct! You unlocked the second puzzle.")
                    return True
                else:
                    print("Incorrect answer. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        print(f"Sorry, you've run out of attempts. The correct answer was {correct_answer}.")
        return False
    
    def puzzle3(self):
        # Add more puzzles as needed
        pass
    
    def scramble_word(self, word):
        scrambled = list(word)
        random.shuffle(scrambled)
        return ''.join(scrambled)
    
    def play_game(self):
        print("Welcome to the Escape Room Puzzle!")
        print("Solve each puzzle to escape the room.")
        
        while len(self.completed_puzzles) < len(self.puzzles):
            puzzle_solved = self.current_puzzle()
            if puzzle_solved:
                self.completed_puzzles.add(self.current_puzzle)
                if len(self.completed_puzzles) < len(self.puzzles):
                    print("Well done! Moving on to the next puzzle.")
                    self.current_puzzle = random.choice([puzzle for puzzle in self.puzzles if puzzle not in self.completed_puzzles])
        
        print("Congratulations! You've solved all puzzles and escaped the room.")

if __name__ == "__main__":
    game = EscapeRoom()
    game.play_game()
