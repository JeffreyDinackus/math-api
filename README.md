# host your own calculus server



This app is a proof of concept for a calculus server. I invite you to expand on my code using sympy and flask to suit your math needs. 

# TODO

- [X] Basic Functions based on Newton Vercel
- [ ] Add find Zereos, Tangent and Area
- [ ] Expand to multiple functions per request
- [ ] AI to solve more advanced problems?
- [X] Test current deployment


# installation

install git cli if needed

clone the repository

activate the virtual environment using venv and python

install flask and sympy 

python app.py



# send get requests in this format:

> yourURLorIp.com/function/equation <br>

### example: 

> 127.0.0.1/function/equation <br>

> 127.0.0.1/factor/3y+2x <br>

### public ip example <br>

> 30.145.23.1/factor/3y+2x <br>

# Functions supported:

- simplify <br>
- factor  <br>
- derive  <br>
- integrate  <br>
- cos  <br>
- sin  <br>
- tan  <br>
- arccos  <br>
- arcsin  <br>
- arctan  <br>
- abs  <br>
- log  <br>

you now have a server you can make get requests to and received JSON of the answer in return. 


# Example response:

"status_code" : 200,"input" : "x^2 - 1", "result" : "(x - 1) (x + 1)", "function" : "factor"
