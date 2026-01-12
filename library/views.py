from rest_framework import viewsets
from .models import Book, Transaction
from .serializers import BookSerializer, TransactionSerializer
from rest_framework.decorators import action #Creates a custom endpoint
from rest_framework.response import Response
from rest_framework import status #HTTP status codes
from django.core.exceptions import ValidationError
from .services import checkout_book

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=True, methods=['post'])
    def checkout(self, request, pk=None):
        book = self.get_object()

        try:
            transaction = checkout_book(request.user, book)
        except ValidationError as e:
            return Response(
                {"error":e.message},
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            {"message":"Book checked out successfully"},
            status= status.HTTP_200_OK
        )

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    
