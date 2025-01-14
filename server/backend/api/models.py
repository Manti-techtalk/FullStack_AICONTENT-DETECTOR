from django.db import models

# Create your models here.
class User(models.Model):
    user_name  = models.CharField(max_length=50, unique=True, null=False)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    gmail = models.EmailField(null=False, max_length=50, unique=True)
    password = models.CharField(null=False, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name

class TextSubmission(models.Model):
    content = models.TextField(max_length=100000, null=False)
    submission_date = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed'),
        ('Cancelled', 'Cancelled'),
    ]
    analysis_status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='Pending')
    results = models.CharField(max_length=225, blank=True)
    confidence_score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.content
    
class Analysis(models.Model):
    submission = models.OneToOneField(TextSubmission, on_delete=models.CASCADE)
    word_count  = models.PositiveIntegerField()
    ai_probability = models.DecimalField(decimal_places=2, max_digits=5)
    human_probability = models.DecimalField(decimal_places=2, max_digits=5)
    processing_time = models.DurationField()
    detected_patterns = models.TextField(null=True)

    def __str__(self):
        return str(self.submission)

class AiModelData(models.Model):
    model_name = models.CharField(max_length=225)
    version = models.CharField(max_length=50)
    accuracy = models.DecimalField(decimal_places=2, max_digits=5)
    last_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.model_name
