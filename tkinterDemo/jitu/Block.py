#coding:utf-8
import EventManager
import Event
import Tkinter
from PIL import ImageTk, Image
# from JiTu import Type, tl, ImgPlus

class Block:
    CLICK = "EVENT::CLICK"
    def __init__(self, eventManager):
        pass
        # self.__eventmanager = eventManager

    def setType(self, t):
        pass
        # self._type = t
        # if t == Type.Ji:
        #     self._t = ImgPlus("../../jitu/img_xiaoJiFangKuai.png")
        # elif t == Type.Spider:
        #     self._t = ImgPlus("../../jitu/img_xiaoJiFangKuai.png")
        # elif t == Type.Tu:
        #     self._t = ImgPlus("../../jitu/img_tuZiFangKuai.png")
        # elif t == Type.Wing:
        #     self._t = ImgPlus("../../jitu/img_xiaoJiFangKuai.png")
        # self._wi = self._t.createWidget("Button", tl)
        # self._wi.blockType = self._t
        # self._wi.bind("<Button-1>", self.clickHandler)
    
    def clickHandler(self, e):
        pass
        # event = Event.Event(type_ = CLICK)
        # event.dict["target"] = e.target
        # event.dict["type"] = e.target.blockType
        # self.__eventmanager.SendEvent(event)
    
    def setPos(self, imgx, imgy):
        pass
        # self._t.setPos(self._wi, imgx, imgy)

        

        
