from django.db import models

# Create your models here.

class Service(models.Model):
	SUCCESS= 'S'
	ERROR = 'E'
	CRAWLING = 'C'
	STATUS = (
		(SUCCESS,'Success'),
		(ERROR,'Error'),
		(CRAWLING,'Crawling')
		)
	name = models.CharField(max_length=255)
	slug = models.SlugField(max_length=50,unique=True)
	url = models.URLField()
	story_url = models.URLField()
	last_run = models.DateTimeField(null=True,blank=True)
	status = models.CharField(max_length=10,default=SUCCESS,choices=STATUS)

	class Meta:
		verbose_name='service'
		verbose_name_plural='services'
		ordering = ('name',)


	def __str__(self):
		return self.name

	def to_dict(self):
		return {
			'name':self.name,
			'slug':self.slug,
			'url':self.url

		}

