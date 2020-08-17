import datetime 
def common(request):
    context = {}
    now = datetime.datetime.now()
    yearmonth = now.strftime('%Y%m')
    #yearmonth = '202006'
    context['yearmonth'] = yearmonth
    return context