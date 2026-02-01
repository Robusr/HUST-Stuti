"""
Robusr 2026.2.1
收藏书籍视图组件
"""
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView

from stuti_app.wants.models import Wants
from stuti_app.wants.serializers import WantsSerializer
from utils import ResponseMessage


class WantsAPIView(APIView):
    """ 基于APIView的收藏图书视图组件"""
     # @todo 后续补充登录权限验证

    def post(self, request):
        request_data = request.data
        # print(request_data)
        # print(type(request_data))

        username = request.data.get('username')
        print(username)
        sku_id = request_data.get('sku_id')
        nums = request_data.get('nums')
        is_deleted = request_data.get('is_deleted')

        #判断数据是否存在
        #不存在==>删除
        data_exists = Wants.objects.filter(
            username=username,
            is_deleted=False,
            sku_id=sku_id
        )
        # 存在==>更新
        if data_exists.exists():
            exists_wants_data = data_exists.get(
                username = username,
                is_deleted=False,
                sku_id=sku_id
            )
            if is_deleted == 0:
                new_nums = nums + exists_wants_data.nums
                request_data['nums'] = new_nums
            elif is_deleted == 1:
                request_data['nums'] = exists_wants_data.nums

            #反序列化
            wants_ser = WantsSerializer(data=request_data)
            # 调用数据验证
            wants_ser.is_valid(raise_exception=True)

            # 更新数据
            Wants.objects.filter(
                username=username,
                is_deleted=False,
                sku_id=sku_id
            ).update(**wants_ser.data)
            if is_deleted == 0:
                return ResponseMessage.WantsResponse.success("UPDATED!")
            elif is_deleted == 1:
                return ResponseMessage.WantsResponse.success("DELETED!")
            # return HttpResponse("UPDATED!")
        else:
            # 数据插入
            wants_ser = WantsSerializer(data=request_data)
            # 调用数据验证
            wants_ser.is_valid(raise_exception=True)
            Wants.objects.create(**wants_ser.data)
            return ResponseMessage.WantsResponse.success("CREATED!")
            # return HttpResponse("CREATED!")

        return HttpResponse("WantsAPIView POST")

    def get(self,request):
        username = request.GET.get('username')
        wants_result = Wants.objects.filter(
            username=username,
            # 校验是否删除
            is_deleted=False
        )
        wants_ser = WantsSerializer(
            instance = wants_result,
            many=True
        )

        # return JsonResponse(
        #     wants_ser.data,
        #     safe=False
        # )

        return ResponseMessage.WantsResponse.success(wants_ser.data)
