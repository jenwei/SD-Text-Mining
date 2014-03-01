# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 22:28:21 2014

@author: charliemouton and Jenniferwei

Charlie's fb code: CAAEuAis8fUgBANEcpy6pnuIwr8IZBLFo3MT7N2m2xbgkecbZCps2CTbm3OY
fN9nbLZAS8ZBQaVzqGPMcfP3p4Dma1eH2YRvNGxGLr4xzPuSpZBsYAVi4BMPUp7HTaNkbNddDEZC9Z
Blt5zC3bf9HICmYAJFPZC7mU4zQFHksF1eTRlf9E2RpypFhZBJ3tqkYYCKwZD


"""

from pattern.web import *
f = Facebook(license='CAAEuAis8fUgBANEcpy6pnuIwr8IZBLFo3MT7N2m2xbgkecbZCps2CTbm3OYfN9nbLZAS8ZBQaVzqGPMcfP3p4Dma1eH2YRvNGxGLr4xzPuSpZBsYAVi4BMPUp7HTaNkbNddDEZC9ZBlt5zC3bf9HICmYAJFPZC7mU4zQFHksF1eTRlf9E2RpypFhZBJ3tqkYYCKwZD')
me = f.profile()
print me
counter = 0
my_friends = f.search(me[0], type=FRIENDS, count=10000)
for friend in my_friends:
    friend_news = f.search(friend.id, type=NEWS, count=100)
    for news in friend_news:
        counter += 1
        print news.text
        print news.author
        print news.date
        print counter
            