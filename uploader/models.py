from django.db import models

class DocumentUpload(models.Model):
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.FileField(upload_to='coverletters/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
