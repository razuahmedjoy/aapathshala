from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class medical(models.Model):
    name = models.CharField(max_length=50)
    gpa_table_name = models.CharField(max_length=50,null=True, blank=True)
    ssc_gpa = models.DecimalField(max_digits=3,decimal_places=2,default=0)
    hsc_gpa = models.DecimalField(max_digits=3,decimal_places=2,default=0)
    hsc_bio_gpa = models.DecimalField(max_digits=3,decimal_places=2,default=0)
    total_gpa = models.DecimalField(max_digits=4,decimal_places=2,default=0)
    total_sit = models.IntegerField(null=True, blank=True)
    application_link = models.CharField(max_length=200,null=True,blank=True)
    
    exam_value = models.IntegerField(null=True, blank=True)
    allow_second_time = models.BooleanField(default=False)
    details_info = RichTextField(blank=True, null=True)
    ssc_gpa_multiply = models.DecimalField(max_digits=4,decimal_places=2,null=True,blank=True)
    hsc_gpa_multiply = models.DecimalField(max_digits=4,decimal_places=2,null=True,blank=True)
    def __str__(self):
        return self.name

class engineering(models.Model):
    name= models.CharField(max_length=50)
    gpa_table_name = models.CharField(max_length=50,null=True, blank=True)
    ssc_gpa = models.DecimalField(max_digits=3,decimal_places=2,default=0)
    hsc_gpa = models.DecimalField(max_digits=3,decimal_places=2,default=0)
    total_gpa = models.DecimalField(max_digits=4,decimal_places=2,default=0)
    physics_gpa = models.DecimalField(max_digits=4,decimal_places=2,default=0)
    chemistry_gpa = models.DecimalField(max_digits=4,decimal_places=2,default=0)
    hmath_gpa = models.DecimalField(max_digits=4,decimal_places=2,default=0)
    english_gpa = models.DecimalField(max_digits=4,decimal_places=2,default=0)
    subject_total_gpa = models.DecimalField(max_digits=4,decimal_places=2,default=0)

    extra_condition = models.TextField(null=True,blank=True)

    total_sit = models.IntegerField(null=True, blank=True)
    application_link = models.CharField(max_length=200,null=True,blank=True)
    
    exam_value = models.IntegerField(null=True, blank=True)
    allow_second_time = models.BooleanField(default=False)
    details_info = RichTextField(blank=True, null=True)
    ssc_gpa_multiply = models.DecimalField(max_digits=4,decimal_places=2,null=True,blank=True)
    hsc_gpa_multiply = models.DecimalField(max_digits=4,decimal_places=2,null=True,blank=True)


    def __str__(self):
        return self.name


class versity(models.Model):
    name= models.CharField(max_length=50)
    gpa_table_name = models.CharField(max_length=50,null=True, blank=True)
    ssc_gpa = models.DecimalField(max_digits=3,decimal_places=2,default=0)
    hsc_gpa = models.DecimalField(max_digits=3,decimal_places=2,default=0)
    total_gpa = models.DecimalField(max_digits=4,decimal_places=2,default=0)

    extra_condition = models.TextField(null=True,blank=True)

    total_sit = models.IntegerField(null=True, blank=True)
    application_link = models.CharField(max_length=200,null=True,blank=True)
    
    exam_value = models.IntegerField(null=True, blank=True)
    allow_second_time = models.BooleanField(default=False)
    details_info = RichTextField(blank=True, null=True)
    ssc_gpa_multiply = models.DecimalField(max_digits=4,decimal_places=2,null=True,blank=True)
    hsc_gpa_multiply = models.DecimalField(max_digits=4,decimal_places=2,null=True,blank=True)

    def __str__(self):
        return self.name
        
class unitChange(models.Model):
    name= models.CharField(max_length=50)
    gpa_table_name = models.CharField(max_length=50,null=True, blank=True)
    ssc_gpa = models.DecimalField(max_digits=3,decimal_places=2,default=0)
    hsc_gpa = models.DecimalField(max_digits=3,decimal_places=2,default=0)
    total_gpa = models.DecimalField(max_digits=4,decimal_places=2,default=0)

    total_sit = models.IntegerField(null=True, blank=True)
    exam_value = models.IntegerField(null=True, blank=True)
    allow_second_time = models.BooleanField(default=False)
    details_info = RichTextField(blank=True, null=True)
    ssc_gpa_multiply = models.DecimalField(max_digits=4,decimal_places=2,null=True,blank=True)
    hsc_gpa_multiply = models.DecimalField(max_digits=4,decimal_places=2,null=True,blank=True)

    def __str__(self):
        return self.name

class admissionSystemOverview(models.Model):
    name= models.CharField(max_length=50,null=True,blank=True)
    details = RichTextField(null=True,blank=True)

    def __str__(self):
        return self.name

class admissionDetailsInfo(models.Model):
    name = models.CharField(max_length=30)
    details = RichTextField(null=True, blank=True)


    def __str__(self):
        return self.name

class eligibilityCheckerControl(models.Model):
    on = models.BooleanField(default=False)
    
    def __str__(self):
        return "On/OFF"
    
class AdmissionApplication(models.Model):
    name = models.CharField(max_length=20)
    
    marks = RichTextField(null=True,blank=True)
    negative_marking = models.CharField(max_length=200,null=True,blank=True)
    second_time = models.CharField(max_length=200,null=True,blank=True)
    calculator = models.CharField(max_length=200,null=True,blank=True)
    
    application_start_date = models.DateTimeField(null=True, blank=True)
    application_end_date = models.DateTimeField(null=True, blank=True)
    application_link = models.CharField(max_length=200,null=True, blank=True)
    exam_date_time = models.DateTimeField(null=True, blank=True)
    syllabus = models.CharField(max_length=100,null=True,blank=True)
    fee = models.CharField(max_length=10,null=True,blank=True)
    admit_card_start_date = models.DateTimeField(null=True, blank=True)
    admit_card_end_date = models.DateTimeField(null=True, blank=True)
    admit_card_link = models.CharField(max_length=200,null=True, blank=True)

    result_date = models.DateTimeField(null=True, blank=True)
    result_link = models.CharField(max_length=200,null=True,blank=True)

    class Meta:
        verbose_name = "Admission Time Table"
        verbose_name_plural = "Admission Time Tables"

    def __str__(self):
        return self.name

