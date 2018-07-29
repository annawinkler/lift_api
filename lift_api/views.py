from lift_api import app


@app.route('/')
def index():
    return 'Lift Inspections Data API'
