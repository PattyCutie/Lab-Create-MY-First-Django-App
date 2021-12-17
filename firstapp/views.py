from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from datetime import date

def index(request):
    #Creat a simple html page as a string
    template = "<html>" \
                "This is Patpicha's first view" \
                "</html>"
    # Returm the template as content argument in HTTP respone
    return HttpResponse(content=template)

def get_date(request):
    today = date.today()
    template = "<html>" \
                "Today's date is {}" \
                "</html>".format(today)
                #<HINT>Add .format(today)
    return HttpResponse(content=template)
    #<HINT> use the template object as argument value 
    # such as <content=template>