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

def renderTypesOfPiesPieChart():
    typesofpiespie = pygal.Pie()
    typesofpiespie.title = 'Popular Types of Pie'
    
    file = open('/home/pi/Desktop/November2019/typesofpie.txt', 'r')

    for line in file.read().splitlines():
      if line:
        label, value = line.split(' ')
        typesofpiespie.add(label, int(value))

    file.close()

    fileName = "typesofpiespie"
    createAndRender( typesofpiespie, fileName )

def renderTypesOfJuiceBarChart():
    typesofjuicebar = pygal.Bar()
    typesofjuicebar.title = 'Popular Types of Juice'
    
    file = open('/home/pi/Desktop/November2019/typesofjuice.txt', 'r')

    for line in file.read().splitlines():
      if line:
        label, value = line.split(' ')
        typesofjuicebar.add(label, int(value))

    file.close()

    fileName = "typesofjuicebar"
    createAndRender( typesofjuicebar, fileName )

def renderTypesOfHolidayDrinksBarChart():
    typesofholidaydrinksbar = pygal.Bar()
    typesofholidaydrinksbar.title = 'Popular Types of Juice'
    
    file = open('/home/pi/Desktop/November2019/holidaydrinks.txt', 'r')

    for line in file.read().splitlines():
      if line:
        label, value = line.split(' ')
        typesofholidaydrinksbar.add(label, int(value))

    file.close()

    fileName = "typesofholidaydrinksbar"
    createAndRender( typesofholidaydrinksbar, fileName )

def renderTypesOfHolidayTreatsPieChart():
    typesofholidaytreatspie = pygal.Pie()
    typesofholidaytreatspie.title = 'Popular Types of Holiday Treats'
    
    file = open('/home/pi/Desktop/November2019/typesofholidaytreats.txt', 'r')

    for line in file.read().splitlines():
      if line:
        label, value = line.split(' ')
        typesofholidaytreatspie.add(label, int(value))

    file.close()

    fileName = "typesofholidaytreatspie"
    createAndRender( typesofholidaytreatspie, fileName )


def getUserInput():
    print("What kind of chart do you want to create?")
    print("Enter: TypesofThanksgivingFood for a pie chart on popular thanskgiving foods")
    print("Enter: TypesofPies for a pie chart on popular flavors  of pie")
    print("Enter: TypesofJuice for a bar chart on popular juice flavors")
    print("Enter: Typesofholidaydrinks for a bar chart on popular holiday drinks")
    print("Enter: TypesofHolidayTreats for a pie chart on popular Holiday Treats") 



    userInput = input("Type the name of the chart you wish to create: ") 
    userInput = userInput.lower() 
    if (userInput == "typesofthanksgivingfood"):
        renderThanksgivingFoodPieChart()
    elif (userInput == "typesofpies"):
        renderTypesOfPiesPieChart()
    elif (userInput == "typesofjuice"):
        renderTypesOfJuiceBarChart()
    elif (userInput == "typesofholidaydrinks"):
        renderTypesOfHolidayDrinksBarChart()
    elif (userInput == "typesofholidaytreats"):
        renderTypesOfHolidayTreatsPieChart() 
    
#call each of the functions to render

getUserInput()



    
                           
