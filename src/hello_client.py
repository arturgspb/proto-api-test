from __future__ import print_function


def get_token():
    return "eyJraWQiOiJhZWRiYmZlN2NjZjA3YzRiZWZkNDUwOTAxNTAxYjgzNzg3Njg1ZWNmIiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYifQ.eyJhdWQiOiJhcGlzLmRldmlzaW9uLmlvIiwic3ViIjoiMzQ4NyIsIml1aWQiOjEwMTkxLCJzY29wZSI6IiIsImlzcyI6InRva2VuLWlzc3Vlci5kZXZpc2lvbi5pbyIsImV4cCI6MTUzODc3NTAxNCwiaWF0IjoxNTM4Nzc0NzE0fQ.TGWcebaaLPrTz26Fuey4-GxknoK7iJBbUqcOr3D6gU0VDfPumqfnQW7kZxh4hdJ5eCvN0uvsYRkmHYdjhd6tT0UnYkJsSvHFDukz8J6q_aPciBkH0_C9-c-MAsPfHJTxO-gXJ8DeDUj5ymIMHAvlK85IK-6LjOfgZ40ld3ZFuKrztkR5oztbq9h2ZOUiWMZJMvtW0QJCXlv4aKhuhaBqrRcGDhA9T-Q1Tm_UGDOd54K-vnsh3eZy9RtbPayWDnEVYt9Vvnjks5V4V8H-ZhwDeUPEzqspxBfrJcEyOWmT8-5-DvzcANN1hjMde3iqI6X5Toaif38jU6wVIUa5uMkIAw"


auth_token = get_token()
print(auth_token)

HEADER = "Bearer " + auth_token


def do_rest():
    import requests
    host = "http://hello.apis.devision.io/v1/hello/ping"
    resp = requests.post(host, json={
        "ping": "Hi, PING!"
    }, headers={
        "Authorization": HEADER
    })
    print(u"resp.text = %s" % str(resp.text))

for idx in range(1000):
    do_rest()
