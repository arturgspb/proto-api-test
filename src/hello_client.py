from __future__ import print_function


def get_token():
    return "eyJraWQiOiJhZWRiYmZlN2NjZjA3YzRiZWZkNDUwOTAxNTAxYjgzNzg3Njg1ZWNmIiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYifQ.eyJhdWQiOiJhcGlzLmRldmlzaW9uLmlvIiwic3ViIjoiMzQ4NyIsIml1aWQiOjEwMTkxLCJzY29wZSI6IiIsImlzcyI6InRva2VuLWlzc3Vlci5kZXZpc2lvbi5pbyIsImV4cCI6MTUzODgyMDk3MywiaWF0IjoxNTM4ODIwNjczfQ.absu3u2puXMXu8HBy3fRWAJtfc2CA4P7-OyShRAKpBF_kYXBCoe7c-Ml3Oh0nybeP8vnBW6EFS9pcvZw_VIAABBt9bF79_Prj2S0h4vEaCaWjRM47h24iozaQ9vDAjn_xUMZyOhhrKkUA89Au-ANv_WULw-KCR_AqNnYYLd6-TloolAZ_AkioKgn2fS_iPKZY3dEHo0ZZmGqqlfTtUe0zsUiEUaPvgLeKXsdKcWUowCj4lr89KBuKSO9dka3v9YwzJPCXDyLeT-oFAJF4lhGSigYRYtsa3VR278ID0uHciMSpr5F4qDJEgctpalmoN1g8oGpjXFfthg4KebcQaOZ6A"


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
