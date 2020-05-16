from flask import Flask, render_template,send_file,request,flash, url_for,redirect
import os
import secrets
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import requests
from io import BytesIO
import io

PEOPLE_FOLDER = os.path.join('static')
DOWNLOAD_FOLDER = os.path.join('downloads')

app = Flask(__name__)
app.secret_key = os.urandom(12)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER


#testing method must delete on prudcation
@app.route("/",methods=['GET', 'POST'])
def hello():
	return "Hello"

@app.route('/index2')
def show_index2():
	#user_image = os.path.join(app.config['UPLOAD_FOLDER'], 'test001.png')
	return render_template("index2.html")

@app.route('/blue/')
def blue():
  user_image = os.path.join('eid_cards-01.png')
  color = 'blue'
  return render_template("index3.html", user_image = user_image,  color = color)

@app.route('/orange/')
def orange():
  user_image = os.path.join('orange.png')
  color = 'orange'
  return render_template("index3.html", user_image = user_image ,  color = color)

@app.route('/pink/')
def pink():
  user_image = os.path.join('pink.png')
  color = 'pink'
  return render_template("index3.html", user_image = user_image,  color = color)

@app.route('/DownloadBlue',methods=['GET', 'POST'])
def DownloadBlue ():
	try:
		output =  io.BytesIO()
		POST_USERNAME = str(request.form['username'])
		print(POST_USERNAME)
		img = Image.open(os.path.join('eid_cards-01.png'))
		buffer = ImageDraw.Draw(img)
		font = ImageFont.truetype("Aaargh.ttf", 150)
		buffer.text((0, 0),POST_USERNAME,(255,255,255), font=font)
		img.save(output, format="png", optimize=True)
		file_name = secrets.token_hex(15)+'.png'
		output.seek(0)
		flash('تم تحميل الصورة بنجاح')
		return send_file(output, mimetype="image/png",as_attachment=True , attachment_filename=file_name)

	except Exception as e:
		print(e)
		return redirect(url_for('hello'))


@app.route('/DownloadOrange',methods=['GET', 'POST'])
def DownloadOrange ():
	try:
		output =  io.BytesIO()
		POST_USERNAME = str(request.form['username'])
		print(POST_USERNAME)
		img = Image.open(os.path.join('orange.png'))
		buffer = ImageDraw.Draw(img)
		font = ImageFont.truetype("Aaargh.ttf", 150)
		buffer.text((0, 0),POST_USERNAME,(255,255,255), font=font)
		img.save(output, format="png", optimize=True)
		file_name = secrets.token_hex(15)+'.png'
		output.seek(0)
		flash('تم تحميل الصورة بنجاح')
		return send_file(output, mimetype="image/png",as_attachment=True , attachment_filename=file_name)

	except Exception as e:
		print(e)
		return redirect(url_for('hello'))


@app.route('/DownloadPink',methods=['GET', 'POST'])
def DownloadPink ():
	try:
		output =  io.BytesIO()
		POST_USERNAME = str(request.form['username'])
		print(POST_USERNAME)
		img = Image.open(os.path.join('pink.png'))
		buffer = ImageDraw.Draw(img)
		font = ImageFont.truetype("Aaargh.ttf", 150)
		buffer.text((0, 0),POST_USERNAME,(255,255,255), font=font)
		img.save(output, format="png", optimize=True)
		file_name = secrets.token_hex(15)+'.png'
		output.seek(0)
		flash('تم تحميل الصورة بنجاح')
		return send_file(output, mimetype="image/png",as_attachment=True , attachment_filename=file_name)

	except Exception as e:
		print(e)
		return redirect(url_for('hello')) #change for showindex2 on prduction


if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0', port=5000)
