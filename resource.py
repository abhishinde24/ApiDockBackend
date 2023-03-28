import falcon

class ApiDetailResource:
    def on_get(self,req,resp):
        result ={"result": "Hello Word!"}
        resp.media = result
        resp.status = falcon.HTTP_OK
        resp.content_type = falcon.MEDIA_JSON