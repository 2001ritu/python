from coapthon.client.helperclient import HelperClient
from coapthon import defines
from coapthon.messages.request import Request


host = "127.0.0.1"
port = 5683
path ="basic"
payload = 'text/plain'

client = HelperClient(server=(host, port))
response = client.get(path)
print(response.pretty_print())

# Create a registration resource
ct = {'content_type': defines.Content_types["application/link-format"]}
payload = 'Random text1234'
response = client.post(path, payload, None, None, **ct)
location_path = response.location_path
print(response.pretty_print())
 
client.stop()
