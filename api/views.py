from django.http import Http404
import json
from api.models import Sale
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import stripe

from api.models import Category, Product
from api.serializers import CategorySerializer, ProductSerializer

class CategoryList(APIView):
    '''Get all categories or create a category'''
    @csrf_exempt
    def get(self, request, format=None):
        cats = Category.objects.all()
        if request.query_params.get('title'):
            cats = cats.filter(title__contains=request.query_params.get('title'))
        serializer = CategorySerializer(cats, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetail(APIView):
    '''Work with an individual Category object'''
    @csrf_exempt
    def get(self, request, pk, format=None):
        cat = Category.objects.get(id=pk)
        serializer = CategorySerializer(cat)
        return Response(serializer.data)

    @csrf_exempt
    def put(self, request, pk, format=None):
        cat = Category.objects.get(id=pk)
        serializer = CategorySerializer(cat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @csrf_exempt
    def delete(self, request, pk, format=None):
        cat = Category.objects.get(id=pk)
        cat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class ProductList(APIView):
    '''Get all categories or create a category'''
    @csrf_exempt
    def get(self, request, format=None):
        prods = Product.objects.all()
        if request.query_params.get('id'):
            prods = prods.filter(
                id__contains=request.query_params.get('id')
                )
        elif request.query_params.get('category'):
            cats = Category.objects.all()
            cats = cats.filter(
                title__contains=request.query_params.get('category')
                )
            prods = prods.filter(
                category__in = cats
                )
        elif request.query_params.get('filename'):
            prods = prods.filter(
                filename__contains=request.query_params.get('filename')
                )
        elif request.query_params.get('name'):
            prods = prods.filter(
                name__contains=request.query_params.get('name')
                )
        elif request.query_params.get('description'):
            prods = prods.filter(
                description__contains=request.query_params.get('description')
                )
        elif request.query_params.get('price'):
            prods = prods.filter(
                price__contains=request.query_params.get('price')
                )
        serializer = ProductSerializer(prods, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetail(APIView):
    '''Work with an individual Category object'''
    @csrf_exempt
    def get(self, request, pk, format=None):
        prod = Product.objects.get(id=pk)
        serializer = ProductSerializer(prod)
        return Response(serializer.data)

    @csrf_exempt
    def put(self, request, pk, format=None):
        prod = Product.objects.get(id=pk)
        serializer = ProductSerializer(prod, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @csrf_exempt
    def delete(self, request, pk, format=None):
        prod = Product.objects.get(id=pk)
        prod.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

################# Sales
class CreateSale(APIView):
    # Creates a sale, including gettign a payment intent from Stripe
    @csrf_exempt
    def post(self, request, format=None):
        body = json.loads(request.body) 
        print(body)
        sale = Sale() #create a sales object import at top create model and migrate

        sale.name = body['name']
        sale.address1 = body['address1']
        sale.address2 = body['address2']
        sale.city = body['city']
        sale.state = body['state']
        sale.zipcode = body['zipcode'] 
        sale.total = body['total']
        sale.items = body['items']
        sale.payment_intent = stripe.PaymentIntent.create(
            amount=int(int(sale.total) * 100), 
            currency = 'usd'
        )
        ... #set the field values
        sale.save()

        return Response({
        'sale_id': sale.id,
        'client_secret': sale.payment_intent['client_secret'],
        'payment_intent': sale.payment_intent
        })

       
        # Validation and submit method in checkout-starter
        # Make migrations
        # Migrate

        # Done
        # serializer
        # views.py
        # fields.py
        # models.py
        # urls.py entry
