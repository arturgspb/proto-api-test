from __future__ import print_function


def get_token():
    return "eyJraWQiOiJhZWRiYmZlN2NjZjA3YzRiZWZkNDUwOTAxNTAxYjgzNzg3Njg1ZWNmIiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYifQ.eyJhdWQiOiJhcGlzLmRldmlzaW9uLmlvIiwic3ViIjoiMzQ4NyIsIml1aWQiOjEwMTkxLCJzY29wZSI6IiIsImlzcyI6InRva2VuLWlzc3Vlci5kZXZpc2lvbi5pbyIsImV4cCI6MTUzODc1MjMzNSwiaWF0IjoxNTM4NzUyMDM1fQ.JSaopRvJXTaRxaOnUJJss6_EIrvAKQ6Hy_Js3tB2QRBciHiC8MjZA4QkqBwx5TRFmaoTVBPAiMIVP0YyU-OoZq-Iii6xE5_DJMB4Iv0eJpOYoXD0b-0hkNDxYBxlLBl10ErcolSYkQ4GuiAqbBdBIQT4H8UlPtZ9KdCZWqtsxRZT1IpGUkW-G-NdVzdfIycT82MLRSlOGod__O7wxZWwzx-ZWU-kUIm1GDwUZAYF-c2yqlK2XoD7uFEigB_L_bmkZiZpaTGwdnHiaLhloQMqtiijPB5S7KqsPgnPOTeBZ9ArVVUGkyS4TleMBCNJarDgiujUYt1841zmkGf_KSF9dQ"

auth_token = get_token()
print(auth_token)

HEADER = "Bearer " + auth_token

def do_rest():
    import requests
    # host = "http://hello.apis.kb.1ad.ru/v1/hello/ping"
    host = "http://localhost:8084/v2/hello/ping"
    resp = requests.post(host, json={
        "ping": "Hi, PING!"
    }, headers={
        "Authorization": HEADER
    })
    print(u"resp.text = %s" % str(resp.text))

do_rest()
