class User:
    # Define the fields and methods for your object here.
    def __init__(self, newUsername, newUserID):
        self.username = newUsername
        self.userID = newUserID
        self.Friends = []

    def getUserName(self):
        return self.username

    def getUserID(self):
        return self.userID

    def getFriends(self):
        return self.Friends

    def addFriends(self, FriendID):
        self.Friends.append(FriendID)

class Network:

    def __init__(self):
        self.users=[]

    def numUsers(self):
        return len(self.users)

    def addUser(self, username):
        user_id=len (self.users)
        self.users.append(User(username,user_id))

    def getUserID(self, username):
        for user in self.users:
            if username==user.getUserName():
                user_id=user.getUserID()
        return user_id


    def addConnection(self,user1,user2):
        user1_id=self.getUserID(user1)
        user2_id=self.getUserID(user2)

        user1=self.users[user1_id]
        user2=self.users[user2_id]

        self.users[user2_id].addFriends(user1_id)
        self.users[user1_id].addFriends(user2_id)


    def printUsers(self):
        print("This is the Network")
        for user in self.users:
            print("\tUser {}: {}".format(user.getID, user.getUserName))

    def printConnections(self, username):
        user_b=self.users[self.getUserID(username)]
        connections=user_b.getFriends()
        print("\t{}'s connections:".format(user_b.getUserName()))
        for FriendID in connections:
            friend=self.users[FriendID]
            print("\t{}:".format(friend.getUserName()))


    # Define the fields and methods for your object here.
def main():
    mynetwork=Network()
    done=False
    while not done:
        action=input("\nWhat would you like to do ? Add a user(u), Add a Connection (c), Print Users(p), Print Connections(pc) Exit(e)")

        if action=="u":
            username=input("What username?")
            mynetwork.addUser(username)

        elif action=="c":
            if mynetwork.numUsers()<2:
                print("ERROR.Don't have enough users.")
                continue
            else:
                user1=input("First User?")
                user2=input("Second User?")
            mynetwork.addConnection(user1, user2)
        elif action=="p":
            mynetwork.printUsers()

        elif action=="pc":
            user_a=input("What user?")
            mynetwork.printConnections(user_a)
        elif action=="e":
            print("Sorry to see you go")
            done=True
        else:
            print("Your dumb. Pay attention :|")


# Runs your program.
if __name__ == '__main__':
    main()
