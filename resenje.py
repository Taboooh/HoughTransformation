import sys
import kalman

file = open('out.txt','w')
file.write("RA 32/2014 Stevan Matovic")
file.write('\nfile  sum')

r0 = kalman.resenje("videos/video-0.avi")
file.write("\nvideo-0.avi\t" + str(r0))

r1 = kalman.resenje("videos/video-1.avi")
file.write("\nvideo-1.avi\t" + str(r1))

r2 = kalman.resenje("videos/video-2.avi")
file.write("\nvideo-2.avi\t" + str(r2))

r3 = kalman.resenje("videos/video-3.avi")
file.write("\nvideo-3.avi\t" + str(r3))

r4 = kalman.resenje("videos/video-4.avi")
file.write("\nvideo-4.avi\t" + str(r4))

r5 = kalman.resenje("videos/video-5.avi")
file.write("\nvideo-5.avi\t" + str(r5))

r6 = kalman.resenje("videos/video-6.avi")
file.write("\nvideo-6.avi\t" + str(r6))

r7 = kalman.resenje("videos/video-7.avi")
file.write("\nvideo-7.avi\t" + str(r7))

r8 = kalman.resenje("videos/video-8.avi")
file.write("\nvideo-8.avi\t" + str(r8))

r9 = kalman.resenje("videos/video-9.avi")
file.write("\nvideo-9.avi\t" + str(r9))