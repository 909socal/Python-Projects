import urllib
def read_text():
    quotes=open("C:\Users\Admin\Desktop\Computer Science\Python/Profanity_check.txt")
    contents_of_file=quotes.read()
    #print (contents_of_file)
    quotes.close()
    profanity_check(contents_of_file)

def profanity_check(text_to_check):
    connection=urllib.urlopen("http://www.wdyl.com/profanity?q"+text_to_check)
    output=connection.read()
    connection.close()
    
    if "true" in output:
        print("PROFANITY ALERT!!!")
    elif "false" in output:
        print("This Document Has No Curse Words")
    else:
        print("Could Not Read File Properly")
        
read_text()
