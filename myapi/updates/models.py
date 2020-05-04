from django.conf import settings
from django.db import models
from django.core.serializers import serialize
import json

# Create your models here.
def upload_update_image(instance, filename):
	return "updates/{user}/{filename}".format(user=instance.user,filename=filename)

class UpdateQuerySet(models.QuerySet):
	def serialize(self):
		list_values = list(self.values("user", "content", "image", "id"))
		#qs = self
		# final_array = []
		# for obj in qs:
		# 	struct = json.loads(obj.serialize())
		# 	final_array.append(struct)
		#return serialize("json", qs, fields=('user', 'content', 'image'))
		#return json.dumps(final_array)
		return json.dumps(list_values)

class UpdateManager(models.Manager):
	def get_queryset(self):
		return UpdateQuerySet(self.model, using=self._db)

class Update(models.Model):
	user 		= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
	content 	= models.TextField(blank=True, null=True)
	image 		= models.ImageField(upload_to=upload_update_image, blank=True, null=True)
	updated 	= models.DateTimeField(auto_now=True)
	timestamp 	= models.DateTimeField(auto_now_add=True)

	objects = UpdateManager()

	def __str__(self):
		return self.content or ""

	def serialize(self):
		#json_data = serialize("json", [self], fields=('user', 'content', 'image', 'id'))
		try:
			image = self.image_url
		except:
			image = ""
		data = {
			"id": self.id,
			"user": self.user.id,
			"content": self.content,
			"image": image
		}
		# struct = json.loads(json_data)
		# print(struct)
		# data = json.dumps(struct[0]['fields'])
		data = json.dumps(data)
		return data
		#return serialize("json", [self], fields=('user', 'content', 'image'))

'''
Keep your command prompt/ terminal running
In case you've missed out on anything, let us know in the chat section
'''