from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import ChatService
from .serializers import ChatRoomSerializer, MessageSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@api_view(['POST'])
@csrf_exempt
def create_chatroom(request):
    try:
        name = request.data['name']
        max_members = request.data['max_members']

    except KeyError as e:
        return Response({'error': f"Missing required parameter: {e}"}, status=400)

    try:
        chatroom = ChatService.create_chatroom(name, max_members)
        serializer = ChatRoomSerializer(chatroom)

        return Response(serializer.data)

    except ValueError as e:
        return Response({'error': str(e)}, status=400)


@api_view(['GET'])
def list_chatrooms(request):
    chatrooms = ChatService.list_chatrooms()
    serializer = ChatRoomSerializer(chatrooms, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@csrf_exempt
def leave_chatroom(request):
    user_id = request.data.get('user_id')
    chatroom_id = request.data.get('chatroom_id')

    try:
        ChatService.leave_chatroom(user_id, chatroom_id)
        return JsonResponse({'message': 'Left chatroom successfully.'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@api_view(['POST'])
@csrf_exempt
def enter_chatroom(request):
    user_id = request.data.get('user_id')
    chatroom_id = request.data.get('chatroom_id')

    try:
        ChatService.enter_chatroom(user_id, chatroom_id)
        return JsonResponse({'message': 'Entered chatroom successfully.'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@api_view(['POST'])
@csrf_exempt
def send_message(request):
    user_id = request.data.get('user_id')
    chatroom_id = request.data.get('chatroom_id')
    content = request.data.get('content')

    try:
        message = ChatService.send_message(user_id, chatroom_id, content)
        serializer = MessageSerializer(message)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=400)


@api_view(['GET'])
def list_messages(request, chatroom_id):
    messages = ChatService.list_messages(chatroom_id)
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)
