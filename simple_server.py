import flask
import pywps

class EchoVector(pywps.Process):
    def __init__(self):
        inputs = [pywps.ComplexInput('message',
                                     'Input message',
                                     supported_formats=[pywps.Format('application/gml+xml'),
                                                        pywps.Format('text/xml')],
                                     mode=pywps.validator.mode.MODE.STRICT)]

        outputs = [pywps.ComplexOutput('response',
                                       'Output response',
                                       supported_formats=[pywps.Format('application/gml+xml')])]

        super(EchoVector, self).__init__(
            self._handler,
            identifier='echo_vector',
            title='Echo Vector Test',
            abstract='Returns the given vector',
            version='1.0.0.0',
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True
        )

    def _handler(self, request, response):
        response.outputs['response'].data = request.inputs['message'][0].data

        return response

app = flask.Flask(__name__)

wps_processes = [EchoVector()]

service = pywps.Service(wps_processes)

@app.route('/wps', methods=['GET', 'POST'])
def wps():
    return service

bind_host='127.0.0.1'
app.run(threaded=True,host=bind_host)
