#api.py

from flask import Flask, jsonify
from flask_restful import Resource, Api
import sys
import re


'''
Use this API to push/pop the stack.
Connect via web browser to apache server to view the stack.

'''

app = Flask(__name__)
api = Api(app)


# Misc. presets
stack = []
heading = "<!doctype html>\n<p>Apache & Flask stack:</p>\n"


# Write file
page = "/var/www/html/index.html"
fd = open(page, "w")
fd.write(heading)
fd.close()

# Misc. presets
stack = []

class StackPush(Resource):
    # Push
    def post(self, content):
        try:
            fd = open(page, "a")
            content = '<p>' + str(content) + '</p>'
            fd.write(content)
            fd.close()
            stack.append(content)
            return jsonify({"success": 1})
        except:
            return jsonify({"success": 0})

class StackPop(Resource):
    # Pop
    def delete(self):
        try:
            content = stack.pop()
            fd = open(page, "w")
            fd.write(heading)
            for i in range(0, len(stack)):
                fd.write(stack[i])
            fd.close()
            return jsonify({"success": 1, "content": re.sub('<[^<]+?>', '', content)})
        except:
            return jsonify({"success": 0, "content": 0})

# Resources
api.add_resource(StackPush, '/push=<content>')
api.add_resource(StackPop, '/')

# Exec
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
