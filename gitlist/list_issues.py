import datetime
import dateutil.parser
import pytz
import requests
import json

l='https://api.github.com/repos/django/django/issues?state=open'

def print_(obj,s):
    '''
    print the list of Issues 
    '''
    if not len(obj):
        return
    if s=='Day':
        print('Issues within 24 hours '+str(len(obj)))
    else:
        print('Issues within a '+ s+' '+str(len(obj)))
    for i in obj:
        print(s+': '+i['title'])
    print('\n')

import requests.packages.urllib3

def get_issues(*args):
    '''
    Get the list of issues(<24 hrs, <1week)
    '''
    requests.packages.urllib3.disable_warnings()#resolve

    if str(args).strip() != '':
        link='https://api.github.com/repos/'+args[0]+'/issues?state=open'
    else:
        link=l
    try:
        resp=requests.get(link)
    except Exception as ex:
       print(str(ex)) 
       return([{"type":"error","message":"Oops! contact owner"}])

    j=json.loads(resp.text)
    print(resp.status_code)

    if resp.status_code == 404:
        return ([{"type":"error","message":"Could not find the github link.    tl;dr 404"}])
    elif resp.status_code != 200:
        return ([{"type":"Url is throwing"+str(resp.status_code)}])

    day=[]
    week=[]
    for i in j:
        if dateutil.parser.parse(i['created_at']) > datetime.datetime.now(tz=pytz.utc)-datetime.timedelta(days=1):
            day.append({'title':i['title'],'issue_url':i['html_url'],'user':i['user']['login']})
        elif dateutil.parser.parse(i['created_at']) > datetime.datetime.now(tz=pytz.utc)-datetime.timedelta(days=7):
            week.append({'title':i['title'],'issue_url':i['html_url'],'user':i['user']['login']})

    #print_(day,'Day')

    sd=[]
    sd.append({"type":"day","length":len(day),"data":day})
    sd.append({"type":"week","length":len(week),"data":week})
    #print_(week,'Week')
    return sd
        
if __name__ == "__main__":
    pass
    #sd=list_issues()
    #print(json.dumps(sd))
