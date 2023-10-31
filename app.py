from flask import Flask, request
from sympy import *

app = Flask(__name__)

function_dict = {
    "factor" : ""


}

a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = symbols('a b c d e f g h i j k l m n o p q r s t u v w x y z')


@app.route("/")
@app.route("/<function>/<equation>")
@app.route("/<function>")
def hello(function=None, equation=None):
    #data normalization
    answer= ""
    prev =""
    for i in equation:

        if i.isalpha() and prev.isdigit():
            answer+="*"+i
        elif i == "^":
            answer+="**"
        else:
            answer+=i
        prev = i
   


    #implement hashmap for functions
    if function != None and equation != None :
        
        if function == "factor":
            result = factor(eval(answer))
        

    prev = ""
    output = ""
    for i in str(result):
        if i == "*" and prev == "*":
            output+="^"
        if i.isalpha() and prev.isdigit():
            


        prev = i
        
    else: 
        return { "request incomplete": "correct and resend", "format": "url/function/equation", "example" : "http://127.0.0.1:5000/factor/x^2-1", "status_code" : 500}
    
    # add in sympy processing, assign to answer.
    
    



    return {"status_code" : 200,"input" : equation, "result" : str(result), "function" : function}

if __name__ == '__main__':
    app.run(debug=True)