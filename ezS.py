{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "b'<!DOCTYPE html>\\n<html>\\n<head>\\n<style>\\ndiv.cities {\\n    background-color:black;\\n    color:white;\\n    margin:20px;\\n    padding:20px;\\n} \\n</style>\\n</head>\\n<body>\\n<h1 align=\"center\"> Here are three big cities </h1>\\n<div class=\"cities\">\\n<h2>London</h2>\\n<p>London is the capital of England and it\\'s been a British settlement since 2000 years ago. </p>\\n</div>\\n<div class=\"cities\">\\n<h2>Paris</h2>\\n<p>Paris is the capital city of France. It was declared capital since 508.</p>\\n</div>\\n<div class=\"cities\">\\n<h2>Tokyo</h2>\\n<p>Tokyo is the capital of Japan and one of the most populated cities in the world.</p>\\n</div>\\n</body>\\n</html>'\n"
     ]
    }
   ],
   "source": [
    "r=requests.get(\"https://pythonhow.com/example.html\")\n",
    "c=r.content\n",
    "print(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<!DOCTYPE html>\n",
      "<html>\n",
      " <head>\n",
      "  <style>\n",
      "   div.cities {\n",
      "    background-color:black;\n",
      "    color:white;\n",
      "    margin:20px;\n",
      "    padding:20px;\n",
      "}\n",
      "  </style>\n",
      " </head>\n",
      " <body>\n",
      "  <h1 align=\"center\">\n",
      "   Here are three big cities\n",
      "  </h1>\n",
      "  <div class=\"cities\">\n",
      "   <h2>\n",
      "    London\n",
      "   </h2>\n",
      "   <p>\n",
      "    London is the capital of England and it's been a British settlement since 2000 years ago.\n",
      "   </p>\n",
      "  </div>\n",
      "  <div class=\"cities\">\n",
      "   <h2>\n",
      "    Paris\n",
      "   </h2>\n",
      "   <p>\n",
      "    Paris is the capital city of France. It was declared capital since 508.\n",
      "   </p>\n",
      "  </div>\n",
      "  <div class=\"cities\">\n",
      "   <h2>\n",
      "    Tokyo\n",
      "   </h2>\n",
      "   <p>\n",
      "    Tokyo is the capital of Japan and one of the most populated cities in the world.\n",
      "   </p>\n",
      "  </div>\n",
      " </body>\n",
      "</html>\n"
     ]
    }
   ],
   "source": [
    "soup=BeautifulSoup(c,\"html.parser\")\n",
    "print(soup.prettify())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<div class=\"cities\">\n",
       " <h2>London</h2>\n",
       " <p>London is the capital of England and it's been a British settlement since 2000 years ago. </p>\n",
       " </div>, <div class=\"cities\">\n",
       " <h2>Paris</h2>\n",
       " <p>Paris is the capital city of France. It was declared capital since 508.</p>\n",
       " </div>, <div class=\"cities\">\n",
       " <h2>Tokyo</h2>\n",
       " <p>Tokyo is the capital of Japan and one of the most populated cities in the world.</p>\n",
       " </div>]"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "all=soup.find_all(\"div\",{\"class\":\"cities\"})\n",
    "all"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<div class=\"cities\">\n",
       "<h2>London</h2>\n",
       "<p>London is the capital of England and it's been a British settlement since 2000 years ago. </p>\n",
       "</div>"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "allin=soup.find(\"div\",{\"class\":\"cities\"})\n",
    "allin"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<div class=\"cities\">\n",
       " <h2>London</h2>\n",
       " <p>London is the capital of England and it's been a British settlement since 2000 years ago. </p>\n",
       " </div>, <div class=\"cities\">\n",
       " <h2>Paris</h2>\n",
       " <p>Paris is the capital city of France. It was declared capital since 508.</p>\n",
       " </div>, <div class=\"cities\">\n",
       " <h2>Tokyo</h2>\n",
       " <p>Tokyo is the capital of Japan and one of the most populated cities in the world.</p>\n",
       " </div>]"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "all=soup.find_all(\"div\",{\"class\":\"cities\"})\n",
    "all"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'London'"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "all[0].find_all(\"h2\")[0].text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "London\n",
      "Paris\n",
      "Tokyo\n"
     ]
    }
   ],
   "source": [
    "for city in all:\n",
    "    print(city.find_all(\"h2\")[0].text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "London is the capital of England and it's been a British settlement since 2000 years ago. \n",
      "Paris is the capital city of France. It was declared capital since 508.\n",
      "Tokyo is the capital of Japan and one of the most populated cities in the world.\n"
     ]
    }
   ],
   "source": [
    "for info in all:\n",
    "    print(info.find_all(\"p\")[0].text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "London is something that goes as follows. London is the capital of England and it's been a British settlement since 2000 years ago. \n",
      "Paris is something that goes as follows. Paris is the capital city of France. It was declared capital since 508.\n",
      "Tokyo is something that goes as follows. Tokyo is the capital of Japan and one of the most populated cities in the world.\n"
     ]
    }
   ],
   "source": [
    "for des in all:\n",
    "    print(des.find_all(\"h2\")[0].text,\"is something that goes as follows.\",des.find_all(\"p\")[0].text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
