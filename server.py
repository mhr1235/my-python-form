from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    # Serve your static index.html
    return open("index.html").read()

@app.route('/cgi-bin/submit.py', methods=['GET', 'POST'])
def submit():
    name = request.form.get('name')
    city = request.args.get('city')
    if request.method == 'POST' and name:
        message = f"Hello, {name}! (sent via POST)"
    elif request.method == 'GET' and city:
        message = f"Ah, you're from {city}! (sent via GET)"
    else:
        message = "No valid data received."
    
    return render_template_string(f"""
    <!DOCTYPE html>
    <html>
      <head><title>Response</title></head>
      <body>
        <h1>{message}</h1>
        <p>Request method: {request.method}</p>
        <a href="/">Go back</a>
      </body>
    </html>
    """)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
