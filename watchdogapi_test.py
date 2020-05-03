from __future__ import print_function
from watchdogapi import *     
                                  
                                 
def test():                      
                                  
    wd = watchdog('/dev/watchdog')    
                                 
    print('keep_alive:', end=' ')  
    try:                              
        print(wd.keep_alive())   
    except IOError as e:              
        print(e)                      
                                   
    print('get_status:', end=' ')     
    try:                          
        print(wd.get_status())        
    except IOError as e:
        print(e)                   
                                      
    print('get_boot_status:', end=' ')
    try:                           
        print(wd.get_boot_status())
    except IOError as e:          
        print(e)                  
                                         
    timeout = 60                  
    print('get_timeout:', end=' ')
    try:                                 
        timeout = wd.get_timeout()
        print(timeout)                   
    except IOError as e:                 
        print(e)                  
                                                                           
    print('set_timeout:', end=' ')       
    try:                         
        for i in range(1, 65536): 
            wd.set_timeout(i)            
            assert(wd.get_timeout() == i)
        wd.set_timeout(timeout)   
        print('OK')
    except IOError as e:                 
        print(e)                  
                                                                                  
    print('magic_close:', end=' ')
    try:                                 
        wd.magic_close()          
        print('OK')                      
    except IOError as e:                 
        print(e)                  
                                         
                                         
if __name__ == '__main__':        
    test()        
