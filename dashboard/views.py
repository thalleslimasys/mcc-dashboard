from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from arches.app.models.models import ResourceInstance, TileModel
from django.http import JsonResponse
from .models import Record

@method_decorator(csrf_exempt, name="dispatch")
class Dashboard(View):

    def serialize_system_records(self):
        res = [{
            "resources": v["state_details"]["resources"],
            "tiles": v["state_details"]["tiles"],
            "statetime": v["state_time"].strftime("%m/%d/%Y, %H:%M:%S")
        } for v in Record.objects.all().values()]
        return res

    def get(self, request):
        data = {
            "records": self.serialize_system_records(),
            "resource_count": ResourceInstance.objects.count(),
            "tile_count": TileModel.objects.count(),
        }
        return JsonResponse(data)

    def post(self, request):
        state = {
            "resources": ResourceInstance.objects.count(),
            "tiles": TileModel.objects.count()
        }
        record = Record()
        record.state_details = state
        record.save()
        data = {"records": self.serialize_system_records()}
        return JsonResponse(data)
