from __future__ import print_function

import grpc

from src import hello_pb2_grpc
from src import hello_pb2

import json
import time

def get_token():
    return "eyJraWQiOiJhZWRiYmZlN2NjZjA3YzRiZWZkNDUwOTAxNTAxYjgzNzg3Njg1ZWNmIiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYifQ.eyJhdWQiOiJhcGlzLmRldmlzaW9uLmlvIiwic3ViIjoiMzQ4NyIsIml1aWQiOjEwMTkxLCJzY29wZSI6IiIsImlzcyI6InRva2VuLWlzc3Vlci5kZXZpc2lvbi5pbyIsImV4cCI6MTUzODYxMDM2NCwiaWF0IjoxNTM4NjEwMDY0fQ.UTTumJklOfYCJHruX3lxk-DXC7tvEsOPEKv3mIPfauDo_PBxwze8qH-4LqMDAnnzy-nAUuSwKBILUQggB059PaXkomIN5Av29jKcE8YUuc4fWaHliLzvXgZODisRhdgLNzU59V0y6wJ78OK8-H-dIfcuhZ4Zk309uAyLwg49i8ptgAWea-d3FjA-FMUOtdvwau-UzLlwmq4Ubw5EfkTTw2Iz64RhcRPLUBK19R0Ed8seuPanteaKAT_qWMo8KoTMFXu6UciYkITnRJaVjr7-FPgjgeTPJFBeBROr_r_8tDfNgvqs7zaLDxyIe_3xa80LByJILQUZEgXtZPMB4g9cyA"

def run():
    auth_token = get_token()
    print(auth_token)

    HEADER = "Bearer " + auth_token


    def do_rest():
        import requests
        resp = requests.post("http://hello.apis.kb.1ad.ru/v1/hello/ping", json={
            "ping": "Hi, PING!"
        }, headers={
            "Authorization": HEADER
        })
        print(u"resp.text = %s" % str(resp.text))
    # for t in range(2):

    # def do_grpc():
    #     # channel = grpc.insecure_channel('books-grpc.grpc.kb.1ad.ru')
    #     channel = grpc.insecure_channel('localhost:8083')
    #     stub = hello_pb2_grpc.HelloServiceStub(channel)
    #
    #     metadata = [("authorization", HEADER)]
    #
    #     hello_pb2.EchoRequest(name="asdasd")
    #
    #     resp = stub.Ping(
    #         hello_pb2.PingRequest(ping="lala")
    #         , metadata=metadata
    #     )
    #     print(u"resp = %s" % str(resp))

    do_rest()

    # do_grpc()
#

if __name__ == '__main__':
    run()
