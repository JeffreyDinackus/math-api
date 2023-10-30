# host your own calculus server



This app is a proof of concept for a calculus server. I invite you to expand on my code using sympy and flask to suit your math needs. 

# installation

install git cli if needed

clone the repository

activate the virtual environment using venv and python

python app.py

send get requests in this format:

yourURLorIp.com/equation/symbols_used
example: 

127.0.0.1/x2-1/x
127.0.0.1/3y+2x/xy
public ip example
30.145.23.1/5x+-8/x


you now have a server you can make get requests to and received JSON of the answer in return. 


Example response: