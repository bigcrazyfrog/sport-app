from django.http import JsonResponse
from ninja import NinjaAPI

from app.internal.services.allergen_service import AllergenService
from app.internal.services.product_service import ProductService

api = NinjaAPI()


@api.get("/status")
def status(request):
    return {"status": "OK"}


@api.get("/product")
def product(request):
    return JsonResponse(ProductService.get_all(), json_dumps_params={'ensure_ascii': False})


@api.get("/product/{id}")
def product(request, id: int):
    return JsonResponse(ProductService.get_by_id(id), json_dumps_params={'ensure_ascii': False})


@api.get("/allergen")
def allergen(request):
    return JsonResponse(AllergenService.get_all(), json_dumps_params={'ensure_ascii': False})


@api.get("/allergen/{id}")
def allergen(request, id: int):
    return JsonResponse(AllergenService.get_by_id(id), json_dumps_params={'ensure_ascii': False})
