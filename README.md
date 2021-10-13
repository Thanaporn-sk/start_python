# start_python

---------------------------------
How to create .exe from .py
---------------------------------
install pyinstaller
>pip install pyinstaller

create .exe file
>pyinstaller --onefile myScript.py


----------------------------------
PyODBC for msaccess
----------------------------------
1. document on : https://docs.microsoft.com/en-us/sql/connect/python/pyodbc/step-1-configure-development-environment-for-pyodbc-python-development?view=sql-server-2017


----------------------------------
Oracle
----------------------------------
1. instant client 11.2 (for oracle9i) http://www.oracle.com/technetwork/topics/winx64soft-089540.html
    download ,extract, add PATH in env variable.

2.cx_oracle     
    pip install cx_oracle
    
    
    



------------------------------------
 Change home directory jupyter in Anaconda 
------------------------------------
1. Open "Anaconda Prompt" and type jupyter notebook --generate-config

2. Open file in C:\Users\username\.jupyter\jupyter_notebook_config.py

3. Find and Change the line of #c.NotebookApp.notebook_dir = '' to c.NotebookApp.notebook_dir = 'c:\\your path\\'

4. Then, go to the shortcut of Jupyter Notebook located in C:\Users\User_name\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Anaconda3 (64-bit)

5. Do the right click and go to the Properties

6. In the Target  remove %USERPROFILE% , then in Start in, type the same directory of 'c:\\your path\\' in jupyter_notebook_config.py

 Try!





---------------------------------
Python virtual env  (windows)
--------------------------------
create:  python -m venv c:\path\to\myenv

activate: C:\> <venv>\Scripts\activate.bat
    
 
 ---------------------------------------
 PIP  (install)
 ---------------------------------------
 python get-pip.py
 
 pip --version
 
 python -m pip install --upgrade pip
 
 python -m pip install pip==18.1
 
 

--------------------------------------
PIP (install  && uninstall package)
--------------------------------------
pip install pandas      #install pandas

pip uninstall pandas    #uninstall pandas

pip install pandas==0.25.3 # install pandas version specific


pip freeze #check package installed in venv

$ pip freeze > requirements.txt
$ pip install -r requirements.txt
$ rmvirtualenv venv

------------------------------------------
link python command in linux
------------------------------------------
sudo unlink /usr/bin/python
sudo ln -s /usr/bin/python3.5 /usr/bin/python

ls -la /usr/bin/python



----------------------------------------------
#convert .ipynb to .py
---------------------------------------------

pip install ipython
pip install nbconvert

$ ipython nbconvert --to script File.ipynb
>> output File.py


-------------------------------------------------------
LookupError: unknown encoding: 874
-------------------------------------------------------
ref : https://medium.com/@winvinc/unknown-encoding-874-ec22cabb69b8


add following to that file (Location “<Install path>\anaconda3\Lib\encodings\aliases.py”)
--------------------------
    #cp 874
    '874' : 'cp874',
    'ibm874' : 'cp874',
    'iso_8859_11': 'cp874',
    'iso8859_11' : 'cp874',
    'windows_874': 'cp874',
    
    
    book lists
    
    
    https://www.pythonkitchen.com/legally-free-python-books-list/?fbclid=IwAR3YF5v6J0eG9OtZA4DnnjExMOF6enGAvkqzNPJx2KbTKf1dXmM7lrIcBqk

    ------------------------------------------------------------------------
    windows power shell
https://www.howtogeek.com/117192/how-to-run-powershell-commands-on-remote-computers/



host computer
	enable-PSRemoting -Force
	 Enable-PSRemoting -SkipNetworkProfileCheck -Force


worker

	test-WSman host-ip-address
	Enter-pssession -computerName sss -Credential user@domain
	hostname.exe
	get-netIPconfiguration
	netstat -n

Set-Item WSMan:\localhost\Client\TrustedHosts -Value "192.168.1.69"

winrm quickconfig -transport:https
netsh firewall add portopening TCP 5986 "WinRM over HTTPS"
winrm set winrm/config/client @{TrustedHosts="10.0.5.35"}
Set-Item wsman:\localhost\client\trustedhosts *

---------------------------
netsh advfirewall firewall set rule group="Windows Management Instrumentation (WMI)" new enable=yes

--------------------------------
pfsense expanding hdd	(vmware)
init 1
gpart show
gpart resize -i 1 ad0

bsdlabel -e /dev/ad0s1

-grow root system file
**gpart delete -i 2 ad0s1
swapoff /dev/label/swap0
gpart resize -i 1 -s 88G ad0s1
****growfs /dev/ad0s1a
service growfs onestart

gpart add -t freebsd-swap ad0s1	
    
    
