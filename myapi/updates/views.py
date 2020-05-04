from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponse
from django.views.generic import View
from myapi.mixins import JsonResponseMixin
from .models import Update
from django.core.serializers import serialize
# Create your views here.
#def detail_view(request):
# 	return render(request, template, {})
#	return HttpResponse(get_template().render({}))

def json_example_view(request):
	'''
	URI - uniform resource identifier
	'''
	data = {
		"count": 1000,
		"content": "Some new content"
	}
	json_data = json.dumps(data)
	#return JsonResponse(data)
	return HttpResponse(json_data, content_type="application/json")

class JsonCBV(View):
	def get(self, request, *args, **kwargs):
		data = {
		"count": 1000,
		"content": "Some new content"
		}
		return JsonResponse(data)



class JsonCBV2(JsonResponseMixin, View):
	def get(self, request, *args, **kwargs):
		data = {
		"count": 1000,
		"content": "Some new content"
		}
		return self.render_to_json_response(data, content_type="application/json")


class SerializedDetailView(View):
	def get(self, request, *args, **kwargs):
		obj = Update.objects.get(id=5)
		#data = serialize("json", [obj,], fields=('user', 'content'))
		# data = {
		# "user": obj.user.username,
		# "content": obj.content
		# }
		# json_data = json.dumps(data)
		json_data = obj.serialize()
		return HttpResponse(json_data, content_type="application/json")

class SerializedListView(View):
	def get(self, request, *args, **kwargs):
		qs = Update.objects.all()
		#data = serialize("json", qs, fields=('user', 'content'))
		# data = {
		# "user": obj.user.username,
		# "content": obj.content
		# }
		#json_data = json.dumps(data)
		json_data = Update.objects.all().serialize()
		return HttpResponse(json_data, content_type="application/json")
