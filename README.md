# guess_number

#  Guess The Number (Python CLI Game)

A simple command-line number guessing game built with Python.  
The player selects a difficulty level and tries to guess a randomly generated number within a limited number of attempts.

---

##  Features

-  Multiple difficulty modes (Easy, Medium, Hard)
-  Random number generation
-  Smart hint system (range-based hints)
-  Hints get more accurate after each wrong guess
-  Limited attempts per game
-  Clean CLI gameplay experience

---

## How It Works

1. The player chooses a difficulty level.
2. The game generates a random number within a specific range.
3. A hint is shown as a **number range**.
4. Each wrong guess:
   - reduces the remaining attempts
   - makes the hint range smaller (more helpful)
5. The game ends when:
   - the player guesses correctly 
   - or runs out of attempts 

---

## Difficulty Levels

| Mode   | Range      | Attempts | Hint Radius |
|--------|-----------|----------|-------------|
| Easy   | 1 – 50    | 10       | Large       |
| Medium | 1 – 100   | 5        | Medium      |
| Hard   | 1 – 200   | 3        | Small       |

---

## Requirements

- Python 3.x

---

##  How to Run

```bash
python guess_number.py
```
---
## Example Gameplay

```bash
Welcome to Guess Number

Select your difficulty
1. Easy
2. Medium
3. Hard

Enter choice (1/2/3): 2

hints: (34, 48)
Guess the number from (1 to 100): 40
------------------------------
You guessed the wrong number
4 attempt(s) left.
```
---
## Core Function

```bash
def hints(secret, R, min_val, max_val):
    low = max(min_val, secret - R)
    high = min(max_val, secret + R)
    return low, high
```

