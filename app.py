import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    token_hash8 = os.getenv("TOKEN_HASH8", "missing")
    return f"""
<html>
  <body>
    <h1>Sample App Day 4</h1>
    <p>TOKEN_HASH8={token_hash8}</p>
  </body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False, threaded=False)
