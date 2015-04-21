import socket             
import RPi.GPIO as GPIO     

GPIO.setmode(GPIO.BOARD)     
GPIO.cleanup()        

GPIO.setup(12,GPIO.OUT)        
HOST = ''                     
PORT = 6879                  
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))         

def cikis(pin,deger):   
    for pin in range(0,data[1])                             
                GPIO.output(pin,GPIO.HIGH) 
                time.sleep(1)             
        print pin,'.inci pini aktif ettim' 
                                        
GPIO.output(pin,GPIO.LOW)              
print ”Sualma bitti"
        
while 1:                    
    s.listen(1)                        
    conn, addr = s.accept()            
    print ‘Baglandi by', addr               
    while 1:                
        data = conn.recv(1024)                
        if not data: break            
        print 'Gelen veri:',data            
        if data[0]==‘F':            
            cikis(12,data[1])                
            cikis(12,data[2])                   

    #conn.close()
