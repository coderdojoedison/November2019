import pygal
import webbrowser

def createAndRender( chart, fileName ):

    svgFileName = fileName +".svg"
    chart.render_to_file( svgFileName)           
    htmlFileName = fileName + ".html"
                
    txt1 =  "<!DOCTYPE html><html><head></head><body><figure><embed type=\"image/svg+xml\" src= "
    txt2 = " </figure><body></html>"
    htmlSrc = txt1 +  svgFileName + txt2
    print("\n htmlsrc ")
    print( htmlSrc )
    print("\n htmlsrc ")
    with open(htmlFileName, "w") as htmlFile:
            htmlFile.write( htmlSrc)
    
    webbrowser.open(htmlFileName, new=2)
    

def renderLCCSFoodBarChart():
    print ("inside lccs")
    lccsfoodbar = pygal.Bar()
    lccsfoodbar.title = 'lccsFoodPie'
    
    file = open('/home/pi/Desktop/November2019/lccsfood.txt', 'r')

    for line in file.read().splitlines():
      if line:
        label, value = line.split(' ')
        lccsfoodbar.add(label, int(value))

    file.close()

    fileName = "lccsfoodbar"
    createAndRender( lccsfoodbar, fileName )

def getUserInput():
   # print("Enter: 1 is for typesofthanksgivingfood or 2 is for lccsFoodPie")
    #userInput = input("Which chart do you want to draw? : ")
    #userInput = userInput.lower()
    #print("userInput ==", userInput)

    label1 = input("label1 ? : ")
    value1 = input("value1 ? : ")

    label2 = input("label2 ? : ")
    value2 = input("value2 ? : ")

    label3 = input("label3 ? : ")
    value3 = input("value3 ? : ")

    label4 = input("label4 ? : ")
    value4 = input("value4 ? : ")

    label5 = input("label5 ? : ")
    value5 = input("value5 ? : ")

    lccsfoodbar = pygal.Bar()
    lccsfoodbar.title = 'lccsFoodBar'
    lccsfoodbar.add(label1, int(value1))
    lccsfoodbar.add(label2, int(value2))
    lccsfoodbar.add(label3, int(value3))
    lccsfoodbar.add(label4, int(value4))
    lccsfoodbar.add(label5, int(value5))

    fileName = "lccsfoodbar"
    createAndRender( lccsfoodbar, fileName )
    
getUserInput()
