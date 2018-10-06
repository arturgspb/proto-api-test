from __future__ import print_function


def get_token():
    return "eyJraWQiOiJhZWRiYmZlN2NjZjA3YzRiZWZkNDUwOTAxNTAxYjgzNzg3Njg1ZWNmIiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYifQ.eyJhdWQiOiJhcGlzLmRldmlzaW9uLmlvIiwic3ViIjoiMzQ4NyIsIml1aWQiOjEwMTkxLCJzY29wZSI6IiIsImlzcyI6InRva2VuLWlzc3Vlci5kZXZpc2lvbi5pbyIsImV4cCI6MTUzODg0NjkwMiwiaWF0IjoxNTM4ODQ2NjAyfQ.t1bwTl4WRXd9osI7hXfaVBtCBay8xRERtTCfkvdqI2hwS5_CQ21ZAiwFvEQml6BacP6AqFEheleV3GHB6Jk5tS2HbpmiJ-gFtagGhK9CtkUz1fNE3h8rzF4g57NtRC_6aqOVbDOTm6bAiiQwekYJrcDy8U_s5lUO4vupesPf4O-wWdjG3j_3iOGK-B0sE9HV1Kec96FtxaABJ2SDSvM82WjKT6gy6Tv08T7lyylQD7BX2T3mK-PkFzskFu6cRuIzaDQxcWwTxED3TEZpRZO3BW70fl7x2vZqK8OxABxF_JRR-I7qZGrfVLQhG7nh5qX-0bDgJy9nw767yqEVhLxCgg"


auth_token = get_token()
print(auth_token)

HEADER = "Bearer " + auth_token


def do_rest():
    import requests
    # host = "http://hello.apis.devision.io/v1/hello/ping"
    host = "http://localhost:8084/v1/hello/ping"
    resp = requests.post(host, json={
        "ping": "Hi, PING!"
    }, headers={
        "Authorization": HEADER
    })
    print(u"resp.text = %s" % str(resp.text))

do_rest()
