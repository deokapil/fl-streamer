"""
Run Flask's bundled web server

"""
from stapp import create_app

application = create_app()
application.run(debug=True)
