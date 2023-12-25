from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import NFT
from .serializers import NFTSerializer


class NFTView(APIView):
    def get(self, request, *args, **kwargs):
        nfts = NFT.objects.all()
        # list serializer
        serializer = NFTSerializer(nfts, many=True)
        return Response(
            {"status": True, "status_code": 200, "message": "NFT listed successfully", "data": serializer.data},
            status=status.HTTP_200_OK
        )

    def post(self, request, *args, **kwargs):
        payload = request.data
        serializer = NFTSerializer(data=payload)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": True, "status_code": 200, "message": "NFT record is created successfully",
                 "data": serializer.data},
                status=status.HTTP_200_OK
            )
        return Response(
            {"status": False, "status_code": 400, "message": "Something went wrong", "error": serializer.errors,
             "data": []},
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, *args, **kwargs):
        payload = request.data
        id = kwargs.get("id")
        nft_record = NFT.objects.get(pk=id)
        serializer = NFTSerializer(nft_record, data=payload, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": True, "status_code": 200, "message": "NFT record is update dsuccessfully",
                 "data": serializer.data},
                status=status.HTTP_200_OK
            )
        return Response(
            {"status": False, "status_code": 400, "message": "Something went wrong", "error": serializer.errors,
             "data": []},
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, *args, **kwargs):
        id = kwargs.get("id")
        nft_record = NFT.objects.get(pk=id)
        nft_record.delete()
        return Response(
            {"status": True, "status_code": 200, "message": "Record deleted successfully", "data": []},
            status=status.HTTP_200_OK
        )
