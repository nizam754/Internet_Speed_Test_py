#Import module
#Install from https://pypi.org/project/speedtest-cli/

import speedtest

#Create speedtest object
test = speedtest.Speedtest()

print("Server loading.....")


#Get a list of servers
test.get_servers()

print ("Choosing ideal server...")

ideal = test.get_best_server()

print(ideal)