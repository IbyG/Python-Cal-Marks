print("This is a program that you type in your score then the score it is out of and finally its percentage weighting\n"
      "to get your overall mark e.g. \n "
      "Mark: 12\n"
      " Out off: 15\n"
      " percentage: 5")

def asking():
    x = str(input("do you want to start the program (y or n)\n"))
    return x


# amount_of_inputs = int(input("How many marks are you going to input?\n"))

def clear():  # this clears the screen but keeps going
    print(' \n' * 100)


def working_out(main, outoff, percentage):  # this is to calculate the mark overall percentage e.g. 13/15 * 5
    global ontop
    global weighting
    weighting = percentage
    ontop = ((main / outoff) * percentage)
    total = ((main / outoff) * percentage)
    print(round(total, 2), "/", percentage)  # rounded to two decimal places
    return total


def overall_addition(x, y):  # this is the overall mark the person is getting
    global total
    global total1
    global text_file_copy #this is used to include into the
    total = total + x
    total1 = total1 + y
    print("overall you are getting", round(total, 2), "/", total1)  # rounded to two decimal places

x1 = asking()
total = 0
total1 = 0
f = open('resulting.txt', 'a') # PART OFWRIGHTING TOTHEFILE
while x1 == "y" or x1 == "Y":  # this while statement calls the references and asks if to continue
    num1 = float(input("Mark: "))
    Outoff = int(input("over: "))
    Weighting = int(input("weighing: "))
    a = working_out(num1, Outoff, Weighting)
    # working_out(num1, Outoff, Weighting)
    overall_addition(ontop, weighting)

    text_file_copy = round(total, 2), "/", total1
    f.write(str(ontop) + " / " + str(weighting) + "\n" + str(text_file_copy) + "\n")# THIS IS NEW TO WRITE TO A FILE

    x1 = input("do you want to do it again(y or n or clear) \n")
    if x1 == "clear" or x1 == "Clear":
        print(" \n" * 100)
        x1 = input("do you want to do it again(y or n or clear) \n")
    if x1 == "N" or x1 == "n":
        f.close() #PART OF WRITING TO A TEXT FILE   https://stackoverflow.com/questions/4706499/how-do-you-append-to-a-file  the ebsite
        exit()
    if x1 == "" or x1 == "":
        x1 = input("do you want to do it again(y or n or clear) \n")
    if x1 != "y" or x1 != "y":
        if x1 != "N" or x1 != "N":
            if x1 != "Clear" or x1 != "clear":
                x1 = input("do you want to do it again(y or n or clear) \n")










