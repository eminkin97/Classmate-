from django.conf.urls import url

from .views import *

urlpatterns = [
	url(r'^auth/$', auth, name="authentication"),
	url(r'^classes/$', getAllClasses, name="class_list"),
	url(r'^user_classes/$', getUserClasses, name="class_list_for_user"),
	url(r'^add_user_class/$', addClassForUser, name="add_class_for_user"),
	url(r'^delete_user_class/$', deleteClassForUser, name="delete_class_for_user"),
	url(r'^messages/$', getMessages, name="message_list"),
	url(r'^sendmsg/$', addMessage, name="add_message"),
	url(r'^like/$', sendLike, name="send_like"),
]
