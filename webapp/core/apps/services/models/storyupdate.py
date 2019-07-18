from django.db import models
from .story import Story

class StoryUpdate(models.Model):
	story = models.ForeignKey(Story,related_name='updates',on_delete=models.CASCADE)
	comments_changes = models.IntegerField(default=0)
	score_changes = models.IntegerField(default=0)
	updated_at = models.DateTimeField(auto_now_add=True)


	class Meta:
		db_table = 'services_story_update'
		verbose_name='story update'
		verbose_name_plural='stories update'

	def __str__(self):
		return self.story.code


