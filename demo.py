import os
import platform
from urllib2 import urlopen
my_ip = urlopen('http://ip.42.pl/raw').read()
print("Your public IP address is " + my_ip + ".")
print("Your OS is " + os.name + ".")
print("Your system is " + platform.system() + " version " + platform.release() + ".")