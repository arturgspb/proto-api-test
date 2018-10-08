from concurrent import futures
import time

import grpc

from src.routes_v1 import reg_server_v1
from src.routes_v2 import reg_server_v2

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


def serve(port: int, grace_period: int):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    reg_server_v1(server)
    reg_server_v2(server)
    server.add_insecure_port('[::]:{}'.format(port))
    server.start()

    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(grace_period)


if __name__ == '__main__':
    serve(50051, 5)
