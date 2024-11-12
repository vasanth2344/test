from flask import Flask, render_template_string
import subprocess
from datetime import datetime

app = Flask(_name_)


@app.route("/")
def system_info():
    # Define server information
    name = "sample_name"
    user = "codespace"
    server_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

    # Get top command output in batch mode with one iteration
    top_output = subprocess.getoutput("top -b -n 1")

    # HTML template for rendering
    html_template = """
    <html>
        <body>
            <h2>Name: {{ name }}</h2>
            <p>User: {{ user }}</p>
            <p>Server Time (IST): {{ server_time }}</p>
            <h3>TOP output:</h3>
            <pre>{{ top_output }}</pre>
        </body>
    </html>
    """

    return render_template_string(
        html_template,
        name=name,
        user=user,
        server_time=server_time,
        top_output=top_output,
    )


if _name_ == "_main_":
    app.run(debug=True, host="0.0.0.0", port=8000)