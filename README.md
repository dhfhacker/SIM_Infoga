<!DOCTYPE html>
<html>
  <head>
    <title>SIM Infoga</title>
  </head>
  <body>
    <h1 align="center">SIM INFOGA</h1>
    <p  align="center"><img alt="SIM Infoga" src="IMG_20240301_220917_191.jpg"></p>
    <hr>
    <h2>What infoga means?</h2>
    <p>Infoga is an abbreviation for Information Gathering and is a tool for gathering information on victim's.</p>
    <hr>
    <h2>What is SIM Infoga?</h2>
    <p>Sim Infoga is a tool that gathers information based on sim and it country,<br> which was build with the help of python programming language.</p>
    <hr>
    <h2>Purpose of SIM Infoga?</h2>
    <i>Actually...!, this can be catagorized in to three.</i>
    <ul>
      <li>It gathers information on phone number and it country.</li>
      <li>And locate the approximately location of the phone number.</li>
      <li>Then Generate a link that will track the phone number on a map.</li>
    </ul>
    <hr>
    <h2>SIM Infoga is Available on...</h2>
    <ul>
      <li>Termux</li>
      <li>Kali Linux</li>
    </ul>
    <hr>
    <h2>Installation in Termux and Usage</h2>
    <i>Download Termux app from google play store and type following commands</i>
    <pre>
      <code>
      apt update && apt upgrade
      </code>
      <code>
      apt install git
      </code>
      <code>
      git clone https://www.github.com/dhfhacker/SIM_Infoga.git
      </code>
      <code>
      cd SIM_Infoga
      </code>
      <code>
      python3 Infoga.py -c [Country_Code] -p [Phone_Number]
      </code>
    </pre>  
    <hr>
    <h2>SIM_Infoga Usage</h2>
    <pre>
      <code>
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
    
      </code>
    </pre>
    <hr>
    <p align="center"><img alt="python to track phone number on a map" src="Untitled.png"></p>
  </body>
</html>
