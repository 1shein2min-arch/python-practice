def result(name, score):

    if score >= 50:
        return f"{name} - Passed"
    else:
        return f"{name} - Failed"


print("===== Student Result =====")

name = input("Enter Name : ")
score = int(input("Enter Score : "))

answer = result(name, score)

print(f"Result : {answer}")