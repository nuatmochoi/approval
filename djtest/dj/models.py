from django.db import models
from django.forms import ModelForm



class Tag(models.Model):
    tag_choice=(
        ('A','A'),
        ('B','B'),
                )

    string1=models.CharField(max_length=30)
    string2 = models.CharField(max_length=30)
    string3 = models.CharField(max_length=30)
    #string4 = models.ForeignKey('tag_str',default=1,on_delete=models.CASCADE,null=True)
    string4 = models.CharField(max_length=30, null=True)



class docxFor(models.Model):
    formName = models.CharField(max_length=30)
    formDocx = models.FileField()

class uploaded_doc(models.Model):
    file=models.FileField(null=True)
    string_mail=models.CharField(max_length=1000,null=True)

class document(models.Model):

    title = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/',null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)


class approved_doc(models.Model):
    approval=models.CharField(max_length=50, null=True)
    title = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=255, blank=True,null=True)
    document = models.FileField(upload_to='documents/',null=True)

class denied_doc(models.Model):
    deny=models.CharField(max_length=50,null=True)
    title = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/',null=True)


class tag_str(models.Model):
    name=models.CharField(max_length=10,null=True)
    #parent = models.ForeignKey('tag_str', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class chat_record(models.Model):
    chat_str=models.CharField(max_length=1000,blank=True,null=True)
    room_name=models.CharField(max_length=100,null=True)

class TagModel(models.Model):
    file = models.FileField(upload_to='DOCXform/')
    tag_document = models.CharField(max_length=30)

    tag_name1 = models.CharField(null=True, blank=True, max_length=30)
    tag_target1 = models.CharField(null=True, blank=True, max_length=30)
    tag_name2 = models.CharField(null=True, blank=True, max_length=30)
    tag_target2 = models.CharField(null=True, blank=True, max_length=30)
    tag_name3 = models.CharField(null=True, blank=True, max_length=30)
    tag_target3 = models.CharField(null=True, blank=True, max_length=30)
    tag_name4 = models.CharField(null=True, blank=True, max_length=30)
    tag_target4 = models.CharField(null=True, blank=True, max_length=30)
    tag_name5 = models.CharField(null=True, blank=True, max_length=30)
    tag_target5 = models.CharField(null=True, blank=True, max_length=30)