from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def log_info():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    user_agent = request.headers.get('User-Agent')
    email = request.args.get('email', 'unknown')
    timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

    with open("visitor_log.txt", "a") as f:
        f.write(f"{timestamp} | Email: {email} | IP: {ip} | Agent: {user_agent}\n")

    return """
    <html>
        <head><title>Tracking Page</title></head>
        <body>
            <h1>Welcome!</h1>
            <p>Your visit has been logged for security and analytics purposes.</p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
