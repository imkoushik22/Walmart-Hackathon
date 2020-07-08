from flask import Flask,abort,render_template,request,redirect,url_for
from werkzeug import secure_filename
import os     
import Fashion_reco as nn
import ipyplot

app = Flask(__name__)

save_dir = "/home/hari/Desktop/Hari/CS endeavours/Walmart-Hackathon/Frontend/static/images/"
model, emb_dict = nn.model_start()

@app.route("/")
def home():
    return render_template("shop.html")

@app.route("/shop.html")
def shop():
    return render_template("shop.html")
    
@app.route("/hari")
def salvador():
    return "Hello, Hari"

@app.route("/shop_2.html")
def shop_2():
    return render_template("shop_2.html")

@app.route("/shop_3.html")
def shop_3():
    return render_template("shop_3.html")

@app.route("/contact.html")
def contact():
    return render_template("contact.html")

@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/cart.html")
def cart():
    return render_template("cart.html")


@app.route("/contact.html")
def checkout():
    return render_template("checkout.html")


@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/thankyou.html")
def thankyou():
    return render_template("thankyou.html")

# @app.route('/upload', methods=['GET', 'POST'])
# def upload():
#     if request.method == 'POST' and 'photo' in request.files:
#         filename = photos.save(request.files['photo'])
#         rec = Photo(filename=filename, user=g.user.id)
#         rec.store()
#         flash("Photo saved.")
#         return redirect(url_for('show', id=rec.id))
#     return render_template('upload.html')

# @app.route('/photo/<id>')
# def show(id):
#     photo = Photo.load(id)
#     if photo is None:
#         abort(404)
#     url = photos.url(photo.filename)
#     return render_template('show.html', url=url, photo=photo)

#---------------

# UPLOAD_FOLDER = './test_images'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 
# @app.route('/upload.html',methods = ['GET','POST'])
# def upload_file():
#     if request.method =='POST' and 'photo' in request.files:
#         return "Hi"
#         file = request.files['photo']
#         if file:
#             return "Hi"
#             rec = Photo(filename=filename, user=g.user.id)
#             rec.store()
#             flash("Photo saved.")
#             return redirect(url_for('thankyou', id=rec.id))
#     return render_template('upload.html')

#----------------------------------

UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 
@app.route('/upload/')
def upload_file():
   return render_template('upload.html')

# @app.route('/uploader/', methods = ['GET', 'POST'])
# def uploader():
#    if request.method == 'POST' & 'photo' in request.files:
#       filename = photos.save(request.files['photo'])
#       f = request.files['file']
#       f.save(secure_filename(f.filename))
#       f.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
#       return 'Image uploaded successfully'
#    return render_template("shop.html")

@app.route('/uploader/', methods = ['GET', 'POST'])
def uploader():
   if request.method == 'POST':
      f = request.files['file']
      #f.filename = './uploads/' + f.filename
      f.save(secure_filename(f.filename))
      #f.save(secure_filename(os.path.join(app.config['UPLOAD_FOLDER'],f.filename)))
      x = f.filename
      ipyplot.plot_images([x], max_images=20, img_width=150)
      nn.query(x, 12, emb_dict, model, save_dir)
      #return 'Image uploaded successfully'
      return redirect(url_for('shop'))


if __name__ == "__main__":
    app.run(debug=True)
  #We made two new changes