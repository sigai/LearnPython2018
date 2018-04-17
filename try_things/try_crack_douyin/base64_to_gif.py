#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = "Sigai"

import os,base64

s = """R0lGODlheAAeAIcAAAAAAAAARAAAiAAAzABEAABERABEiABEzACIAACIRACIiACIzADMAADMRADMiADMzADd3REREQAAVQAAmQAA3QBVAABVVQBMmQBJ3QCZAACZTACZmQCT3QDdAADdSQDdkwDungDu7iIiIgAAZgAAqgAA7gBmAABmZgBVqgBP7gCqAACqVQCqqgCe7gDuAADuTwD/VQD/qgD//zMzMwAAdwAAuwAA/wB3AAB3dwBduwBV/wC7AAC7XQC7uwCq/wD/AEQAREQAiEQAzEREAEREREREiEREzESIAESIRESIiESIzETMAETMRETMiETMzEQAAFUAAFUAVUwAmUkA3VVVAFVVVUxMmUlJ3UyZAEyZTEyZmUmT3UndAEndSUndk0nd3U/u7mYAAGYAZlUAqk8A7mZmAGZmZlVVqk9P7lWqAFWqVVWqqk+e7k/uAE/uT0/unlX/qlX//3cAAHcAd10Au1UA/3d3AHd3d11du1VV/127AF27XV27u1Wq/1X/AFX/VYgAiIgAzIhEAIhERIhEiIhEzIiIAIiIRIiIiIiIzIjMAIjMRIjMiIjMzIgAAIgARJkATJkAmZMA3ZlMAJlMTJlMmZNJ3ZmZAJmZTJmZmZOT3ZPdAJPdSZPdk5Pd3ZkAAKoAAKoAVaoAqp4A7qpVAKpVVapVqp5P7qqqAKqqVaqqqp6e7p7uAJ7uT57unp7u7qr//7sAALsAXbsAu6oA/7tdALtdXbtdu6pV/7u7ALu7Xbu7u6qq/6r/AKr/Var/qswAzMxEAMxERMxEiMxEzMyIAMyIRMyIiMyIzMzMAMzMRMzMiMzMzMwAAMwARMwAiN0Ak90A3d1JAN1JSd1Jk91J3d2TAN2TSd2Tk92T3d3dAN3dSd3dk93d3d0AAN0ASe4AT+4Anu4A7u5PAO5PT+5Pnu5P7u6eAO6eT+6enu6e7u7uAO7uT+7unu7u7u4AAP8AAP8AVf8Aqv8A//9VAP9VVf9Vqv9V//+qAP+qVf+qqv+q////AP//Vf//qv///ywAAAAAeAAeAAAI//8EDiRY0OBBhAkVLmTYsKENhxElTqRYsaINjBYLQtTY0ePHfxw9YhQJ0uRJlAlLpmTZ0uVLmDFlzqzIi1e3bu7c0fxow123mzwRosmTZ9Uqmzh3CmWoUyBEG0VXMiUKdFXRoppWMV3I6ypJsHm6cR14tShSXv+6GSWLkFfRt2n/eXUHNiPXn2/RIM0jF6U7m0sjek3rdRVgtHk62vS7GI27vh8BZwUqtbFDpALjutPEC7JEwHqjFv0Y961gjZyNrkaaeeIqTYAr89JaV2LWm2A9djtK2CRtvn1po3b49h9ps4fFRjRqNnZfu3cbQkZa+yRtm6vWXlYpcrimqquIQt7mnhCreJuxD5JkePqqU5OTdxqXSBJ7ctpir1I83Zc4aDQ8mwqk7eZarqLeWhMrp7Um4symPP6LSDXOtmLJuLT2Q1A7sajbyTaJ3lpLO5socue991rqqxsblLNwIuMi8/AfNMZyiDwWNdHqMRizOjCl/tATz8YQn5PrLdgCHEwToAzTxIbyFEKsMwk/Oku4PDSJrEckl+LNv4iq8kpL2KJc6CeXTtTxyBIRNMozgeCbyCgdOwuqrYTyqtJEz/Yc7CYi8RR0UEILNfRQRBNFdEBFG31KOkdhis4uhxg9KSAAOw=="""
imgdata=base64.b64decode(s)
print(imgdata)
file=open('1.png','wb')
file.write(imgdata)
file.close()
