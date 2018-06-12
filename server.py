import flask
import pywps
import processes.echo_string

app = flask.Flask(__name__)

wps_processes = [processes.echo_string.EchoString()]

service = pywps.Service(wps_processes, ['pywps.cfg'])

@app.route('/wps', methods=['GET', 'POST'])
def wps():
    return service

bind_host='127.0.0.1'
app.run(threaded=True,host=bind_host)

#http://127.0.0.1:5000/wps?service=wps&version=1.0.0&request=GetCapabilities
#http://127.0.0.1:5000/wps?service=wps&version=1.0.0&request=DescribeProcess&IDENTIFIER=echo_string
#http://127.0.0.1:5000/wps?service=wps&version=1.0.0&request=Execute&IDENTIFIER=echo_string&datainputs=message=Hello%20World!
