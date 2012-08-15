from caa.schedules.models import Showing
import datetime

def next_showing(request):
    now = datetime.datetime.today()
    #now_date = now.strftime('%Y-%m-%d')
    #now_time = now.strftime('%H:%M:00')

    query = Showing.objects.filter(date__gte=now.date())
    
    if query.count() == 0:
        next_showing = None
    else:
        if query[0].date == now.date():
            if query[0].end_time < now.time():
                if query.count() > 1:
                    next_showing = query[1]
                else:
                    next_showing = None
            else:
                next_showing = query[0]
        else:
            next_showing = query[0]
        
    return {'next_showing': next_showing}
