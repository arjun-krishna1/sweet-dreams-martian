from django.shortcuts import render
import tensorflow as tf

MARS_URL_COLOR = 'https://mars.nasa.gov/msl-raw-images/msss/01590/mcam/1590MR0081020030800438E01_DXXX.jpg'
MARS_URL_GRAY = 'https://mars.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/03000/opgs/edr/ncam/NLB_663825201EDR_F0850000NCAM00291M_.JPG'

def index(request):
    print("tf version")
    print(tf.__version__)
    context = {
        'image_path': MARS_URL_GRAY,
        'tf_version': tf.__version__,
    }
    return render(request, 'app/index.html', context)
