# author:ToddCombs
from flask import request
from flask import Flask


app = Flask(__name__)

@app.route('/getInfo')
def hello_world():
    """
    反爬虫实例，如果请求头User-Agent包含User-Agent: python-requests/2.21.0等字段
    则return。如果是正常浏览器用户访问，则return"这里有很多数据么？"
    """
    if(str(request.headers.get('User-Agent')).startswith('python')):
        return '爬什么虫？爬哪？'
    else:
        return '这里有很多数据么？'


if __name__ == '__main__':

    app.run(debug=True)


