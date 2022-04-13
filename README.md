# Setup
If DCS-gRPC updates, you may need to re-generate the proto files. Below are the steps to do so.
1. `pip install grpcio-tools`
2. Generate the route guides 
   1. Mission first - `python -m grpc_tools.protoc -I"C:\Users\Tim\Saved Games\DCS.openbeta\Docs\DCS-gRPC\Protos" --python_out=. --grpc_python_out=. "C:\Users\Tim\Saved Games\DCS.openbeta\Docs\DCS-gRPC\Protos\dcs\mission\v0\mission.proto"`
   2. Then common - `python -m grpc_tools.protoc -I"C:\Users\Tim\Saved Games\DCS.openbeta\Docs\DCS-gRPC\Protos" --python_out=. --grpc_python_out=. "C:\Users\Tim\Saved Games\DCS.openbeta\Docs\DCS-gRPC\Protos\dcs\common\v0\common.proto"`

# Running
1. Launch DCS, waiting for it to load
2. Run the script
3. Load a mission

