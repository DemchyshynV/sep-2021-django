import json

from rest_framework.views import APIView
from rest_framework.response import Response


class Hw1View(APIView):
    def get(self, *args, **kwargs):
        try:
            with open('users.json') as file:
                data = json.load(file)
                return Response(data)
        except Exception as err:
            return Response(err)

    def post(self, *args, **kwargs):
        try:
            new_user = self.request.data
            with open('users.json', 'r+') as file:
                users: list = json.load(file)
                users.append(new_user)
                file.seek(0)
                json.dump(users, file)
                return Response(new_user)
        except Exception as err:
            return Response(err)
