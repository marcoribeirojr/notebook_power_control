import psutil
import requests
import time
from decouple import config
import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify

def notify(header='', msg=''):
    '''
        Emite notificação de sistema
        Arguments:
            <str> header - Cabeçalho da notificação
            <str> msg - Mensagem a ser emitida na notificação  
    '''
    
    notification = Notify.Notification.new(header, msg)
    notification.show()
    return

def main():
    
    Notify.init('power_battery')
    min = config('min')
    max = config('max')

    while True:
    
        info = psutil.sensors_battery()
        power_level = round(info.percent)
        power_plugged = info.power_plugged

        power_on_url = config('url_power_on')
        power_off_url = config('url_power_off')
    
        error_header = 'Nível de bateria baixo'
        error_msg = 'Nível de bateria baixo e carregador desconectado.'
    
        if power_level < min and not power_plugged:
            notify(error_header, error_msg)
            time.sleep(240)
        
        if power_level < (min + 1)  and not power_plugged:
            data_returned = requests.get(power_on_url)
    
        if power_level > max and power_plugged : 
            data_returned = requests.get(power_off_url)
        
        time.sleep(60)
    
if __name__ == '__main__':
    main()     
