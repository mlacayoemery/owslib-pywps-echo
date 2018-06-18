import owslib.wps
import collections

url = "http://127.0.0.1:5000/wps"
wps = owslib.wps.WebProcessingService(url, verbose=False, skip_caps=True)
wps.getcapabilities()

process_name = "echo_vector"
inputs = [("message", owslib.wps.GMLMultiPolygonFeatureCollection([[(-102.8184, 39.5273),
                                                                    (-102.8184, 37.418),
                                                                    (-101.2363, 37.418),
                                                                    (-101.2363, 39.5273),
                                                                    (-102.8184, 39.5273)]]))]

execution = wps.execute(process_name, inputs)

for output in execution.processOutputs:
    owslib.wps.printInputOutput(output)
