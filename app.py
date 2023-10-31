from flask import Flask, request
import sympy

app = Flask(__name__)

function_dict = {
    "factor" : ""


}



@app.route("/")
@app.route("/<function>/<equation>")
@app.route("/<function>")
def hello(function=None, equation=None):

    if function != None and equation != None :
        result = 1
        #do processing
    else: 
        return { "request incomplete": "correct and resend", "format": "url/function/equation", "example" : "http://127.0.0.1:5000/factor/2x+1", "status_code" : 500}
    
    # add in sympy processing, assign to answer.
    
    



    return {"status_code" : 200,"input" : equation, "result" : result, "function" : function}

if __name__ == '__main__':
    app.run(debug=True)