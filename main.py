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

#Call the download function
print("Executing download test...")
download_outcome = test.download()

#Call the upload function
print("Executing upload test...")
upload_outcome = test.upload()

ping_outcome = test.results.ping

print(download_outcome)
print(upload_outcome)
print(ping_outcome)

#Convert to Mbps
print(f"Download speed: {download_outcome / 1024 /1024: .3f} Mbps")
print(f"Upload speed: {upload_outcome / 1024 /1024: .3f} Mbps")
print(f"Ping: {ping_outcome: .3f} ms")