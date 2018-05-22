import urllib.request
import json
import ftplib
import os
url = "jsonUrl"



file_name = "filename.json"
remote_path = "ftpUploadPath"

#get Json Data
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
data = str(response.read().decode('utf-8'))
new_file = open(file_name,'w')
new_file.write(data)
new_file.close()


server = 'ftpServer'
username = 'ftpUser'
password = 'ftpPassword'

#Upload file to ftp server
ftp_connection = ftplib.FTP(server, username, password)
ftp_connection.cwd(remote_path)
fh = open(file_name, 'rb')
ftp_connection.storbinary('STOR ' + file_name, fh)
fh.close()


#delete file

os.remove(file_name)
