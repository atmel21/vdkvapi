from django.shortcuts import render,render_to_response,RequestContext
from django.db import connection
#from forms import form_kv
import time
from httphandler import models
# Create your views here.

# Method for handling insert request
def insertkv(request):
    message=''
    if request.method == 'POST':
        entry = models.KeyValueStore(keyid = request.POST['key'],val = request.POST['value'],modified = int(time.time()))
        entry.save()
        message = "Stored successfully"

    context={'message': message}
    return render_to_response('form.html',context=context,context_instance=RequestContext(request))

#Method for handlilng fetch request

def fetchkv(request,keyid='',ts=''):
    message=''
    if request.method == 'GET':
        ts = request.GET.get('timestamp','')
        if keyid != '' and ts != '':

            #create sql connection
            sql_cursor=connection.cursor()
            #query to fetch value for the corresponding key & Time stamp
            query='select val from key_value_store where keyid ='+keyid+' and modified ='+ts

            try : 
                sql_cursor.execute(query)
                outputval = sql_cursor.fetchone()[0]
                message = 'The value for the keyid '+keyid+' at timestamp '+ts+' is '+outputval
            except Exception:
                message = 'Record may not exist'
            finally:
                sql_cursor.close()
        elif keyid != '' and ts == '':
            #create sql connection
            sql_cursor=connection.cursor()
            # query to fetch latest modied value for the corresponding key
            query='select val from key_value_store where keyid ='+keyid+' order by modified desc limit 1'
            try : 
                sql_cursor.execute(query)
                outputval = sql_cursor.fetchone()[0]
                message = 'The latest value for the key '+keyid+' is '+str(outputval)
            except Exception:
                message = 'Record may not exist'
            finally:
                sql_cursor.close()
    elif request.method=='POST':
        key = request.POST['key']
        if key == '': message = "Please mention a key"
        elif request.POST['timestamp'] == '':
            sql_cursor=connection.cursor()
            # query to fetch value for the corresponding key
            query='select val from key_value_store where keyid ='+key+' order by modified desc limit 1'
            try :
                sql_cursor.execute(query)
                outputval = sql_cursor.fetchone()[0]
                message = 'The latest value for the key '+key+' is '+str(outputval)
            except Exception:
                message = 'Record may not exist'
            finally:
                sql_cursor.close()
        else:
            timestamp = request.POST['timestamp']
            sql_cursor=connection.cursor()

            query='select val from key_value_store where keyid ='+key+' and modified ='+timestamp
            try:
                sql_cursor.execute(query)
                outputval = sql_cursor.fetchone()[0]
                message = 'The value for the key '+key+'at timestamp '+timestamp+' is '+outputval
            except Exception:
                message = 'Record may not exist'
            finally:
                sql_cursor.close()

    context={'message': message}
    return render_to_response('fetch.html',context=context,context_instance=RequestContext(request))


