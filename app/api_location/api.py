

class Position(restful.Resource):
    def post(self):
        longtitude = request.json['longitude']
        latitude = request.json['latitude']
        elevation = request.json['elevation']
        speed = request.json['speed']
        return 'OK'
