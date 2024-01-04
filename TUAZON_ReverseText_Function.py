while True:
    user_input = input("Enter a string: ")

    if user_input.isalpha():
        reversed_string = user_input[::-1]
        print("Output:", reversed_string)
        break
    else:
        print("Error Reported! Enter text only.")