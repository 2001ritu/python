from coapthon.server.coap import CoAP
from pms_basicresourse import BasicResource

class CoAPServer(CoAP):
    def __init__(self, host, port):
        CoAP.__init__(self, (host, port))
        print(port)
        self.add_resource('basic/', BasicResource())

def main():
    server = CoAPServer("127.0.0.1", 5683)
    try:
        print("abc :")
        server.listen(10)
    except KeyboardInterrupt:
        print ("Server Shutdown")
        server.close()
        print ("Exiting...")

if __name__ == '__main__':
    main()
