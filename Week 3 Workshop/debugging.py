score = float(input("Enter score: "))
if score > 100 or score < 0:
    print('Invalid score')
else:
    if score >= 90:
        print('Excellent')

    if score >= 50 and score <= 89:
        print("Passable")

    if score <= 49:
        print("Bad")

# score < 0 and score > 100:
