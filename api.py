from flask import Flask, jsonify
import sys
app = Flask(__name__)

'''
Use this API to push/pop the stack.
Connect to apache server to view the stack.

'''


#Clear default apache file.
page = "/var/www/html/index.html"
fd = open(page, "w")
fd.write('')
fd.close()


@app.route('/content=<content>', methods=['POST'])
def push_page_content(content):
    try:
        fd = open(page, "a")
        content = str(content + '\n')
        content = fd.write(content)
        fd.close()
        return jsonify({"success": 1})
    except:
        return jsonify({"success": 0})

@app.route('/', methods=["DELETE"])
def pop_page_content():
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


if __name__ == '__main__':
    app.run(debug=True)
