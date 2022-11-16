import subprocess
from subprocess import Popen, PIPE
from subprocess import check_output
from flask import Flask

def get_shell_script_output_using_communicate():
    session = Popen(['./script.sh'], stdout=PIPE, stderr=PIPE)
    stdout, stderr = session.communicate()
    if stderr:
        raise Exception("Error "+str(stderr))
    return stdout.decode('utf-8')

app = Flask(__name__)

@app.route('/',methods=['GET',])
def home():
    return '<pre>'+get_shell_script_output_using_communicate()+'</pre>'

app.run(debug=False, host='0.0.0.0', port=5000)
