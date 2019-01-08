import os
import time
from concurrent import futures

import grpc

import hello_pb2
import hello_pb2_grpc


class Servicer(hello_pb2_grpc.ProductServiceServicer):
    def AddProduct(self, request, context):
        print("AddProduct called")
        print(request.product)
        return hello_pb2.RequestType


    def ListProduct(self, request, context):
        pass


def serve():
    print("starting server...")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_ProductServiceServicer_to_server(Servicer(), server)
    server.add_insecure_port(os.environ['SERVER_IP'] + ':' + os.environ['SERVER_PORT'])
    server.start()

    print('Listen :' + os.environ['SERVER_PORT'])
    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        print('Stop server')
        server.stop(0)

if __name__ == '__main__':
    serve()
