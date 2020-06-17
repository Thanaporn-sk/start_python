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

