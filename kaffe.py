from __future__ import unicode_literals
from picamera import PiCamera
from time import sleep
import boto
import time

crontable = []
outputs = []

s3bucket = 's3_bucket'
s3baseurl = 'https://your_s3_bucket/'

def capture_image():
    camera = PiCamera()
    camera.start_preview()
    sleep(3)
    camera.capture('/home/pi/kaffe.jpg')
    camera.stop_preview()
    camera.close()

def upload():
    ts = time.time()
    ukey = 'kaffe_' + str(ts) + '.jpg'
    s3 = boto.connect_s3()
    bucket = s3.get_bucket(s3bucket)
    key = bucket.new_key(ukey)
    key.set_contents_from_filename('/home/pi/kaffe.jpg', policy='public-read')
    return ukey

def process_message(data):
    if 'text' in data.keys() and  data['text'].startswith('finns det kaffe'):
        capture_image()
        key = upload()
        outputs.append([data['channel'], s3baseurl+key])