from django.http import HttpResponse

def home(request):
    data="""
    <html>
        <head>
            <tittle> welcome to class </tittle>
        </head>
        <body>
            <h1> .....hello frends......</h1>
            <h2> ......how r u .....</h2>
        </body>
    </html>"""
    return HttpResponse(data)
