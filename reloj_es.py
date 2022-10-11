from datetime import datetime, timedelta
from text_to_speach import *

def reloj_español():
    time=datetime.now()
    user_time=datetime.strftime(time, '%H:%M')
    hora=datetime.strptime(user_time, '%H:%M')


    h=''
    m=''

    if hora.minute >=0 and hora.minute <=2 or hora.minute >=58:
        m='en punto'
    elif hora.minute >=3 and hora.minute <=7:
        m='y cinco'
    elif hora.minute >=8 and hora.minute <=12:
        m='y diez'
    elif hora.minute >=13 and hora.minute <=17:
        m='y cuarto'
    elif hora.minute >=18 and hora.minute <=22:
        m='y veinte'
    elif hora.minute >=23 and hora.minute <=27:
        m='y veinticinco'
    elif hora.minute >=28 and hora.minute <=32:
        m='y media'
    elif hora.minute >=33 and hora.minute <=37:
        hora+=timedelta(hours=1)
        m='menos veinticinco'
    elif hora.minute >=38 and hora.minute <=42:
        hora+=timedelta(hours=1)
        m='menos veinte'
    elif hora.minute >=43 and hora.minute <=47:
        hora+=timedelta(hours=1)
        m='menos cuarto'
    elif hora.minute >=48 and hora.minute <=52:
        hora+=timedelta(hours=1)
        m='menos diez'
    elif hora.minute >=53 and hora.minute <=57:
        hora+=timedelta(hours=1)
        m='menos cinco'


    if hora.hour==1 or hora.hour==13:
        h='la una'
    elif hora.hour==2 or hora.hour==14:
        h='las dos'
    elif hora.hour==3 or hora.hour==15:
        h='las tres'
    elif hora.hour==4 or hora.hour==16:
        h='las cuatro'
    elif hora.hour==5 or hora.hour==17:
        h='las cinco'
    elif hora.hour==6 or hora.hour==18:
        h='las seis'
    elif hora.hour==7 or hora.hour==19:
        h='las siete'
    elif hora.hour==8 or hora.hour==20:
        h='las ocho'
    elif hora.hour==9 or hora.hour==21:
        h='las nueve'
    elif hora.hour==10 or hora.hour==22:
        h='las diez'
    elif hora.hour==11 or hora.hour==23:
        h='las once'
    elif hora.hour==12 or hora.hour==0:
        h='las doce'
    
    return (f'Son {h} {m}')

decir_hora(reloj_español())   