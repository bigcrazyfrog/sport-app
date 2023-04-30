from django.http import JsonResponse
from ninja import NinjaAPI

from app.internal.services.allergen_service import AllergenService
from app.internal.services.product_service import ProductService

api = NinjaAPI(
    title="SPORT.BACKEND",
    version="1.0.2"
)


@api.get("/status")
def status(request):
    return {"status": "OK"}


@api.get("/products")
def products(request):
    return JsonResponse(ProductService.get_all(), json_dumps_params={'ensure_ascii': False})


@api.get("/products/{id}")
def products(request, id: int):
    return JsonResponse(ProductService.get_by_id(id), json_dumps_params={'ensure_ascii': False})


@api.get("/allergens")
def allergens(request):
    return JsonResponse(AllergenService.get_all(), json_dumps_params={'ensure_ascii': False})


@api.get("/allergens/{id}")
def allergens(request, id: int):
    return JsonResponse(AllergenService.get_by_id(id), json_dumps_params={'ensure_ascii': False})
