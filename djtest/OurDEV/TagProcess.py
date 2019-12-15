#from docx import Document

from OurDEV import DocumentProcess
from dj.models import TagModel

def modifyDocxByTag(document, tag_sender, tag_receiver, tag_date):
    for para in document.paragraphs:
        style = para.style
        if 'target_sender' in para.text:
            para.text =para.text.replace("target_sender", tag_sender)
        if 'target_receiver' in para.text:
            para.text =para.text.replace("target_receiver", tag_receiver)
        if 'target_date' in para.text:
            para.text =para.text.replace("target_date", tag_date)
        para.style = style

    return document

def modifyAddtion(document, model, str_more1, str_more2, str_more3, str_more4, str_more5):
    changeString(document, str_more1, model.tag_target1)
    changeString(document, str_more2, model.tag_target2)
    changeString(document, str_more3, model.tag_target3)
    changeString(document, str_more4, model.tag_target4)
    changeString(document, str_more5, model.tag_target5)

    return document

def changeString(document, string, tagTarget):
    for para in document.paragraphs:
        style = para.style
        if tagTarget in para.text:
            para.text = para.text.replace(tagTarget, string)
        para.style = style

    return document

def createApproval(tag_sender, tag_receiver, tag_date, tag_documentType):
    document = DocumentProcess.findForm(tag_documentType)
    document = modifyDocxByTag(document, tag_sender, tag_receiver, tag_date)

    return document