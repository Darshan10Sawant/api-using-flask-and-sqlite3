# api-using-flask-and-sqlite3

Flask is a web framework for Python, meaning that it provides functionality for building web applications, including managing HTTP requests and rendering templates.

in api.py file created a basic Flask application
Flask runs the code in the home function and displays the returned result in the browser. In this case, the returned result is HTML markup for a home page welcoming visitors to the site hosting our API.
The process of mapping URLs to functions is called routing "@app.route('/', methods=['GET'])"
home function should be mapped to the path /. The methods list (methods=['GET']) is a keyword argument that lets Flask know what kind of HTTP requests are allowed.
in this all three python files i used only GET requests.

In api_2.py file i implemented a small API with data that have define right in our application.
"jsonify" used to convert list and dictionary into json format
