from __future__ import print_function

import grpc

from src import hello_pb2_grpc
from src import hello_pb2

import json
import time

import google.auth.crypt
import google.auth.jwt

"""Max lifetime of the token (one hour, in seconds)."""
MAX_TOKEN_LIFETIME_SECS = 60 * 10


def generate_jwt(service_account_file, issuer, audiences):
    """Generates a signed JSON Web Token using a Google API Service Account."""
    with open(service_account_file, 'r') as fh:
        service_account_info = json.load(fh)

    signer = google.auth.crypt.RSASigner.from_string(
        service_account_info['private_key'],
        service_account_info['private_key_id'])

    now = int(time.time())

    payload = {
        'iat': now,
        'exp': now + MAX_TOKEN_LIFETIME_SECS,

        'iss': issuer,
        'aud': audiences,

        # sub and email are mapped to the user id and email respectively.
        'sub': '12345678',
        'email': 'user@example.com',
        'scp': "meta.metaql,userinfo.profile"
    }

    signed_jwt = google.auth.jwt.encode(signer, payload)
    return signed_jwt


def get_token():
    sec_file = '/Users/arturgspb/esp/test-esp-service-account-creds.json'
    # issuer = "test-esp@meta-test-164215.iam.gserviceaccount.com"
    issuer = "jwt-client.endpoints.sample.google.com"
    jwt_key = generate_jwt(sec_file, issuer, audiences="bookstore.endpoints.meta-test-164215.cloud.goog")
    access_token = jwt_key.decode("utf-8")
    return access_token


def run():
    # channel = grpc.insecure_channel('localhost:12345')
    # channel = grpc.insecure_channel('localhost:50051')
    # channel = grpc.insecure_channel('apiproxyt.apis.kb2.1ad.ru:50051')
    channel = grpc.insecure_channel('localhost:8083')
    # channel = grpc.insecure_channel('grpc-test.kb2.1ad.ru:50051')
    # channel = grpc.insecure_channel('n2.adp.vmc.loc:31846')
    stub = hello_pb2_grpc.HelloServiceStub(channel)

    # metadata = [("x-api-key", "AIzaSyBOvwjnUe4CDrmm7RftN4QhRg_J2a-TpL4")]
    auth_token = get_token()

    metadata = [("authorization", "Bearer " + auth_token)]

    def do_req():
        resp = stub.Echo(
            hello_pb2.EchoRequest(name="Artur!")
            , metadata=metadata
        )
        print(resp)

    # do_req()
    do_req()


if __name__ == '__main__':
    run()
