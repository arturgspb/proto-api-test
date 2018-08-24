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
