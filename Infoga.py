
# 29 - FEBUARY - 2024
# Tool-Name: SIM_Infoga
# Versoin: 2.0.1
# Author: DHFH4CKER
# Website: www.dhfhacker.com.org
# Email: darkhackingforce@gmail.com

##### This is an Information Gathering tool based on SIM and it Country
##### SIM Infoga was build with the help of python programming language
##### The purpose of this script can be catagorized in-to three (3)
##### First step: Fetch information on a given phone number and it country
##### Second step: Track the location of the phone number
##### Third step: Generate a link that will directly track down the phone number on a map

import os,sys,time,argparse

stop="\033[0m"
red="\033[31;1m"
blue="\033[34;1m"
green="\033[32;1m"
yellow="\033[33;1m"
purple="\033[35;1m"
skyblue="\033[36;1m"

info2 = "%s[%s•%s]%s "%(green,stop,green,purple)
info = "%s[%s+%s]%s "%(red,stop,red,yellow)
error = "%s[%s!%s]%s "%(blue,stop,blue,red)
success = "%s[%s√%s]%s "%(purple,stop,purple,green)
version = "2.0.1.6"
lib = ["countryinfo","lolcat","pyfiglet","requests","phonenumbers","opencage"]

def slow(dhf):
    for a in dhf + '\n':
        sys.stdout.write(a)
        sys.stdout.flush()
        time.sleep(1 / 20)

def DHF():
    usage = """
 Useage: python3 Infoga.py [OPTION...]
------------
      | OPTIONS
      |----------
            | -u <Script Updating>       | Update Infoga Script for Better Security
            | -a <About Tool & Author>   | About our Tool and Contact us for more Question
            | -c <Victim's Country Code> | Specify Victim's Country Code WithOut "+" .eg 234
            | -p <Victim's Phone Number> | Specify Victim's Phone Number'
      | EXAMPLES
      |----------
            | python3 Infoga.py -u                   | Script Updating
            | python3 Infoga.py -a DHF               | About  Tool & Author
            | python3 Infoga.py -c 234 -p 7000000000 | Specify victim's Country Code & Phone Number         
    """
    return usage
    os.sys.exit()

try:import lolcat, pyfiglet, requests, opencage, countryinfo, phonenumbers
except ModuleNotFoundError:
    os.system("pyfiglet DHF Infoga | lolcat")
    slow("%sSetting up ur environment%s"%(info2,stop))
    for i in lib:os.system("pip install %s"%(i))
    os.system("pip install folium")
    os.system("clear || cls")
    print(DHF())
    os.sys.exit()
    
from countryinfo import CountryInfo
from opencage.geocoder import OpenCageGeocode
from phonenumbers import carrier, timezone, geocoder

def internet():
    try:
        s = socket(AF_NET, SOCK_STREAM)
        s.connect_ex(("www.google.com",80))
        return True
    except Exception:return False
    
def aboutme():
    os.system("clear || cls")
    os.system("pyfiglet DHF Infoga | lolcat")
    slow("%s"%(red))
    slow("-"*60)
    slow('\t%sTool Name     %s:>>%s Infoga'%(info,blue,yellow))
    slow("\t%sVersion       %s:>>%s v[%s]"%(info,blue,yellow,version[:-2]))
    slow("\t%sAuthor        %s:>>%s DHFH4CKER"%(info,blue,yellow))
    slow("\t%sGithub        %s:>>%s DHF Hacker"%(info,blue,yellow))
    slow("\t%sYoutube       %s:>>%s DHF Hacker"%(info,blue,yellow))
    slow("\t%sLatest Update %s:>>%s 25-02-2024"%(info,blue,yellow))
    slow("\t%sWebsite       %s:>>%s www.dhfhackers.org"%(info,blue,yellow))
    slow("\t%sEmail         %s:>>%s darkhackingforce@gmail.com%s"%(info,blue,yellow,red))
    slow("-"*60)
    slow("%s"%(stop))
    os.sys.exit()
    
def updateme():
    os.system("clear || cls")
    os.system("pyfiglet DHF Infoga | lolcat")
    slow("Checking For Update...")
    time.sleep(1)
    slow("Update Found!")
    os.system("clear || cls")
    os.system("cd")
    slow("Updating SIM_Infoga Script")
    os.system("git clone https://www.github.com/dhfhacker/SIM_Infoga.git")
    
def infoga(cncode,number):
    try:
        num = "+%s%s"%(cncode,number)
        phoneNumber = phonenumbers.parse(num)#+
        inter = phonenumbers.format_number(phoneNumber,phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        nation = phonenumbers.format_number(phoneNumber,phonenumbers.PhoneNumberFormat.NATIONAL)
        e164 = phonenumbers.format_number(phoneNumber,phonenumbers.PhoneNumberFormat.E164)
        gc = geocoder.description_for_number(phoneNumber,"en")
        tz = timezone.time_zones_for_number(phoneNumber)
        c = carrier.name_for_number(phoneNumber,"en")
        cncode = phoneNumber.country_code
        local = phoneNumber.national_number
        
        if (gc and c):   
            gcd = gc
            country = CountryInfo(gcd)
            iso = country.iso()["alpha2"]
            slow("\033[31;1m")
            slow("="*60)
            slow("[!] Attemting to track location of %s  [!]" % (inter.replace(" ","-")))
            slow("="*60)
            slow("%sRunning local scan..."%(purple))
            slow("%sInternational Format%s :>>  %s%s"%(skyblue,blue,green,inter))
            slow("%sNational Format%s :>>  %s%s"%(skyblue,blue,green,nation))
            slow("%sE164 Format%s :>>  %s%s"%(skyblue,blue,green,e164))
            slow("%sLocal Format%s :>>  %s%s"%(skyblue,blue,green,local))
            slow("%sCountry Found%s :>>  %s+%s (%s)"%(skyblue,blue,green,cncode,iso))
            time.sleep(1/3)
            
            Do = input("%sDo u want to get counrty infomation %s[%sYes%s/%snO%s]%s :>>  %s"%(info2,blue,stop,blue,stop,blue,red,green))
            
            if Do in ["yes","YES","Y","y","Yes"]:
                data = country.info()
                for i, j in data.items():
                    slow("%s%s %s :>> %s%s"%(skyblue,i,blue,green,j))
            elif Do in ["no","NO","N","n","No"]:slow("%sWe hope u know what u are doing!!!"%(info2))
            else:
                time.sleep(1)
                slow("%sInvalid Option%s"%(error,stop))
                os.sys.exit()
                
            slow("%sCity/Area%s :>>  %s%s (+%s)"%(skyblue,blue,green,gcd,cncode))
            slow("%sTime Zone ID%s :>>  %s%s"%(skyblue,blue,green,tz))
            slow("%sService Providers%s :>>  %s%s"%(skyblue,blue,green,c))
            if (phonenumbers.is_valid_number(phoneNumber)):slow("%sChacking Validation%s :>> %s Found"%(skyblue,blue,green))
            else:slow("%sChacking Validation%s :>> %s Not Found"%(skyblue,blue,red))
            
            slow("%sRunning Numverify.com scan..."%(purple))
            slow("%sNumber%s :>> %s (+%s) %s"%(skyblue,blue,green,cncode,local))
            slow("%sCountry%s :>> %s %s (%s)"%(skyblue,blue,green,gcd,iso))
            slow("%sLocation%s :>> %s Found"%(skyblue,blue,green))
            
            try:
                Key = "42c84373c47e490ba410d4132ae64fc4"
                code = OpenCageGeocode(Key)
                query = str(gcd)
                results = code.geocode(query)
                lat = results[0]['geometry']['lat']
                lng = results[0]['geometry']['lng']
                slow("%sLatitude%s :>>  %s%s%s, %sLongitude%s :>>  %s%s"%(skyblue,blue,green,lat,stop,skyblue,blue,green,lng))
                addr = coder.reverse_geocode(lat,lng)
                if addr:
                    address = addr[0] ['formatted']
                    slow("%sApproximate Location%s :>>  %s%s"%(purple,red,green,address))
                else:slow("%sNo address found for the given co-ordinates."%(info2))
            except Exception:
                time.sleep(1)
                slow("%sPlease check your internet connection.%s"%(error,stop))
                os.sys.exit()
                
            try:import folium
            except ModuleNotFoundError:
                time.sleep(1)
                slow('%sU will have to install "folium" else u can not view the location of this number in a map\n    type "pip install folium" to install folium after running this program.%s'%(error,stop))
                os.sys.exit()
                
            try:
                map = folium.Map(loction=[lat,lng],zoom_start=9)
                folium.Marker([lat,lng],popup=gcd).add_to(map)
                file = "%s/%s.html"%(gcd,local)
                map.save("%s"%(file))
                slow("%sPath to See Aerial Coverage%s :>>  %s%s"%(purple,red,green,os.path.abspath(file)))
            except NameError:
                time.sleep(1)
                slow("%sCould not get Aerial Coverage for this number.%s"%(error,stop))
                os.sys.exit()
            slow("%sRunning OVH scan..."%(purple))
            slow("%sRunning OSINT footprint reconnissance..."%(purple))
            slow("%sGeerating scan URL on 411.com!"%(green))
            slow("%sScan URL %s:>>%s https://www.411.com/phone/%s"%(skyblue,blue,green,inter.replace(" ","-")))
            time.sleep(2)
            slow("%s\nPrograms rans Successfully\nThanks for Using this Tool%s"%(green,stop))
            os.sys.exit()
            
        else:
            c = "Unkown"
            gc = "Unkown"
            gcd = gc
            slow("\033[31;1m")
            slow("="*60)
            slow("[!] Attemting to track location of %s [!]" % (inter.replace(" ","-")))
            slow("="*60)
            slow("%sRunning local scan..."%(purple))
            slow("%sInternational Format%s :>>  %s%s"%(skyblue,blue,red,number))
            slow("%sLocal Format%s :>> %s %s"%(skyblue,blue,red,number))
            slow("%sE164 Format%s :>>  %s%s%s"%(skyblue,blue,red,cncode,number))
            slow("%sCountry%s :>> %s Not Found"%(skyblue,blue,red))
            slow("%sCity/Area%s :>>  %s%s"%(skyblue,blue,red,gcd))
            slow("%sTime Zone ID%s :>>  %s%s"%(skyblue,blue,red,tz))
            slow("%sService Providers%s :>>  %s%s"%(skyblue,blue,red,c))
            if (phonenumbers.is_valid_number(phoneNumber)):slow("%sChacking Validation%s :>> %s Not Found"%(skyblue,blue,red))
            else:slow("%sChacking Validation%s :>> %s Not Found"%(skyblue,blue,red))
            time.sleep(1)
            slow("\n%sPlease specify a valid phone number and make sure that the country code you provided is for the phone number.%s\n"%(error,stop))
            os.sys.exit() 
    except Exception as err:
        time.sleep(1)
        slow ("\n%sCould not get the location of this number. Please specify a valid phone number %s\n"%(error,stop))
        os.sys.exit() 

def main():
    parser = argparse.ArgumentParser( description = "This is an imformation gathering tools that gathers imformation on a phone number and trys to locate the phone number on a map.")
    parser.add_argument ( "-c" , "--code" , dest= "coutry_code", type=str, help='Specified the country code without "+" eg.234')
    parser.add_argument ( "-p" , "--phone" , dest= "phone_number", type=str, help='Specified the victims phone number')
    parser.add_argument ( "-a" , "--about" , dest= "about_tool",  type=str, help='About the Author and the Tool')
    parser.add_argument ( "-u" , "--update" , dest= "update_script",  action ="store_true",help='About the Author and the Tool')
    argument = parser.parse_args()
    number = argument.phone_number
    cncode = argument.coutry_code
    update = argument.update_script
    about = argument.about_tool
    if not internet():
        slow("\n%sPlease check your internet connection%s"%(error,stop))
        os.sys.exit()
    if update:updateme()
    elif about in ["dhf","DHF"]:aboutme()
    elif number and cncode:infoga(cncode,number)
    else:print(DHF())
    #return argument
main()


