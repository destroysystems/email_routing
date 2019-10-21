# Email Routing

This is a simple Flask app that allows routing emails based on the recipient's address. For more information about it, check [this blog post](https://destroy.systems).

TODO: when the post is done, update the link

## Running

This app requires `python3` (because we're in 2019 already). To run it, create a `virtualenv`, install the requirements from `requirements.txt`, create an environment variable pointing to the app and run. To do that, follow the steps below:

```bash
$ cd email_routing
$ python3 -m venv .venv
$ source .venv/bin/activate
(.venv) $ pip install -r requirements.txt
(.venv) $ FLASK_APP=app.py flask run
```

You should see something similar to the following in your shell:
```
 * Serving Flask app "app.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

After that, you can perform GETs and POSTs to http://localhost:5000 (or a different port, check your output to be sure).
