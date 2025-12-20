try:
    #Tried to write file
    file = open("data.txt", "w")
    file.write("Learning Python step by step\n")
    file.write("Day 7: File handling and errors\n")
    file.close()

    #Tried to append file
    file = open("data.txt", "a")
    file.write("Appended file\n")
    file.close()

    #Tried to read file
    file = open("data.txt", "r")
    content = file.read()
    print(content)
    file.close()

except Exception as e:
    print("An error occured:", e)