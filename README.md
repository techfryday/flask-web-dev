#   FLASK-WEB-DEV

##  Installation

Create virtual environment.
```bash
python -m venv venv
```

Activate virtual environment.
```bash
.\venv\Scripts\activate
```

Set environment variables to prevent __pycache__ files from being created, app and environment type.
```bash
$env:PYTHONDONTWRITEBYTECODE=1;$env:FLASK_APP="app";$env:FLASK_ENV = "development"
```

Install dependancies (Only once)
```bash
pip install flask
```

Run the app
```bash
flask run
```
