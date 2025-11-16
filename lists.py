# Day 3 - Lists tasks (Justice League operations)
from pprint import pprint

print("\nInitial Justice League:")
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
pprint(justice_league)

print("\n1) Number of members:")
print(len(justice_league))

print("\n2) Add Batgirl and Nightwing:")
justice_league.append("Batgirl")
justice_league.append("Nightwing")
pprint(justice_league)

print("\n3) Move Wonder Woman to the beginning (index 0):")
# find her current index and move
if "Wonder Woman" in justice_league:
    justice_league.remove("Wonder Woman")
    justice_league.insert(0, "Wonder Woman")
pprint(justice_league)

print("\n4) Separate Aquaman and Flash by inserting someone between them:")
# Ensure both exist, then place 'Green Lantern' between them (or Superman if preferred)
# We'll choose "Green Lantern" as asked in task. We'll remove and reinsert to ensure ordering.
if "Aquaman" in justice_league and "Flash" in justice_league:
    # remove Green Lantern if it exists elsewhere so insertion is clean
    if "Green Lantern" in justice_league:
        justice_league.remove("Green Lantern")
    # find index of Aquaman, then insert after it
    aquaman_index = justice_league.index("Aquaman")
    justice_league.insert(aquaman_index + 1, "Green Lantern")
pprint(justice_league)

print("\n5) Replace existing list with new members:")
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
pprint(justice_league)

print("\n6) Sort the Justice League alphabetically and show new leader (0th index):")
justice_league.sort()
pprint(justice_league)
print("\nNew leader (index 0):", justice_league[0])

# BONUS: show predicted leader comment
print("\nBONUS Prediction:")
print("If we sort alphabetically, the hero at index 0 becomes leader.")
print("Based on the final list sorted, the new leader is:", justice_league[0])