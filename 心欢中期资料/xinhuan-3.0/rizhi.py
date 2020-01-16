from datetime import *

def logging(massage):
    t2 = datetime.now().strftime("%Y-%m-%d")
    filename = "%s_logging.text" % t2
    fa = open("logs/" + filename, 'a+')
    fa.write(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+"  : "+massage+"\n")
    fa.close()



