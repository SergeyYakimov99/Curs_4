from flask_restx import Namespace
from flask import request
from flask_restx import Namespace, Resource
from project.container import user_service
from project.setup.api.models import user


#user_ns = Namespace('users')
api = Namespace('user')


@api.route('/')
class UsersView(Resource):
    @api.marshal_with(user, as_list=True, code=200, description='OK')
    def get(self):
        all_users = user_service.get_all()

        return all_users, 200

    @api.route('/<int:bid>')
    class UserView(Resource):
        def get(self, bid):
            pass
            # b = user_service.get_one(bid)
            # return sm_d, 200

        def put(self, bid):
            pass
            # req_json = request.json
            # if "id" not in req_json:
            #     req_json["id"] = bid
            # user_service.update(req_json)
            # return "", 204

        def delete(self, bid):
            pass
            # user_service.delete(bid)
            # return "", 204

