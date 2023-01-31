days=int(input('enter the days'))
if (days>84):
    print('plan xpired')
else:
    remainingdays=84-days
    calls=int(input('enter the calls'))
    data=float(input('enter the data'))
    msgs=int(input('enter msgs'))

    print('remainingdays',remainingdays)
    
    
    if(calls>3000):
        print('your limit is exceeded')
    else:
        remainingcalls=3000-calls
        print('remainingcalls',remainingcalls)
        
        
        if(data>2):
                print('data exceeded')
        else:
                remainingdata=2-data
                print('remainingdata',remainingdata)

               
                if(msgs>100):
                    print('msgs xceeded')
                else:
                    remainingmsgs=100-msgs
                    print('remainingmsgs',remainingmsgs)
        
