
class BowlingGame:
    def __init__(self):
        self.rolls = []  # Get a list to store all rolls

    def roll(self, pins: int):
        self.rolls.append(pins)

    def score_total(self) -> int:
        """Calculates and returns the total game score."""
        total_score = 0
        roll_index = 0

        for frame in range(10):
            if self.is_strike(roll_index):
                total_score += 10 + self.strike_bonus(roll_index)
                roll_index += 1
            elif self.is_spare(roll_index):
                total_score += 10 + self.spare_bonus(roll_index)
                roll_index += 2
            else:
                total_score += self.sum_of_balls_in_frame(roll_index)
                roll_index += 2

        return total_score

    def is_strike(self, roll_index: int) -> bool:
        return self.rolls[roll_index] == 10

    def is_spare(self, roll_index: int) -> bool:
        return self.rolls[roll_index] + self.rolls[roll_index + 1] == 10

    def strike_bonus(self, roll_index: int) -> int:
        return self.rolls[roll_index + 1] + self.rolls[roll_index + 2]

    def spare_bonus(self, roll_index: int) -> int:
        return self.rolls[roll_index + 2]

    def sum_of_balls_in_frame(self, roll_index: int) -> int:
        return self.rolls[roll_index] + self.rolls[roll_index + 1]


# Test Cases
def main():
    # Test 1: A gutter game (20 times 0 pin) should score 0
    game = BowlingGame()
    for _ in range(20):
        game.roll(0)
    print("Gutter game score:", game.score_total())  # Expected: 0

    # Test 2: An all one game (20 times 1 pin) should score 20
    game = BowlingGame()
    for _ in range(20):
        game.roll(1)
    print("All ones score:", game.score_total())  # Expected: 20

    # Test 3: A spare followed by a 3 should score 16
    game = BowlingGame()
    game.roll(5)
    game.roll(5)
    game.roll(3)
    for _ in range(17):
        game.roll(0)
    print("Spare followed by 3 score:", game.score_total())  # Expected: 16

    # Test 4: A strike followed by a 3 and a 4 should score 24
    game = BowlingGame()
    game.roll(10)
    game.roll(3)
    game.roll(4)
    for _ in range(16):
        game.roll(0)
    print("Strike followed by 3 and 4 score:", game.score_total())  # Expected: 24

    # Test 5: The perfect game (12 times 10) should score 300
    game = BowlingGame()
    for _ in range(12):
        game.roll(10)
    print("Perfect game score:", game.score_total())  # Expected: 300


if __name__ == "__main__":
    main()
