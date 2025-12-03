import time;

speed_type = "python is my favourite language" #The string that'll be typed
word_count = len(speed_type.split()) #Takes note of the length of word count when typing the string and the fact
#that it splits up to create separate words

while str(input('Type "yes" when you are ready!: ')):
    
    type1 = time.time() #The start time
    
    input_text = len(input('Enter the phrase "%s" as fast as possible' % speed_type))
    
    type2 = time.time() #The end time
    
    accuracy = input_text #Setting the accuracy of the speed typer
    accuracy = accuracy / word_count
   
    time_taken = type2 - type1 #Calculates the time taken
    wpm = word_count / time_taken #Calculates the words per minute
    
    print(wpm, accuracy, time_taken) #prints out the time taken and words per minute
