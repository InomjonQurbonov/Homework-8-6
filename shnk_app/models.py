from django.db import models


class Podsystem(models.Model):
    pod_number = models.IntegerField()
    pod_name = models.CharField(max_length=100)

    def __str__(self):
        return self.pod_name

    class Meta:
        db_table = 'podsystem'
        verbose_name = 'Podsystem'
        verbose_name_plural = 'Podsystem'


class Groups(models.Model):
    podsistem = models.ForeignKey(Podsystem, on_delete=models.CASCADE)
    group_number = models.IntegerField()
    group_name = models.CharField(max_length=100)

    def __str__(self):
        return self.group_name

    class Meta:
        db_table = 'groups'
        verbose_name = 'Groups'
        verbose_name_plural = 'Groups'


class Document_types(models.Model):
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)
    document_type = models.CharField(max_length=100)
    document_number = models.IntegerField()

    def __str__(self):
        return self.document_type

    class Meta:
        db_table = 'document_types'
        verbose_name = 'Document Types'
        verbose_name_plural = 'Document Types'


class Document_files(models.Model):
    uzb_file = models.CharField(max_length=100)
    rust_file = models.CharField(max_length=100)

    def __str__(self):
        return self.uzb_file

    class Meta:
        db_table = 'document_files'
        verbose_name = 'Document Files'
        verbose_name_plural = 'Document Files'


class Document(models.Model):
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)
    document_type = models.ForeignKey(Document_types, on_delete=models.CASCADE)
    document_title = models.CharField(max_length=100)
    document_file = models.ForeignKey(Document_files, on_delete=models.CASCADE)
    doc_file = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.document_title

    class Meta:
        db_table = 'document'
        verbose_name = 'Document'
        verbose_name_plural = 'Document'
