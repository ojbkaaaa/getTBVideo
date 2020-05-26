# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：run
   Description :
   Author : zhang
   date：2020/4/17
-------------------------------------------------
   Change Activity: 2020/4/17:
-------------------------------------------------
"""
from flask import Flask, render_template, jsonify, request, redirect, url_for, make_response, flash
from flask_cors import CORS
from auto.main import slideMain
import asyncio



app = Flask(__name__)
CORS(app, resources=r'/*')
app.config['JSON_AS_ASCII']= False
app.secret_key = "jJInfewp(8efkd*9&jfkl"


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        values = request.values
        url = values.get('url', '')
        loop = asyncio.new_event_loop()
        res = loop.run_until_complete(slideMain(url))
        flash(res)
        return render_template('input.html')
    return render_template('input.html')

@app.route('/post/url', methods=['POST'])
def post_url():
    print('登陆成功')
    flash('登陆成功')
    return redirect(index)




if __name__ == '__main__':

    app.run(debug=True)
