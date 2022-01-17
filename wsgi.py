from flask import Flask, request, make_response

app = Flask(__name__)


@app.route("/")
def alles():
    return """
<head>
  <link href="https://unpkg.com/@triply/yasgui/build/yasgui.min.css" rel="stylesheet" type="text/css" />
  <script src="https://unpkg.com/@triply/yasgui/build/yasgui.min.js"></script>
</head>
<body>
  <div id="yasgui"></div>
  <script>
    const yasgui = new Yasgui(document.getElementById("yasgui"), {
                                requestConfig: { endpoint: "/nfdico/sparql" },
                                copyEndpointOnNewTab: false,
    });
  </script>
</body>
"""
