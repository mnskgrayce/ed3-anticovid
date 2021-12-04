import multiprocessing as mp

from multiprocessing import Process

import time
from grove.gpio import GPIO
from grove.button import Button
from grove.grove_ryb_led_button import GroveLedButton

start = time.perf_counter()
# Grove - LED Button connected to port D16
button = GroveLedButton(16)

def ledbutton():
    button.led.light(True)
    time.sleep(2)
    button.led.light(False)

# funtion for buzzer
class GroveRelay(GPIO):
    def __init__(self, pin):
        super(GroveRelay, self).__init__(pin, GPIO.OUT)
 
    def on(self):
        self.write(1)
 
    def off(self):
        self.write(0)

# Grove - Buzzeer connect to PWM port 12
relay = GroveRelay(12)

def buzzer():
    relay.on()
    time.sleep(1)
    relay.off()
    time.sleep(0.5)
    relay.on()
    time.sleep(1)
    relay.off()


def main():

    proc1 = Process(target=buzzer)
    proc2 = Process(target=ledbutton)
    proc1.start()
    proc1.join()
    proc2.start()
    proc2.join()
    print('cimplted...')
    # while True:
    #     t1 = threading.Thread(target=buzzer)
    #     t2 = threading.Thread(target=ledbutton)
    #     t1.start()
    #     t2.start()
    #     t1.join()
    #     t2.join()
    #     finish = time.perf_counter()
    #     print(f'Finished in {round(finish-start, 2)} second(s)')
    #     time.sleep(1)
 
if __name__ == '__main__':
    main()
