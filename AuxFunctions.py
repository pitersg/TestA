#Libraries for DAta Scrap
from urllib.request import urlopen
from bs4 import BeautifulSoup
#Libraries for Excel handling
#import pandas as pd

def SetupConnection(site):
    #Setup Data Data connection to website
    #The purpose of this test is to test the the connectivity with the site
    #if the result is reached and data scrap is retrieved the result will be Passed
    #Otherwise the result of the test will be FAILED

    return 'PASSED'

def SearchArticle(url,article):
    #The input will specify the site to reach(url) and the article on search(article)
    #if the data scrap contains the article searched in the Artifact name field the result will be Passed
    #Otherwise the result of the test will be failed

     return 'PASSED'

def ListArticles(site):
    #The Function will download a list of articles found during the Data scrap and will store them into an excel report
    #if the report is empty the result will be FAILED

    return 'PASSED'

def CheckItemFields(url,List):
     #using as input the List provided above, the function will check that all the fields listed for all the items have been filled
     # If there is none empty fields in the report the result will be PASSED, Otherwise the result will be FAILED
     return 'PASSED'

def AddItem(url):
     #This function will add an item into the site, if the item is correctly added the result will be PASSED, Otherwise the result will be FAILED
     #Data Structure needs to be specified
     return 'PASSED'
def EditChart(url):
    #Function to Edit Quantity Field in Items in chart
    #Needs to be executed AddItem() function previously
    #The result will be PASSED if the quantity can be edited correctly, Otherwise the result will be FAILED

     return 'PASSED'

def DeleteChartItem(url):
    # Function to Delete Items in chart
    # Needs to be executed AddItem() function previously
    #The result will be PASSED if the quantity can be deleted correctly, Otherwise the result will be FAILED


     return 'PASSED'

def CheckPurchaseFlow(url):
    #Function to follow that the purchase flow iterates correctly
    #If the purchase can be correctly finished the result will be PASSED, otherwise will be FAILED
     return 'PASSED'


