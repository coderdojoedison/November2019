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
    
def renderThanksGivingPieChart():
    thanksgivingfoodpie = pygal.Pie()
    thanksgivingfoodpie.title = 'Popular Thanksgiving Foods'
    
    file = open('/home/pi/Desktop/November2019/thanksgivingfood.txt', 'r')

    for line in file.read().splitlines():
      if line:
        label, value = line.split(' ')
        thanksgivingfoodpie.add(label, int(value))

    file.close()

    fileName = "thanksgivingfoodpie"
    createAndRender( thanksgivingfoodpie, fileName )

def renderThanksGivingBarChart():
    thanksgivingfoodbar = pygal.Bar()
    thanksgivingfoodbar.title = 'Popular Thanksgiving Foods'
    
    file = open('/home/pi/Desktop/November2019/thanksgivingfood.txt', 'r')

    for line in file.read().splitlines():
      if line:
        label, value = line.split(' ')
        thanksgivingfoodbar.add(label, int(value))

    file.close()

    fileName = "thanksgivingfoodbar"
    createAndRender( thanksgivingfoodbar, fileName )

def renderLCCSFoodPieChart():
    print ("inside lccs")
    lccsfoodpie = pygal.Pie()
    lccsfoodpie.title = 'lccsFoodPie'
    
    file = open('/home/pi/Desktop/November2019/lccsfood.txt', 'r')

    for line in file.read().splitlines():
      if line:
        label, value = line.split(' ')
        lccsfoodpie.add(label, int(value))

    file.close()

    fileName = "lccsfoodpie"
    createAndRender( lccsfoodpie, fileName )

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
    print("1 for Bar, 2 for Pie")
    user1Input = input("What kind of chart do you want to create? Bar Graph or Pie Chart")
    print("Enter: 1 is for typesofthanksgivingfood or 2 is for lccsFoodPie")
    userInput = input("Which chart do you want to draw? : ")
    userInput = userInput.lower()
    print("userInput ==", userInput)
    if (userInput == "2" and user1Input == "2"):
        renderLCCSFoodPieChart()
    elif (userInput == "1" and user1Input == "2"):
        renderThanksgivingFoodPieChart()
    elif (userInput == "2" and user1Input == "1"):
        renderLCCSFoodBarChart()
    elif (userInput == "1" and user1Input == "1"):
        renderThanksGivingBarChart()
        
getUserInput()
