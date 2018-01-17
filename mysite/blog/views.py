# Jan 17th, 2018 @ dormitory
# 写个首页看看

from django.http import HttpResponse
import datetime
def homepage(request):
    now = datetime.datetime.now()
    html = "<html><body>hello, this is homepage, it is {time}.</body></html>".format(time=now)

    return HttpResponse(html)
