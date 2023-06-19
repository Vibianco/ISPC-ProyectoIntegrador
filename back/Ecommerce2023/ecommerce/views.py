from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login, logout
from rest_framework import status, generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import UserSerializer, ProvinciaSerializer, Numeros_RifasSerializer, VentaSerializer, Medio_PagoSerializer, FacturaSerializer, RifaSerializer
from .models import Provincia, Numeros_Rifas, Venta, Medio_Pago, Factura, Rifa, CustomUser
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
#import mercadopago
#import json

#Clases referidas al usuario
class SigupView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

class LoginView(APIView):
    permission_classes = [AllowAny] 
    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        user = authenticate(username=username, password=password)
        token,_=Token.objects.get_or_create(user=user)
        if token:
            login(request, user)
            return Response({
                'token': token.key
            },
                status=status.HTTP_200_OK
            )
        return Response(
            status=status.HTTP_404_NOT_FOUND
        )

class LogoutView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        request.user.auth_token.delete()
        logout(request)
        return Response(
            status=status.HTTP_200_OK
        )

class UserViewSet(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset=CustomUser.objects.all()
    serializer_class= UserSerializer

class UpdateUser(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    lookup_field = 'username'

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

class DeleteUser(generics.DestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class= UserSerializer
    queryset = CustomUser.objects.all()
    lookup_field = 'username'

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    
#Clases referidas a las rifas

class AddRifa(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = RifaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

class ListRifa(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset=Rifa.objects.all()
    serializer_class= RifaSerializer

class DeleteRifa(generics.DestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset=Rifa.objects.all()
    serializer_class= RifaSerializer
    lookup_field = 'id_rifa'
    
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    
class UpdateRifa(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = RifaSerializer
    queryset = Rifa.objects.all()
    lookup_field = 'id_rifa'

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

class ListRifaFilter(generics.RetrieveAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = RifaSerializer
    queryset = Rifa.objects.all()
    lookup_field = "nombre_sorteo"
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


# Clases referidas al carrito

class ListCarrito(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

class AddCarrito(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format = None):
        serializer = VentaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,status=status.HTTP_400_BAD_REQUEST
        )

class DeleteCarrito(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
    lookup_field = 'id_venta'

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class UpdateCarrito(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = VentaSerializer
    queryset = Venta.objects.all()
    lookup_field = 'titulo_rifa'

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

class ListCarritoFilter(generics.RetrieveAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = VentaSerializer
    queryset = Venta.objects.all()
    lookup_field = 'titulo_rifa'
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

# Clases referidas a la pasarela de pagos (MercadoPago)

# #class ProcessPaymentAPIView(APIView):
#     def post(self, request):
#         try:
#             request_values = json.loads(request.body)
#             payment_data = {
#                 "transaction_amount": float(request_values["transaction_amount"]),
#                 "token": request_values["token"],
#                 "installments": int(request_values["installments"]),
#                 "payment_method_id": request_values["payment_method_id"],
#                 "issuer_id": request_values["issuer_id"],
#                 "payer": {
#                     "email": request_values["payer"]["email"],
#                     "identification": {
#                         "type": request_values["payer"]["identification"]["type"],
#                         "number": request_values["payer"]["identification"]["number"],
#                     },
#                 },
#             }

#             #sdk = mercadopago.SDK("")

#             #payment_response = sdk.payment().create(payment_data)

#             payment = payment_response["response"]
#             status = {
#                 "id": payment["id"],
#                 "status": payment["status"],
#                 "status_detail": payment["status_detail"],
#             }

#             return Response(data={"body": status, "statusCode": payment_response["status"]}, status=201)
#         except Exception as e:
#             return Response(data={"body": payment_response}, status=400)

# class retornarPagado(APIView):   
#     def get(self, request):
#         return Response({"respuesta": "aprobado"})
    
#Return Custom json, reduzca el stock segun lo enviado.
# class customjsonybajarstock(APIView):
#     permission_classes = [IsAdminUser] 
#     def patch(self, request, pk, cantidad): 
#         model = get_object_or_404(Rifa, pk=pk)  
#         data = {"cantidad": model.cantidad - int(cantidad)} 
#         serializer = RifaSerializer(model, data=data, partial=True) 

#         if serializer.is_valid(): 
#             serializer.save() 
#             agregarcustomjson={"respuesta": "aprobado"}
#             agregarcustomjson.update(serializer.data)  
#             return Response(agregarcustomjson)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

class RifaViewSet(viewsets.ModelViewSet):
    queryset = Rifa.objects.all()
    serializer_class = RifaSerializer

class ProvinciaViewSet(viewsets.ModelViewSet):
 queryset=Provincia.objects.all()
 serializer_class= ProvinciaSerializer

class Numeros_RifasViewSet(viewsets.ModelViewSet):
 queryset=Numeros_Rifas.objects.all()
 serializer_class= Numeros_RifasSerializer

class VentaViewSet(viewsets.ModelViewSet):
 queryset=Venta.objects.all()
 serializer_class= VentaSerializer

class Medio_PagoViewSet(viewsets.ModelViewSet):
 queryset=Medio_Pago.objects.all()
 serializer_class= Medio_PagoSerializer