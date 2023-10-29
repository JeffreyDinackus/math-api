from flask import Flask, request
import sympy

app = Flask(__name__)

@app.route("/")
@app.route("/<equation>/<symbols>")
def hello(equation=None, symbols=None):
    answer = 1
    symanswer = list(symbols)
    
    return {"status_code" : 200,"input" : equation, "answer" : answer, "symbols" : symanswer}
 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(debug=True)