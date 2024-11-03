# events/views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import TransferEvent
from .serializers import TransferEventSerializer

@api_view(['GET'])
def transfer_history(request, token_id):
    try:
        token_id_int = int(token_id)
        events = TransferEvent.objects.filter(token_id=token_id_int)

        if not events.exists():
            return Response({'message': 'No transfer events found for this token ID.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TransferEventSerializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except ValueError:
        return Response({'error': 'Invalid token ID format.'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)