# https://cloud.google.com/endpoints/docs/grpc/configure-endpoints

# https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/endpoints/getting-started-grpc/
# https://cloud.google.com/endpoints/docs/grpc/running-esp-localdev
# https://github.com/cloudendpoints

# https://cloud.google.com/endpoints/docs/openapi/authenticating-users#configuring_extensible_service_proxy_to_support_client_authentication
# https://github.com/googleapis/googleapis/blob/master/google/api/service.proto
# https://cloud.google.com/endpoints/docs/grpc/authentication-method

docker run \
    --name="esp" \
    --publish=8083:8083 \
    --volume=$HOME/esp:/esp \
    gcr.io/endpoints-release/endpoints-runtime:1 \
    --service=bookstore.endpoints.meta-test-164215.cloud.goog \
    --rollout_strategy=managed \
    --http2_port=8083 \
    --backend=grpc://docker.for.mac.localhost:50051 \
    --service_account_key=/esp/test-esp-service-account-creds.json

docker rm esp