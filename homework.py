# 1. The Range Riddle

# Task 1: Your Mood Today
moods = ["happy", "sad", "energetic", "calm"]
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
import random
for i in range(len(days)):
    random.choice(moods)
    print(f"on {days[i]}, you were feeling {random.choice(moods)}")

# 2. Double Scoop with Nested Loops

#Task 1: Your Mood Tracker
time_of_day = ["morning", "evening", "night"]
for i in range(len(days)):
    for d in range(len(time_of_day)):
        print(f"On {days[i]} {time_of_day[d]} I was feeling {random.choice(moods)}")

# 3. Loop Condition Logic

# Task 1: Loop Condition Exploration
iterations = 0
while True:
    print("never ends")
    iterations += 1
    if iterations >= 5:
        break

# Task 2: Conditional Exit

iterations = 0
while iterations < 10:
    iterations += 1
    print("ends now")
    iterations >= 10

# 4. Python's Random Game Night
list_of_items = ["sword", "shield", "armor", "wand", "potion"]
picked = random.choice(list_of_items)
guess = input("Guess the item:")
if guess == picked:
    print("Yay, you got it right")
else:
    print("Oh no! Try again.")

# 5. Looping Lists - The Rhythm of Repetition

# Task 1: The for Loop DJ Set
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
message = ("you love this!", "it's so loud!", "is a good choice!", "is boring!")
for i in range(len(genres)):
    track = i + 1
    print(f"Listening to {track}, genre is {genres[i]} {message[i]}")


# Task 2: The Remix Artist with while
song_number = 1
while song_number <= len(genres):
    song = random.choice(genres)
    print(f"Track {song_number}: in {song}, that's {random.choice(message)}!")
    if  song == 'Hip-hop':
        print("Playlist stopped because you don't like Hip hop")
        break
    song_number += 1

# Task 3: Light Show Technician Loop
for i in range(len(genres)):
    track = i + 1
    if genres[i] == 'Classical':
        print(f"{genres[i]} is not suitable for a light show...")
        continue
    print(f"Track {track}: for {genres[i]}, the light show is ready!")
        
# 6. Advanced Looping Techniques

# Task 1: The Selective DJ      
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
sublist = genres[1:4]
print(sublist)

# Task 2: The One-Liner Band with List Comprehensions
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
music_list = [music + " music" for music in genres]
print(music_list)

# Task 3: Munerical beats with range
for beat in range(10, 0, -1):
    if beat == 1:
        print(f"{beat} The beat drops now!")
else:
    print(beat)
