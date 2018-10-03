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
        # 'email': 'user@example.com',
        'scope': "meta.metaql userinfo.profile"
    }

    signed_jwt = google.auth.jwt.encode(signer, payload)
    return signed_jwt


def get_token():
    sec_file = '/Users/arturgspb/Documents/devision-token-issuer.json'
    jwt_key = generate_jwt(sec_file, issuer="token-issuer.devision.io", audiences="apis.devision.io")
    # jwt_key = generate_jwt(sec_file, issuer="token-issuer@devision-io.iam.gserviceaccount.com", audiences="https://oauth2.googleapis.com/token")
    access_token = jwt_key.decode("utf-8")
    return access_token


def run():
    auth_token = get_token()
    auth_token="eyJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJhcGlzLmRldmlzaW9uLmlvIiwic3ViIjoiMzQ4NyIsInNjb3BlIjoiYXNkYXNkIGFzZGFzZCIsImlzcyI6InRva2VuLWlzc3Vlci5kZXZpc2lvbi5pbyIsImV4cCI6MTUzODU5MjQ5OSwiaWF0IjoxNTM4NTkyMTk5fQ.Hv6C1JmNH4xo9Uyb4r-FimpbvdAtEPh9HB3uccXXSh6FoRiCpWN-ul8wh0zgpzXNLCanAWjCcQvzeWIQTUXv_EZfzXS15cYThwffBsUWT5Xhbs7pcs9rggfYy1PurXYCTjgQf-BrvdLRE_2A-MpP3vAz-6srXdufv_5HnWHTxbb4J-02cvzdtNwXYgRE3tbDfz-OH-DZfMpVm18cEHVocWu0H1k-Y14EeqSHDz1qmjor9M3-BJLQIHtLYS5RasMr8muS-qRU-X_D4O09gLAVU4u0aQqqvwBMJMBtSbmsb1UtKfNrmoXcdRZltqWHAzjrf3bKrntl16YIIkH09m5BAg"
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
