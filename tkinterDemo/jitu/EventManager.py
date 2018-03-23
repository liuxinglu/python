#coding:utf-8
import Queue 
from threading import *


class EventManager:
    def __init__(self):
        self.__eventQueue = Queue.Queue()
        self.__active = False
        self.__thread = Thread(target=self.__Run)
        self.__handlers = {}

    def __EventProcess(self, event):
        if event.type_ in self.__handlers:
            for handler in self.__handlers[event.type_]:
                handler(event)

    def __Run(self):
        while self.__active == True:
            try:
                event = self.__eventQueue.get(block=True, timeout=1)
                self.__EventProcess(event)
            except Queue.Empty:
                pass

    def Start(self):
        self.__active = True
        self.__thread.start()

    def Stop(self):
        self.__active = False
        self.__thread.join()

    def AddEventListener(self, type_, handler):
        try:
            handlerList = self.__handlers[type_]
        except KeyError:
            handlerList = []
        self.__handlers[type_] = handlerList
        if handler not in handlerList:
            handlerList.append(handler)

    def RemoveEventListener(self, type_, handler):
        handlerList = self.__handlers[type_]
        if handler in handlerList:
            handlerList.remove(handler)

    def SendEvent(self, event):
        self.__eventQueue.put(event)



