# Importing required libs
from flask import Flask, render_template, request
from model import preprocess_img

# Instantiating flask app
app = Flask(__name__)


# Home route
@app.route("/")
def main():
    return render_template("index.html")


# Prediction route
@app.route('/prediction', methods=['POST'])
def predict_image_file():
    try:
        if request.method == 'POST':
            print(request.files['file'])
            preprocess_img("C:\\Users\\Vivek\\Desktop\\College\\Minor Project\\colorization_main\\colorization_main\\colorization\\test_image\\"+request.files['file'].filename,request.files['file'].filename)
            print(request.files['file'].filename)
            #predict_result(img)
            return render_template("result.html", predictions=str("image saved"))

    except:
        error = "File cannot be processed."
        return render_template("result.html", err=error)


# Driver code
if __name__ == "__main__":
    app.run(port=9000, debug=True)
