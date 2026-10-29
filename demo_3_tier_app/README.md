# Demo Three-Tier Student Registration App

A small teaching demo with three layers:

1. **Presentation tier:** HTML template and CSS in `templates/` and `static/`
2. **Application tier:** Python Flask routes and validation in `app.py`
3. **Data tier:** SQLite database accessed by helper functions in `app.py`

## Run locally or on an EC2 Linux instance

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000` on the same machine.

For EC2 access, allow inbound TCP port `5000` in the instance security group, restricted to your own IP for a lab, then open `http://YOUR_EC2_PUBLIC_IP:5000`.

This built-in Flask server is for demonstration only, not production use. Do not commit secrets or real personal data to Git.
