from django.db import models
from .services import Service

class Story(models.Model):
	TEXT = 'T'
	URL = 'U'
	IMAGE = 'I'

	CONTENT_TYPES=(
        (TEXT,'text'),
        (URL,'url'),
        (IMAGE,'image')
		)

	NEW = 'N'
	OK = 'O'
	ERROR = 'E'

	STATUS = (
		(NEW,'new'),
		(OK,'ok'),
		(ERROR,'error')
		)

	service = models.ForeignKey(Service,related_name='stories',on_delete=models.CASCADE)
	code = models.CharField(max_length=255)
	title = models.CharField(max_length=500, null=True, blank=True)
	url = models.URLField(max_length=2000, null=True, blank=True)
	content = models.TextField(null=True, blank=True)
	content_type = models.CharField(max_length=1, choices=CONTENT_TYPES, null=True, blank=True)
	start_comments = models.IntegerField(default=0)
	comments = models.IntegerField(default=0)
	start_score = models.IntegerField(default=0)
	score = models.IntegerField(default=0)
	date = models.DateField(auto_now_add=True, db_index=True)
	status = models.CharField(max_length=1, default=NEW, choices=STATUS)
	top_ten = models.BooleanField(default=False)
	nsfw = models.BooleanField(default=False)
	description = models.CharField(max_length=2000, null=True, blank=True)

	class Meta:
		verbose_name='story'
		verbose_name_plural = 'stories'
		unique_together = (('service','code','date'),)
		ordering = ('-score',)


	def __str__(self):
		return self.code


	def to_dict(self):
		return {
		    'code': self.code,
	    'title': self.title,
	    'url': self.url,
	    'comments': self.comments,
	    'score': self.score,
	    'description': self.description
	    }