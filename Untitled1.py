{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'position' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-29-37e105ff2338>\u001b[0m in \u001b[0;36mdraw_circle\u001b[1;34m(event, x, y, flags, param)\u001b[0m\n\u001b[0;32m     19\u001b[0m         \u001b[1;32melif\u001b[0m \u001b[0mmode\u001b[0m \u001b[1;33m==\u001b[0m \u001b[1;36m2\u001b[0m \u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     20\u001b[0m             \u001b[0mpostion\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34m\"(\"\u001b[0m\u001b[1;33m+\u001b[0m\u001b[0mstr\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mx\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m+\u001b[0m\u001b[1;34m\",\"\u001b[0m\u001b[1;33m+\u001b[0m\u001b[0mstr\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0my\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m+\u001b[0m\u001b[1;34m\")\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 21\u001b[1;33m             \u001b[0mcv2\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mputText\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mimg\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mposition\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mx\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0my\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mfont\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m1\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m255\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m255\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m255\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mcv2\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mLINE_AA\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     22\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     23\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'position' is not defined"
     ]
    }
   ],
   "source": [
    "import cv2\n",
    "import numpy as np\n",
    "\n",
    "mode = 0;\n",
    "\n",
    "font = cv2.FONT_HERSHEY_SIMPLEX\n",
    "# mouse callback function\n",
    "def draw_circle(event,x,y,flags,param):\n",
    "    global mode, font\n",
    "    if event == cv2.EVENT_RBUTTONUP: # left button down event\n",
    "        mode = (mode+1)%3\n",
    "    if event == cv2.EVENT_LBUTTONUP:\n",
    "        if mode == 0 :\n",
    "            cv2.rectangle(img,(x-10,y-10),(x+10,y+10),(0,255,0),-1)\n",
    "        \n",
    "        elif mode == 1 :\n",
    "            cv2.circle(img,(x,y),10,(255,0,0),-1)\n",
    "        \n",
    "        elif mode == 2 :\n",
    "            position = \"(\"+str(x)+\",\"+str(y)+\")\"\n",
    "            cv2.putText(img,position,(x,y), font, 1,(255,255,255),1,cv2.LINE_AA)\n",
    "        \n",
    "            \n",
    "img = np.zeros((512,512,3), np.uint8)\n",
    "cv2.namedWindow('image')\n",
    "cv2.setMouseCallback('image',draw_circle)\n",
    "\n",
    "while(1):\n",
    "    cv2.imshow('image',img)\n",
    "    if cv2.waitKey(20) & 0xFF == 27: # enter ESC (0):무한정 대기 (20):20m/s 마다 갱신을 하겠다 라는 뜻\n",
    "        break\n",
    "\n",
    "cv2.destroyAllWindows()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
