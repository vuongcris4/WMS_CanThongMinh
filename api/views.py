from django.utils import timezone
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import generics, status
import pytz

from material_app.models import MaterialTransactions, Material
from .serializers import MaterialTransactionsSerializer, MaterialTransactionsCreateSerializer

from .utils import xoa_dau

@api_view(['GET', 'POST'])
def material_transactions(request):
    if request.method == 'GET':
        transactions = MaterialTransactions.objects.all()
        serializer = MaterialTransactionsSerializer(transactions, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        # serializer = MaterialTransactionsCreateSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer = MaterialTransactionsCreateSerializer(data=request.data)
        if serializer.is_valid():
            transaction = serializer.save()
            transaction_type = "Nhập" if transaction.transaction_type == "import" else "Xuất"

            base_quantity = transaction.base_quantity
            base_quantity = "{:.1f}".format(base_quantity)
            material_name = transaction.materialId.name
            base_unit = transaction.materialId.base_unitId.name

            quantity = transaction.quantity
            unit = transaction.unitId.name

            tz = pytz.timezone('Asia/Ho_Chi_Minh')
            created_at_local = timezone.localtime(transaction.created_at, tz)
            created_at = created_at_local.strftime("%H:%M %d/%m/%Y")

            inventory_level = transaction.materialId.inventory_level
            inventory_level = "{:.1f}".format(inventory_level)

            LEN_WIDTH_LCD = 19
            message1 = xoa_dau(f"{transaction_type} '{material_name}'").ljust(LEN_WIDTH_LCD," ")
            message2 = xoa_dau(f"{quantity}{unit} {base_quantity} {base_unit}").ljust(LEN_WIDTH_LCD," ")
            message3 = f"{created_at}".ljust(LEN_WIDTH_LCD," ")
            message4 = xoa_dau(f"Ton: {inventory_level} {base_unit}").ljust(LEN_WIDTH_LCD," ")
            message = message1 + "\n" + message2 + "\n" + message3 + "\n" + message4 + "\n"
            return Response({"message": message}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_name_from_id(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        if id:
            try:
                material = Material.objects.get(id=id)
                # name_material = xoa_dau(material.name).ljust(19," ")
                name_material = xoa_dau(material.name).ljust(19," ")
                return Response({"name": name_material}, status=status.HTTP_200_OK)
            except:
                return Response({"name": "NOT_FOUND".ljust(19," ")}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)