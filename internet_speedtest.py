# Internet SpeedTest

import speedtest as st

# Need to get best server for testing
server = st.Speedtest()
server.get_best_server()

# Check download speeds and convert it to Mb/s
down = server.download()
down = round(down / 1000000, 2)
print(f"Download Speed: {down} Mb/s")

# Check upload speeds and convert it to Mb/s
up = server.upload()
up = round(up / 1000000, 2)
print(f"Upload Speed: {up} Mb/s")

# Check ping
ping = round(server.results.ping, 2)
print(f"Ping Speed: {ping}")
