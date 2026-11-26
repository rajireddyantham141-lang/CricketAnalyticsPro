# Cricket Analytics Pro

A mobile-friendly Flask + HTML/CSS/JavaScript starter application.

## Important data note
This starter intentionally uses fictional demonstration match records. It does **not** provide live scores, verified historical results, or trained AI predictions. To add those features, connect a licensed cricket data provider and build a verified ball-by-ball database and prediction pipeline.

## Run locally
```bash
pip install -r backend/requirements.txt
python backend/app.py
```
Open http://127.0.0.1:5000

## Deploy on Render
1. Push this repository to GitHub.
2. In Render, create a new Web Service and connect the repository.
3. Build command: `pip install -r backend/requirements.txt`
4. Start command: `gunicorn --chdir backend app:app`
5. Deploy. Render supplies the `PORT` environment variable.

The included `render.yaml` can also be used as a Blueprint configuration.
