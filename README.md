# bankyatest
For exec the code you can run 

```shell
C:\docker\bankyatest> python app/app.py
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 117-265-270
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```
other option is using docker you must execute:

```shell
    bankyatest> docker build -t flaskapp .
```
and after run the docker image using:

```shell
    docker run -p 5000:5000 -d flaskapp
```
after upload the server you can use postman or use a web browser to open the url:
```shell
    http://127.0.0.1:5000/cat-facts
```
