def main():
    score = float(input("Enter score: "))
    print(new_function(score))


def new_function(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()