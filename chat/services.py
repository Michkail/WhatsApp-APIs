from django.core.exceptions import ObjectDoesNotExist
from .models import ChatRoom, Message


class ChatService:
    @staticmethod
    def create_chatroom(name, max_members):
        if not name or not max_members:
            raise ValueError("Name and max_members are required fields.")

        chatroom = ChatRoom.objects.create(name=name, max_members=max_members)
        return chatroom

    @staticmethod
    def list_chatrooms():
        return ChatRoom.objects.all()

    @staticmethod
    def leave_chatroom(user_id, chatroom_id):
        try:
            chatroom = ChatRoom.objects.get(id=chatroom_id)
            chatroom.members.remove(user_id)

        except ObjectDoesNotExist:
            raise ValueError("Chatroom not found.")

        except Exception as e:
            raise ValueError(str(e))

    @staticmethod
    def enter_chatroom(user_id, chatroom_id):
        try:
            chatroom = ChatRoom.objects.get(id=chatroom_id)

            if chatroom.members.count() < chatroom.max_members:
                chatroom.members.add(user_id)

            else:
                raise ValueError("Chatroom is full.")

        except ObjectDoesNotExist:
            raise ValueError("Chatroom not found.")

        except Exception as e:
            raise ValueError(str(e))

    @staticmethod
    def send_message(user_id, chatroom_id, content):
        try:
            chatroom = ChatRoom.objects.get(id=chatroom_id)

            if user_id not in chatroom.members.all():
                raise ValueError("User is not a member of this chatroom.")

            message = Message.objects.create(
                chat_room=chatroom,
                sender_id=user_id,
                content=content
            )

            return message

        except ObjectDoesNotExist:
            raise ValueError("Chatroom not found.")

        except Exception as e:
            raise ValueError(str(e))

    @staticmethod
    def list_messages(chatroom_id):
        return Message.objects.filter(chat_room_id=chatroom_id)
