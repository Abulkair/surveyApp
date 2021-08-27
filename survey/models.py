from django.db import models


class Survey(models.Model):
    # title = models.CharField(max_length=150)
    # description = models.CharField(max_length=300, blank=True)
    # date = models.DateTimeField(auto_now_add=True)
    # done = models.BooleanField(default=False)

    survey_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    end_date = models.DateTimeField()
    survey_description = models.CharField(max_length=200)

    def __str__(self):
        # return self.title
        return self.survey_name

