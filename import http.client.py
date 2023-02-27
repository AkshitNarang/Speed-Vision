# import http.client

# conn = http.client.HTTPSConnection("aerodatabox.p.rapidapi.com")

# headers = {
#     'X-RapidAPI-Key': "f876d351c7mshba1239e0d729ab2p12fbbajsn2928a15fda0d",
#     'X-RapidAPI-Host': "aerodatabox.p.rapidapi.com"
#     }

# conn.request("GET", "/flights/%7BsearchBy%7D/KL1395/2020-06-10", headers=headers)

# res = conn.getresponse()
# data = res.read()

# print(data.decode("utf-8"))