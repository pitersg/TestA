#IMPORT Libraries
from AuxFunctions import *

#Setup input Variables
url="https://automationpractice.com"
List= ListArticles(url)


#Link Test cases to functions
TC1= SetupConnection(url)
TC2= SearchArticle(url,'Blouse')
TC3= SearchArticle(url,'Gucci Shoes')
TC4= CheckItemFields(url,List)
TC5= AddItem(url)
TC6= EditChart(url)
TC7= DeleteChartItem(url)
TC8= CheckPurchaseFlow(url)

#Print Results
print('Execution Result ')
print('TC1:',TC1)
print('TC2:',TC2)
print('TC3:',TC3)
print('TC4:',TC4)
print('TC5:',TC5)
print('TC6:',TC6)
print('TC7:',TC7)
print('TC8:',TC8)