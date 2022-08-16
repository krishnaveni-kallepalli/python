class instagram:
    def __init__(self,followers,following,unfollow,accept,follow):
        self.followers = followers
        self.following = following
        self.unfollow = unfollow
        self.accept = accept
        self.follow = follow
        return
    def op(self):
        print("Followers : ",self.followers)
        print("Following : ",self.following)
   # def unfollow(self):
        #print("Enter how many people to be unfollow : ",self.unfollow)
        print("unfollowing ",self.unfollow,"members")
        if(following <= 0 and following < unfollow):
            print("Cannot unfollow")
        else:
            self.following = self.following-self.unfollow
            print("Following : ",self.following)
      #  return
   # def accept(self):
        print("Accepting ",self.accept,"friend requests")
        self.following = self.following+self.accept
        print("Following : ",self.following)
       # return
   # def follow(self):
        print("Followiing ",self.follow,"members")
        self.followers = self.followers+self.follow
        print("Followers : ",self.followers)
        return
    

followers = int(input("Enter no.of followers : "))
following = int(input("Enter no.of followings : "))
unfollow = int(input("Enter no.of people to unfollow : "))
accept = int(input("Enter request accepted count : "))
follow = int(input("Enter no.of people to follow : "))
acc = instagram(followers,following,unfollow,accept,follow)
op1= instagram(followers,following,unfollow,accept,follow)
op1.op()
'''
op2 = instagram(followers,following,unfollow,accept,follow)
op2.unfollow()
op3 = instagram(followers,following,unfollow,accept,follow)
op3.accept()
op4 = instagram(followers,following,unfollow,accept,follow)
op4.follow()




'''
