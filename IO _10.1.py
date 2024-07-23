def ReadFile(fileName):
    try:

        with open(fileName, 'r') as file:#reading file
            print("file name is here: ",fileName)#trying to print file name
            for line in file:
                print(line.rstrip())
                
    except:
        print("File not found")

# Example usage:
fileName = "XYZ.txt"
ReadFile(fileName)


#file name is here:  XYZ.txt
#sanskruti pooja
