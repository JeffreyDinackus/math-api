from flask import Flask, request
import sympy

app = Flask(__name__)

@app.route("/")
@app.route("/<equation>/<symbols>")
@app.route("/<equation>/")
def hello(equation=None, symbols=None):

    if symbols != None and equation != None :

        symanswer = list(symbols)
        # problem = list(equation)
    else: 
        return { "request incomplete": "format: url/equation/symbolsUsed example: 127.0.0.1/2x-y/xy", "status_code" : 500}
    
    # add in sympy processing, assign to answer.
    
    answer = 1



    return {"status_code" : 200,"input" : equation, "answer" : answer, "symbols" : symanswer}

if __name__ == '__main__':
    app.run(debug=True)