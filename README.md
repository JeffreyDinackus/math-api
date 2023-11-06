# host your own calculus server



This app is a proof of concept for a calculus server. I invite you to expand on my code using sympy and flask to suit your math needs. 

# installation

install git cli if needed

clone the repository

activate the virtual environment using venv and python

install flask and sympy 

python app.py

send get requests in this format:

yourURLorIp.com/equation/symbols_used
example: 

127.0.0.1/function/equation
127.0.0.1/factor/3y+2x
public ip example
30.145.23.1/factor/3y+2x

Functions supported:
simplify 
factor 
derive 
integrate 
cos 
sin 
tan 
arccos 
arcsin 
arctan 
abs 
log 

you now have a server you can make get requests to and received JSON of the answer in return. 


Example response:

"status_code" : 200,"input" : "x^2 - 1", "result" : "(x - 1) (x + 1)", "function" : "factor"
