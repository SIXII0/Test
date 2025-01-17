from cozepy import Coze, TokenAuth, Message, ChatStatus, MessageContentType, ChatEventType
#从coze引用URL
from cozepy import COZE_CN_BASE_URL
#密钥
coze_api_token = 'pat_xyvCL9CXmPwVhyfxFOfs8555awhNilMG0Dlg0uiFxyeJ7CxwGRA8w7vk1ZEbZVH2'
coze_api_base =COZE_CN_BASE_URL

coze = Coze(auth=TokenAuth(token=coze_api_token), base_url=coze_api_base)

#机器人编号
bot_id = '7419135881967091712'
user_id = '123456'
text=input()

for event in coze.chat.stream(
    bot_id=bot_id,
    user_id=user_id,
    additional_messages=[
        Message.build_user_question_text(text)
    ]
):
    if event.event == ChatEventType.CONVERSATION_MESSAGE_DELTA:
        print(event.message.content, end="", flush=True)
    if event.event == ChatEventType.CONVERSATION_CHAT_COMPLETED:
        print('')
        print("token usage:", event.chat.usage.token_count)