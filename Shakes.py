import pygal
import webbrowser
import svgwrite


def createAndRender( chart, fileName ):

    svgFileName = fileName +".svg"
    chart.render_to_file( svgFileName)

    dwg = svgwrite.Drawing(svgFileName, profile='tiny', chart)
    dwg.add(dwg.text( 'Our Shakes!',
                          insert=(21,30),
                          stroke='none',
                          fill=svgwrite.rgb(15,15,15, '%'),
                          font_size='15px',
                          font_weight="bold")
    )

    
    dwg.save(svgFileName)
    

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


def rendertypesofshakes():
    typesofshakespie = pygal.Pie(height=300)
    typesofshakespie.title = 'Popular Shakes! (Percent)'
    print ("Our Shakes!" )
    print ("Oreo Monster - Oreos, Vanilla Icecream, Whipped Cream, Fudge, Milk")
    print ("Red Panda - Strawberry, Vanilla Icecream, Oreo bits, Whipped Cream, Milk")
    print ("Chocoloco - Chocolate Cream, Milk, Whipped Cream, Fudge")
    print ("Berry Cream - Strawberry, Blue Berry, Blackberry, Vanilla Ice Cream, Milk, Whipped Cream")
    print ("Peanut Butter - Peanut Butter, Vanilla/Chocolate Icecream, Milk, Whipped Cream, Milk, Fudge")
    file = open('/home/pi/Desktop/November2019/typesofshakes.txt','r')
    for line in file.read().splitlines():
        if line:
            label, value = line.split(' ')
            typesofshakespie.add(label, int(value))
    file.close()
    fileName = "typesofshakespie"
    createAndRender(typesofshakespie, fileName)

rendertypesofshakes() 
