# coding=utf-8
import os
from flask import Flask, request
import json
from textSummary import TextSummary
app = Flask(__name__)


@app.route('/api/calc_summary/', methods=['GET', 'POST'])
def calc_summary():
	data = request.data
	data = data.decode(encoding="utf-8")
	content = json.loads(data)
	text = content['text']
	title = content['title']
	text_summary = TextSummary()
	text_summary.set_text(title, text)
	summary = text_summary.calc_summary()
	print(''.join(summary))
	return json.dumps(summary)


@app.route('/')
def index():
	# 直接返回静态文件
	return app.send_static_file("index.html")


if __name__ == '__main__':

	port = int(os.environ.get("PORT", "5000"))
	app.run(host='0.0.0.0', port=port, debug=True)
