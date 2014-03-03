# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 22:28:21 2014

@author: CharlieMouton and JenniferWei

Charlie's fb code: CAAEuAis8fUgBANEcpy6pnuIwr8IZBLFo3MT7N2m2xbgkecbZCps2CTbm3OY
fN9nbLZAS8ZBQaVzqGPMcfP3p4Dma1eH2YRvNGxGLr4xzPuSpZBsYAVi4BMPUp7HTaNkbNddDEZC9Z
Blt5zC3bf9HICmYAJFPZC7mU4zQFHksF1eTRlf9E2RpypFhZBJ3tqkYYCKwZD


"""

from pattern.web import *
f = Facebook(license='CAAEuAis8fUgBANEcpy6pnuIwr8IZBLFo3MT7N2m2xbgkecbZCps2CTbm3OYfN9nbLZAS8ZBQaVzqGPMcfP3p4Dma1eH2YRvNGxGLr4xzPuSpZBsYAVi4BMPUp7HTaNkbNddDEZC9ZBlt5zC3bf9HICmYAJFPZC7mU4zQFHksF1eTRlf9E2RpypFhZBJ3tqkYYCKwZD')
me = f.profile()
print me #prints out information of license (id,name,birthday,gender,country)
counter = 0
textDict = {}
textFreq = {}
my_friends = f.search(me[0], type=FRIENDS, count=1000)


def access_newsfeed(frnd):
    """
    access_newsfeed takes in the information of a friend, accesses their 
    newsfeed, and puts all of it into a dictionary, where the key is the 
    name and the value is the newsfeed text list.
    
    frnd: is the newsfeed information for a specified friend
    
    returns: value (list of newsfeed text) from the textDictionary for that
    specific friend
    """
    textList = []
    friend_news = f.search(frnd.id, type=NEWS, count=100)
    for news in friend_news:
        #print news.text
        #print type(news.author)
        #print news.date
        textList.append(news.text)
    textDict[frnd.author[1]] = textList
    return textDict[frnd.author[1]]
    
    
def cleanup(friend_name,posts):
    """
    Takes the list of posts taken directly from Facebook and removes all 
    automatic Facebook posts like "BLANK and BLANK are now friends."
    
    posts: list of newsfeed text
    friend_name = name of newsfeed owner
    
    returns: modPosts = modified list of newsfeed text
    """
    
    for post in posts:
        print type(post)
        if not(str(post).contains(friend_name)):
            modPosts.append(post)
    return modPosts
    

def facebook_pull(specific_friend):
    """
    facebook_pull pulls the newsfeed information for a specific friend.
    specific_friend: name of specific friend as a string
    
    returns: dictionary of posts from the newsfeed of the specific friend
    """
    
    for friend in my_friends:
        temp_name = friend.author[1]
        #print friend.author[1] #Prints the name of the author of the post
        
        if (temp_name == specific_friend):
            roughDict = access_newsfeed(friend)
            cleanTextDict = cleanup(specific_friend, roughDict)
            return cleanTextDict
        #print friend_news
        #for news in friend_news:
        #    counter += 1
        #    print news.text
        #    print news.author[1]
        #    print type(news.author)
        #    print news.date
        #    print counter


#test for facebook_pull
print facebook_pull("Danielle Mouton")
print facebook_pull("Casey Alvarado")