# Vulnerability Scanner

##  Overview  
Software vulnerabilities are one of the critical issues in the current software development; these vulnerabilities can pose a serious risk of exploitation and result in system compromise, information leaks, and even further financial loss. Unfortunately,
testing and manual code reviews cannot always find every vulnerability. To solve the problem we are using an efficient ML-driven approach to solve this ever growing cybersecurity issue.

# Training 
## Prerequisites
1. **Python 3**: Python 3.7+
2. **Tensorflow 2**: Tensorflow 2.0.0+
3. **Pandas**: Pandas 1.2.3
4. **Jupyter Notebook** Notebook 6.2.0
5. **CUDA Toolkit** The version matches your Tensorflow version. The code works fine without GPU support, but GPU support is highly recommanded.

## Installation
1. Check the version of the dependencies on your machine, or install the dependencies by runing:
~~~
$ pip3 install --no-cache-dir -r web-app/requirements.txt
~~~

2. Clone the project
```bash
$ git clone https://github.com/Jiawen-Zhang/Vulnerability_Scanner
```

3. Download the dataset [here](https://osf.io/d45bw/); put the files into `Vulnerability_Scanner/dataset`

4. Use the `data_formatting.ipynb` to convert the dataset to the format that can be used by our models.

5. To start a taining process, go to `Vulnerability_Scanner/model`. The `Simple_CNN_binary.ipynb` is a binary classifier; you can use this model to detect if the source code contains a vulnerability in our monitored classes.

6. To avoid training the model by yourself and save your time, I have uploaded my trained model [here](https://drive.google.com/drive/folders/1uftmaXdh3gAgbMJYk3KZSrjaKSEgzJnW?usp=sharing); you can download and use them directly.

## Experimental Evaluation

<div align=center>
    <img src="https://i.postimg.cc/c4VTPsqW/test-results.png">
</div>


# Web app  

## 1. Change directory
~~~
$ cd web-app/
~~~

## 2. Install the dependant libraries

~~~
$ pip3 install --no-cache-dir -r requirements.txt
~~~
## 3. Place the following trained models inside the directory trained_model which is at the same level as app directory
~~~
Simple_CNN_CWE119                
Simple_CNN_CWE120                    
Simple_CNN_CWE469  
Simple_CNN_CWE476                
Simple_CNN_binary
~~~

## 4. Set ENV variable for Flask
~~~
$ # Set the FLASK_APP environment variable
$ (Unix/Mac) export FLASK_APP=run.py
$ (Windows) set FLASK_APP=run.py
$ (Powershell) $env:FLASK_APP = ".\run.py"
~~~

## 5. Run the web app

Once you have ensured the above steps are done , run
~~~
$ flask run --host=0.0.0.0 --port=5000
~~~

## 6. Visit the web app
~~~
http://localhost:5000/login
~~~
