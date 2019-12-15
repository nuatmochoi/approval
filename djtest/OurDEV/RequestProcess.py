import threading

#import mammoth
#import pypandoc

from OurDEV import TagProcess
from docx import Document
import json, os

def createApproval(tag_sender, tag_receiver, tag_date, tag_documentType) :
    # t = threading.Thread(target=doThread, args=(self, tag_sender, tag_receiver, tag_date, tag_documentType))
    document = TagProcess.createApproval(tag_sender, tag_receiver, tag_date, tag_documentType)
    return document


def doThread(tag_sender, tag_receiver, tag_date, tag_documentType):
    """WebInterface에게 연결 정보를 받아서 직접 결과 DOCX를 전송 (google API 사용?)"""
    TagProcess.createApproval(tag_sender, tag_receiver, tag_date, tag_documentType)


