import os

import grpc

import hello_pb2
import hello_pb2_grpc


def run():
    channel = grpc.insecure_channel(os.environ['SERVER_IP'] + ':' + os.environ['SERVER_PORT'])
    stub = hello_pb2_grpc.ProductServiceStub(channel)
    stub.AddProduct(hello_pb2.Product(name='happy product', price=1200))
    print('Added')


if __name__ == '__main__':
    run()
