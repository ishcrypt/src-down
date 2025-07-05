#!/usr/bin/python3

import urllib.request as src
import pyfiglet
from termcolor import colored 

banner=colored(pyfiglet.figlet_format("Source code Read" ), 'cyan' )
print(banner)

print(colored("********************     Source code read from WebSite       ********************" , 'light_yellow'))
print(colored("******************** Make by ArenaWebSecurityStudent(ishmam) ********************" , 'light_red'))

site_name = input("Enter website name : ")
openn = src.urlopen(site_name)
reading = openn.read()

print(reading)
