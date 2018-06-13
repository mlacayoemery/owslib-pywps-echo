import os
import importlib

import flask
import pywps

process_path = os.path.join(os.path.dirname(__file__), "processes")

app = flask.Flask(__name__)

wps_processes = []

for file_name in os.listdir(process_path):
    if file_name != "__init__.py" and file_name.endswith(".py"):
        module_name = os.path.splitext(file_name)[0]
        m = importlib.import_module(".".join(["processes",
                                              module_name]))
        print("Found process %s" % module_name)
        c = getattr(m, "WebProcess")
        
        wps_processes.append(c())


service = pywps.Service(wps_processes, ['pywps.cfg'])

@app.route('/wps', methods=['GET', 'POST'])
def wps():
    return service

bind_host='127.0.0.1'
app.run(threaded=True,host=bind_host)

#http://127.0.0.1:5000/wps?service=wps&version=1.0.0&request=GetCapabilities
#http://127.0.0.1:5000/wps?service=wps&version=1.0.0&request=DescribeProcess&IDENTIFIER=echo_string
#http://127.0.0.1:5000/wps?service=wps&version=1.0.0&request=Execute&IDENTIFIER=echo_string&datainputs=message=Hello%20World!
