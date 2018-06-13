import owslib.wps
import collections

url = "http://127.0.0.1:5000/wps"
wps = owslib.wps.WebProcessingService(url, verbose=False, skip_caps=True)
wps.getcapabilities()
print("Process list is %i long." % len(wps.processes))

tests = collections.OrderedDict()

process_name = "echo_string"
inputs = [("message", "Hello World!")]

tests[process_name] = inputs

for process_name in tests:
    print("%s test" % process_name)
    execution = wps.execute(process_name, inputs)
    for output in execution.processOutputs:
        owslib.wps.printInputOutput(output)

##owslib.wps.monitorExecution(execution)
