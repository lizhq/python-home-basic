import logging

logging.basicConfig(level=logging.DEBUG,  
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',  
                    datefmt='%Y-%m-%d %H:%M:%S') 
                    #filename='/tmp/test.log',  
                    #filemode='w') 

def info(messge):
    logging.info(messge)