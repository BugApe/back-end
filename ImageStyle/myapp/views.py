from django.shortcuts import render

# Create your views here.

from rest_framework import  mixins,viewsets
from myapp.models import StyleImage
from myapp.serializers import ImageSerializers

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response



# Create your views here.



class ImageViewSet(viewsets.ModelViewSet):
    # 指定结果集并设置排序
    queryset = StyleImage.objects.all().order_by('name')
    # 指定序列化的类
    serializer_class = ImageSerializers

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)  # 对上传的图片序列化
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({
            "status": status.HTTP_200_OK,
            "message": 'Working right.',
            "tag": 'pass',
            #"data": serializer2.data
        }
        )  # 返回worker中匹配的图片地址





