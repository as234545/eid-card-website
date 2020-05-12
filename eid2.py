from flask import Flask, render_template,send_file,request,flash, url_for,redirect
import os
import secrets
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import requests

PEOPLE_FOLDER = os.path.join('static')
DOWNLOAD_FOLDER = os.path.join('downloads')

app = Flask(__name__)
app.secret_key = os.urandom(12)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER

@app.route("/",methods=['GET', 'POST'])
def hello():
	#img = Image.new('RGB', (100, 30), color = (73, 109, 137))
	#d = ImageDraw.Draw(img)
	#user_image = os.path.join(app.config['UPLOAD_FOLDER'], 'orange.png')
	img = Image.open("C:/Users/hh577/ZKCloud/eid/orange.png")
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype("Aaargh.ttf", 150)

	draw.text((0, 0),"Sample Text",(255,255,255), font=font)
	#ha = user_image.text((10,10), "Halah", fill=(255,255,0))
	#img.save("C:/Users/hh577/ZKCloud/eid/static/test002.png")
	img.save(secrets.token_hex(15)+'.png')
	user_image = os.path.join(app.config['UPLOAD_FOLDER'], 'test002.png')

	#fp = "C:/Users/hh577/ZKCloud/eid/static/background.png"
	#with open(fp, 'w') as f:
	#		Image.save(f)

	return render_template("index.html", user_image = user_image )

@app.route('/index')
def show_index():
	user_image = os.path.join(app.config['UPLOAD_FOLDER'], 'test001.png')
	return render_template("index.html", user_image = user_image)

@app.route('/index2')
def show_index2():
	#user_image = os.path.join(app.config['UPLOAD_FOLDER'], 'test001.png')
	return render_template("index2.html")

@app.route('/blue/')
def blue():
  user_image = os.path.join('blue.png')
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
	POST_USERNAME = str(request.form['username'])
	print(POST_USERNAME)
	img = Image.open(os.path.join('blue.png'))
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype("Aaargh.ttf", 150)
	draw.text((0, 0),POST_USERNAME,(255,255,255), font=font)
	img.save(secrets.token_hex(15)+'.png')
	flash('تم تحميل الصورة بنجاح')
	return redirect(url_for('show_index2'))


@app.route('/DownloadOrange',methods=['GET', 'POST'])
def DownloadOrange ():
	POST_USERNAME = str(request.form['username'])
	print(POST_USERNAME)
	img = Image.open(os.path.join('orange.png')) #"C:/Users/hh577/ZKCloud/eid/orange.png"
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype("Aaargh.ttf", 150)
	draw.text((0, 0),POST_USERNAME,(255,255,255), font=font)
	img.save(secrets.token_hex(15)+'.png')
	flash('You were successfully logged in')
	return redirect(url_for('show_index2'))


@app.route('/DownloadPink',methods=['GET', 'POST'])
def DownloadPink ():
	POST_USERNAME = str(request.form['username'])
	print(POST_USERNAME)
	img = Image.open(os.path.join('pink.png'))
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype("Aaargh.ttf", 150)
	draw.text((0, 0),POST_USERNAME,(255,255,255), font=font)
	img.save(secrets.token_hex(15)+'.png')
	flash('You were successfully logged in')
	return redirect(url_for('show_index2'))


@app.route("/api/downloadlogfile/<path>")
def DownloadLogFile (path = None):
    if path is None:
        self.Error(400)
    try:
        return send_file(path, as_attachment=True)
    except Exception as e:
        self.log.exception(e)
        self.Error(400)

if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0', port=5000)
