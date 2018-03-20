#coding:utf-8
from threading import *
import EventManager
import Event
import time

EVENT_ARTICAL = "Event_Artical"

class PublicAccounts:
    def __init__(self, eventManager):
        self.__eventmanager = eventManager
    
    def WriteNewArtical(self):
        event = Event.Event(type_ = EVENT_ARTICAL)
        event.dict["artical"] = u'你好'
        self.__eventmanager.SendEvent(event)
    
class Listener:
    def __init__(self, userName):
        self.__userName = userName
    
    def ReadArtical(self, event):
        print u'%s 收到新文章' % self.__userName
        print u'新内容：%s' % event.dict["artical"]

def main():
    l1 = Listener("Thinker")
    l2 = Listener("ST")
    eventManager = EventManager.EventManager()
    eventManager.AddEventListener(EVENT_ARTICAL, l1.ReadArtical)
    eventManager.AddEventListener(EVENT_ARTICAL, l2.ReadArtical)
    eventManager.Start()

    publicAcc = PublicAccounts(eventManager)
    while True:
        publicAcc.WriteNewArtical()
        time.sleep(2)

if __name__ == '__main__':
    main()
