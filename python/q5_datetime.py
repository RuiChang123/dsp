# Hint:  use Google to find python function
from datetime import datetime, date, time
####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   
d1=datetime.strptime(date_start, "%m-%d-%Y")
d2=datetime.strptime(date_stop, "%m-%d-%Y")
(d2-d2).days
####b)  
date_start = '12312013'  
date_stop = '05282015'  
d1=datetime.strptime(date_start, "%m%d%Y")
d2=datetime.strptime(date_stop, "%m%d%Y")
(d2-d2).days
####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015' 
d1=datetime.strptime(date_start, "%m-%b-%Y")
d1=datetime.strptime(date_stop, "%m-%b-%Y")
(d2-d1).days
