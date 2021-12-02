import cv2
import logging
from datetime import datetime, timedelta
from django.views.generic import View
from django.shortcuts import redirect

logger = logging.getLogger(__name__)


class FaceLoginView(View):
    def get(self, request, *args, **kwargs):
        pengklasifikasiWajah  = cv2.CascadeClassifier(
            "authentication/views/haarcascade_frontalface_default.xml"
        )
        videoCam = cv2.VideoCapture(0)

        if not videoCam.isOpened():
            logger.info("Camera did not open")
            exit()
        start = datetime.now() + timedelta(seconds=5)
        tombolQditekan = False
        while (tombolQditekan == False):
            endtime = datetime.now()
            if endtime >= start:
                logger.info('time out')
                videoCam.release()
                cv2.destroyAllWindows()
                return redirect('login')
            ret, kerangka = videoCam.read()

            if ret == True:
                abuAbu = cv2.cvtColor(kerangka, cv2.COLOR_BGR2GRAY)
                dafWajah = pengklasifikasiWajah.detectMultiScale(
                    abuAbu, scaleFactor = 1.3, minNeighbors = 2
                )

                for (x, y, w, h) in dafWajah:
                    cv2.rectangle(
                        kerangka, (x, y), (x + w, y + h), (0, 255, 0), 2
                    )

                teks = "Total Face = " + str(len(dafWajah))

                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(kerangka, teks, (0, 30), font, 1, (255, 0, 0), 1)

                cv2.imshow("Face Detector", kerangka)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    tombolQditekan = True
                    break


        videoCam.release()
        cv2.destroyAllWindows()
        return redirect('login')
