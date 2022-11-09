import flask
import os
import numpy
# import scipy.misc
# import imageio
import keras.models
from PIL import Image

server = flask.Flask(__name__)
@server.route('/', methods=['GET', 'POST'])

def handle_request():
    capturedImage = flask.request.files['image']
    stored_image = flask.request.files['image']

    # img = scipy.misc.imread(capturedImage, mode="L")
    # img = imageio.imread(capturedImage)
    img = Image.open(capturedImage).convert('L')
    img = numpy.asarray(img)
    img = numpy.resize(img,28*28)
    print(img.shape)

    # Link used to load a saved model and predict our label
    # Source - https://stackoverflow.com/questions/35074549/how-to-load-a-model-from-an-hdf5-file-in-keras
    ml_model = keras.models.load_model("C:/Users/pkbhat/Downloads/CSE_535_MC/MLModel/model.h5")
    # C:\Users\pkbhat\Downloads\CSE_535_MC\MLModel - is the local path where our model is stored
    
    predicted_label = ml_model.predict(numpy.array([img]))[0]
    # ans = numpy.where(predicted_label == 1)
    ans = 0
    for i in range(len(predicted_label)):
        if predicted_label[i] == 1:
            ans = i
    print(ans)
    savePath = "C:/Users/pkbhat/Downloads/MobileComputing/Uploads/" + str(ans) + "/"
    # C:\Users\pkbhat\Downloads\MobileComputing\Uploads - is the local path where our image is stored
    
    # Source - https://stackoverflow.com/questions/44926465/upload-image-in-flask
    savePathExists = os.path.exists(savePath)
    if not savePathExists:
        os.makedirs(savePath)
    stored_image.save(savePath+stored_image.filename)
    return "Image has been uploaded Successfully!"

server.run(host="0.0.0.0", port=5000, debug=True)