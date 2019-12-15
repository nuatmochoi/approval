from docx import Document
import pickle

def findForm(documentTag):
    """ with open('tagCheckList.txt', 'rb'):
                data = pickle.load(tagCheckList)"""
    loadedDocx = Document('media/DOCXform/'+documentTag + ".docx")

    return loadedDocx








