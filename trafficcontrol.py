import pyfirmata

comport='COM10'

board=pyfirmata.Arduino(comport)

Led_1=board.get_pin('d:13:o')
Led_2=board.get_pin('d:12:o')
Led_3=board.get_pin('d:11:o')
Led_4=board.get_pin('d:10:o')
Led_5=board.get_pin('d:9:o')

def led(total):
    if total==0:# Slow yellow #pin 11
        Led_1.write(0)
        Led_2.write(0)
        Led_3.write(1)
        Led_4.write(0)
        Led_5.write(0)
    elif total==1: # Go!! green #pin 13
        Led_1.write(1)
        Led_2.write(0)
        Led_3.write(0)
        Led_4.write(0)
        Led_5.write(0) 
    elif total==5:#stop red #pin 9
        Led_1.write(0)
        Led_2.write(0)
        Led_3.write(0)
        Led_4.write(0)
        Led_5.write(1)