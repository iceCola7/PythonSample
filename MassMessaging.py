import itchat
import ybc_box as box

itchat.auto_login(True)

targetChatroom = '您搜索的网页开小差了'
# 获取所有的群聊
# 必须先获取一遍所有的群聊，否则使用search_chatrooms方法时会查询不到
chatroomsList = itchat.get_chatrooms()


# for chatroom in chatroomsList:
#     print(chatroom)
#     print('------------------')


# 查询并更新指定群聊的成员列表
def updateMemberlist(chatroomName):
    chatroomRes = itchat.search_chatrooms(chatroomName)
    if len(chatroomRes) > 0:
        # chatroomMembers = chatroomRes[0]['MemberList']['ContactList']
        # print(chatroomMembers)
        itchat.update_chatroom(chatroomRes[0]['UserName'], detailedMember=True)
    else:
        print('没有找到该群聊:' + chatroomName)


def searchChatroomByName(chatroomName):
    itchat.get_chatrooms()
    updateMemberlist(chatroomName)
    chatroomRes = itchat.search_chatrooms(chatroomName)
    return chatroomRes


# contactList = itchat.get_contact()
# print(contactList)


# chatroomRes = itchat.search_chatrooms(targetChatroom)


# 获取成员列表
# memberList = chatroomRes[0]['MemberList']
# # print(chatroomRes)
# # print(memberList[0]['NickName'])
# for obj in memberList:
#     print(obj['NickName'])
#     # print(obj)


def printNickNameInChatroom(chatroom):
    memberList = chatroom['MemberList']
    print('~~~~~~~~~' + chatroom['NickName'] + '~~共' + str(len(memberList)) + '人，群成员如下~~~~~~~~~~~')
    for obj in memberList:
        print(obj['NickName'])


def getMemberListFromChatroom(chatroom):
    memberList = chatroom['MemberList']
    return memberList


def getChatroomNames():
    chatroomsList = itchat.get_chatrooms()
    print('~~~~~~~~~共' + str(len(chatroomsList)) + '个群，所有的群聊名称如下~~~~~~~~~~~')
    for chatroom in chatroomsList:
        print(chatroom['NickName'])


getChatroomNames()

# 查找指定的群聊
chatroomRes = searchChatroomByName(targetChatroom)
# 打印群成员的名称
printNickNameInChatroom(chatroomRes[0])

# 获取群成员对象列表
memberList = getMemberListFromChatroom(chatroomRes[0])
# print(memberList)
judge = True
while judge:
    msg = box.enterbox('请输入您要发送的消息')
    if msg == 'exit' or msg is None:
        break
    # 给群成员群发消息
    for member in memberList:
        friends = itchat.search_friends(member['NickName'])
        # print(friends[0])
        # print(friends[0]['UserName'])
        itchat.send(msg, friends[0]['UserName'])
        print('--to--' + friends[0]['NickName'] + '--:' + msg + '------')
