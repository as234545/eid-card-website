from flask import Flask, render_template,send_file,request,flash, url_for,redirect
import os
import secrets
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import requests
from io import BytesIO
import io
# install: pip install --upgrade arabic-reshaper
import arabic_reshaper

# install: pip install python-bidi
from bidi.algorithm import get_display

PEOPLE_FOLDER = os.path.join('static')
DOWNLOAD_FOLDER = os.path.join('downloads')

app = Flask(__name__)
app.secret_key = os.urandom(12)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER


#testing method must delete on prudcation

@app.route('/hello')
def hello():
	#user_image = os.path.join(app.config['UPLOAD_FOLDER'], 'test001.png')
	return "brrr"

@app.route('/')
def show_index2():
	#user_image = os.path.join(app.config['UPLOAD_FOLDER'], 'test001.png')
	return render_template("index2.html")

@app.route('/blue/')
def blue():
  user_image = os.path.join('eid_cards_names-01.png')
  color = 'blue'
  return render_template("index3.html", user_image = user_image,  color = color)

@app.route('/orange/')
def orange():
  user_image = os.path.join('eid_cards_names-02.png')
  color = 'orange'
  return render_template("index3.html", user_image = user_image ,  color = color)

@app.route('/pink/')
def pink():
  user_image = os.path.join('eid_cards_names-03.png')
  color = 'pink'
  return render_template("index3.html", user_image = user_image,  color = color)

@app.route('/yallow/')
def yallow():
  user_image = os.path.join('eid_cards_names-04.png')
  color = 'yallow'
  return render_template("index3.html", user_image = user_image,  color = color)

@app.route('/DownloadBlue',methods=['GET', 'POST'])
def DownloadBlue ():
	try:
		output =  io.BytesIO()
		POST_USERNAME = str(request.form['username'])
		reshaped_text = arabic_reshaper.reshape(POST_USERNAME)    # correct its shape
		bidi_text = get_display(reshaped_text) 
		print(bidi_text)
		img = Image.open(os.path.join('static/eid_cards-01.png'))
		imgW, imgH = img.size
		print(imgW)
		buffer = ImageDraw.Draw(img)
		font = ImageFont.truetype("static/fonts/ArbFONTS-GE-SS-Unique-Bold.otf", 150 )
		w, h = buffer.textsize(bidi_text, font)
		imgW, imgH = img.size
		nullH = (imgH-h)
		print(imgH, h)

		buffer.text(((imgW-w)/2, nullH-1000),bidi_text,(255,255,255), font=font)
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
		reshaped_text = arabic_reshaper.reshape(POST_USERNAME)    # correct its shape
		bidi_text = get_display(reshaped_text) 
		print(bidi_text)
		img = Image.open(os.path.join('static/eid_cards-02.png'))
		imgW, imgH = img.size
		print(imgW)
		buffer = ImageDraw.Draw(img)
		font = ImageFont.truetype("static/fonts/ArbFONTS-GE-SS-Unique-Bold.otf", 150 )
		w, h = buffer.textsize(bidi_text, font)
		imgW, imgH = img.size
		nullH = (imgH-h)
		print(imgH, h)

		buffer.text(((imgW-w)/2-1000, nullH-500),bidi_text,(34,51,68), font=font)
		img.save(output, format="png", optimize=True)
		file_name = secrets.token_hex(15)+'.png'
		output.seek(0)
		flash('تم تحميل الصورة بنجاح')
		return send_file(output, mimetype="image/png",as_attachment=True , attachment_filename=file_name)

	except Exception as e:
		print(e)
		return redirect(url_for('show_index2'))


@app.route('/DownloadPink',methods=['GET', 'POST'])
def DownloadPink ():
	try:
		output =  io.BytesIO()
		POST_USERNAME = str(request.form['username'])
		reshaped_text = arabic_reshaper.reshape(POST_USERNAME)    # correct its shape
		bidi_text = get_display(reshaped_text) 
		print(bidi_text)
		img = Image.open(os.path.join('static/eid_cards-03.png'))
		imgW, imgH = img.size
		print(imgW)
		buffer = ImageDraw.Draw(img)
		font = ImageFont.truetype("static/fonts/ArbFONTS-GE-SS-Unique-Bold.otf", 150 )
		w, h = buffer.textsize(bidi_text, font)
		imgW, imgH = img.size
		nullH = (imgH-h)
		print(imgH, h)

		buffer.text(((imgW-w)/2, nullH-1000),bidi_text,(100,114,130), font=font)
		img.save(output, format="png", optimize=True)
		file_name = secrets.token_hex(15)+'.png'
		output.seek(0)
		flash('تم تحميل الصورة بنجاح')
		return send_file(output, mimetype="image/png",as_attachment=True , attachment_filename=file_name)

	except Exception as e:
		print(e)
		return redirect(url_for('show_index2'))


@app.route('/DownloadYallow',methods=['GET', 'POST'])
def DownloadYallow ():
	try:
		output =  io.BytesIO()
		POST_USERNAME = str(request.form['username'])
		reshaped_text = arabic_reshaper.reshape(POST_USERNAME)    # correct its shape
		bidi_text = get_display(reshaped_text) 
		print(bidi_text)
		img = Image.open(os.path.join('static/eid_cards-04.png'))
		imgW, imgH = img.size
		print(imgW)
		buffer = ImageDraw.Draw(img)
		font = ImageFont.truetype("static/fonts/ArbFONTS-GE-SS-Unique-Bold.otf", 150 )
		w, h = buffer.textsize(bidi_text, font)
		imgW, imgH = img.size
		nullH = (imgH-h)
		print(imgH, h)

		buffer.text(((imgW-w)/2, nullH-1100),bidi_text,(108,109,109), font=font)
		img.save(output, format="png", optimize=True)
		file_name = secrets.token_hex(15)+'.png'
		output.seek(0)
		flash('تم تحميل الصورة بنجاح')
		return send_file(output, mimetype="image/png",as_attachment=True , attachment_filename=file_name)

	except Exception as e:
		print(e)
		return redirect(url_for('show_index2')) #change for showindex2 on prduction


if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0', port=5000)

