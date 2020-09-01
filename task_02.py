def task2(input_value, min, max):
    while(input_value < min or input_value > max):


        while True:
            input_value = input("Input a number in range " + str(min) + " to " + str(max) + ": ")
            try:
                input_value = float(input_value)
                break
            except TypeError:
                print("Not a number! Try again!")
            except ValueError:
                print("Not a number! Try again!")


        if (input_value < min) or (input_value > max):
            print("The number is out of range. Try again!")
