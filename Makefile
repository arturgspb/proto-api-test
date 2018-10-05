init:
	git clone https://github.com/googleapis/googleapis ~/googleapis

esp:
	# Cloud Endpoints
	python3 -m grpc.tools.protoc \
		--include_imports \
		--include_source_info \
		-I/Users/arturgspb/go/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis \
		--proto_path=protos \
		--python_out=./src \
		--mypy_out=./src \
		--grpc_python_out=./src \
		--descriptor_set_out=api_descriptor.pb \
		hello.proto

	#gcloud endpoints services deploy api_descriptor.pb api_config.yaml --project devision-io
	#rm api_descriptor.pb

dev:
	docker run \
		--name="esp" \
		--publish=8083:8083 \
		--publish=8084:8084 \
		--volume=/Users/arturgspb/esp:/esp \
		gcr.io/endpoints-release/endpoints-runtime:1 \
		--service=bookstore.endpoints.meta-test-164215.cloud.goog \
		--rollout_strategy=managed \
		--http_port=8084 \
		--http2_port=8083 \
		--backend=grpc://docker.for.mac.localhost:50051 \
		--service_account_key=/esp/test-esp-service-account-creds.json

	docker rm esp

kube:
	kubectl delete deployment grpc-hello
	kubectl apply -f deployment.yaml
