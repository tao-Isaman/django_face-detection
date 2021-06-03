from django.shortcuts import render
from django.views import View
from django.http import HttpResponse , StreamingHttpResponse ,request


from .camera import VideoCameraFace
from .handtracker import VideoCameraHand


# Create your views here.


def gen(camera):
    while True:
        #get camera frame
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# @gzip.gzip_page
def face(request):
    try:
        return StreamingHttpResponse(gen(VideoCameraFace()), content_type="multipart/x-mixed-replace;boundary=frame")
    except:  # This is bad! replace it with proper handling
        pass

def hand(request):
    try:
        return StreamingHttpResponse(gen(VideoCameraHand()), content_type="multipart/x-mixed-replace;boundary=frame")
    except:  # This is bad! replace it with proper handling
        pass

class Camera(View):
    template_name = 'camera.html'
    word = 'ได้เขียน django แล้ว'

    def get(self, request):
        context = {
            'data': self.word
        }
        return render(request, self.template_name, context)