esp:
	# Cloud Endpoints
	python3 -m grpc.tools.protoc \
		--include_imports \
		--include_source_info \
		--proto_path=protos \
		--descriptor_set_out=api_descriptor.pb \
		hello.proto

	gcloud endpoints services deploy api_descriptor.pb api_config.yaml --project meta-test-164215

	rm api_descriptor.pb

dev:
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