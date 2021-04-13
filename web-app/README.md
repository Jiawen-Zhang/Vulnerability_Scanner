# Vulnerability Scanner

# Web app  


## 1. Install the dependant librariess

~~~
$ pip3 install --no-cache-dir -r requirements.txt
~~~
## 2. Place the following trained models inside the directory trained_model which is at the same level as app directory
You can find a recent copy of the trained model [here](https://drive.google.com/drive/folders/1uftmaXdh3gAgbMJYk3KZSrjaKSEgzJnW?usp=sharing);
~~~
Simple_CNN_CWE119                
Simple_CNN_CWE120                    
Simple_CNN_CWE469  
Simple_CNN_CWE476                
Simple_CNN_binary
~~~

## 3. Run the web app
~~~
$ # Set the FLASK_APP environment variable
$ (Unix/Mac) export FLASK_APP=run.py
$ (Windows) set FLASK_APP=run.py
$ (Powershell) $env:FLASK_APP = ".\run.py"
~~~

## 4. Run the web app

Once you have ensured the above steps are done , run
~~~
$ flask run --host=0.0.0.0 --port=5000
~~~

## 5. Visit the web app
~~~
http://localhost:5000/login
~~~
