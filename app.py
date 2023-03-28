from waitress import serve
import falcon
# import routes
# from .config import init_session
from resource import ApiDetailResource
# import routes
app = falcon.App()
app.add_route("/", ApiDetailResource())

# init_session()
if __name__ == '__main__':
   serve(app, host='0.0.0.0', port=8000)

