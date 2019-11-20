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




    
def renderThanksgivingFoodPieChart():
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


def getUserInput():
    print("What kind of chart do you want to create?")
    print("Enter: TypesofThanksgivingFood for a pie chart on popular thanskgiving foods")
    userInput = input("Which chart do you want to draw? : ")
    userInput = userInput.lower() 
    if (userInput == "typesofthanksgivingfood"):
        renderThanksgivingFoodPieChart()
        
getUserInput() 
