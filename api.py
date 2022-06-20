#api.py

from flask import Flask, jsonify
from flask_restful import Resource, Api
import sys


'''
Use this API to push/pop the stack.
Connect via web browser to apache server to view the stack.

'''

app = Flask(__name__)
api = Api(app)

# Clear default apache file
page = "/var/www/html/index.html"
#fd = open(page, "w")
#fd.write('')
#fd.close()

class StackPush(Resource):
    # Push
    def post(self, content):
        try:
            fd = open(page, "a")
            content = str(content + '\n')
            content = fd.write(content)
            fd.close()
            return jsonify({"success": 1})
        except:
            return jsonify({"success": 0})

class StackPop(Resource):
    # Pop
    def delete(self):
        try:
            fd = open(page, "r+")
            content = fd.readlines()
            fd.seek(0)
            fd.truncate()
            for i in range(len(content)-1):
                fd.write(content[i])
            fd.close()
            return jsonify({"success": 1, "content": content[-1].rstrip()})
        except:
            return jsonify({"success": 0, "content": 0})

# Resources
api.add_resource(StackPush, '/push=<content>')
api.add_resource(StackPop, '/')

# Exec
if __name__ == '__main__':
    app.run(debug=True)
