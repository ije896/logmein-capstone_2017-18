from flask import render_template, redirect, url_for

class Index:
	@staticmethod
	def page():
		return render_template('index.html')