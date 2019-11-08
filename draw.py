{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
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
    "            cv2.putText(img,position,(x,y), font, 0.5,(255,255,255),1,cv2.LINE_AA)\n",
    "    if event == cv2.EVENT_MOUSEMOVE:\n",
    "        position = \"(\"+str(x)+\",\"+str(y)+\")\"\n",
    "        cv2.putText(img,position,(x,y), font, 0.5,(255,255,255),1,cv2.LINE_AA)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
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
