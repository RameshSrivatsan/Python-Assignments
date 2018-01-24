{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Q: Hey How are you?\n",
      " A: HI I am good!\n",
      "Q: How is your course?\n",
      " A: Its very hectic\n"
     ]
    }
   ],
   "source": [
    "#Question-1\n",
    "class Question:\n",
    "   \n",
    "    def __init__(self,question1,question2):\n",
    "        self.question1 = question1\n",
    "        self.question2 = question2\n",
    "        \n",
    "    def __str__(self):\n",
    "        self.l = ['HI I am good!','Its very hectic']\n",
    "        print('Q:',self.question1 + '\\n','A:',self.l[0])\n",
    "        print('Q:',self.question2 + '\\n','A:', self.l[1])\n",
    "            \n",
    "        \n",
    "c = Question('Hey How are you?','How is your course?')\n",
    "c.__str__()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'v ebpx'"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# QUestion-2\n",
    "import collections\n",
    "import csv\n",
    "response = requests.get('https://data.cityofnewyork.us/api/views/w7w3-xahh/rows.csv?accessType=DOWNLOAD')\n",
    "rows_1 = response.content.decode().split('\\n')\n",
    "rows = list(csv.DictReader(rows_1))\n",
    "rows\n",
    "area_codes = collections.Counter()\n",
    "zip_codes = collections.Counter()\n",
    "\n",
    "for a in rows:\n",
    "    if a['License Type'] == 'Individual':\n",
    "        zip_codes[a['Address ZIP']]+= 1\n",
    "        area_codes[a['Address State']] += 1\n",
    "print(zip_codes.most_common(1))\n",
    "print(area_codes.most_common(1))\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2011 MALE [('AARON', 20)]\n",
      "2011 FEMALE [('GRACE', 20)]\n",
      "2012 MALE [('AARON', 8)]\n",
      "2012 FEMALE [('ABIGAIL', 8)]\n",
      "2013 MALE [('Aaron', 8)]\n",
      "2013 FEMALE [('Abigail', 8)]\n",
      "2014 MALE [('Aaron', 8)]\n",
      "2014 FEMALE [('Abigail', 8)]\n"
     ]
    }
   ],
   "source": [
    "# QUestion-3\n",
    "import csv\n",
    "import collections\n",
    "import requests\n",
    "from collections import Counter\n",
    "response = requests.get('https://data.cityofnewyork.us/api/views/25th-nujf/rows.csv?accessType=DOWNLOAD')\n",
    "rows_1 = response.content.decode().split('\\n')\n",
    "rows = list(csv.DictReader(rows_1))\n",
    "rows\n",
    "for year in ['2011','2012','2013','2014']:\n",
    "    for gender in ['MALE','FEMALE']:\n",
    "        names = [s['Child\\'s First Name'] for s in rows if s['Year of Birth'] == year and s['Gender'] == gender]\n",
    "        names_1 = Counter(names)\n",
    "        print(year,gender,names_1.most_common(1))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[('A', 642)]\n"
     ]
    }
   ],
   "source": [
    "first_letter = [t['Child\\'s First Name'][0] for t in rows if t['Year of Birth'] == '2012']\n",
    "first_letter = Counter(first_letter)\n",
    "print(first_letter.most_common(1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[('a', 1604)]\n"
     ]
    }
   ],
   "source": [
    "mostcommon_letter = [t['Child\\'s First Name'].lower() for t in rows if t['Year of Birth'] == '2014' and t['Gender'] == 'MALE']\n",
    "c = []\n",
    "for a in mostcommon_letter:\n",
    "    for b in a:\n",
    "        c.append(b)\n",
    "mostcommonletter = Counter(c)\n",
    "print(mostcommonletter.most_common(1))\n",
    "        \n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "187"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Question-4\n",
    "import bs4\n",
    "import collections\n",
    "import requests\n",
    "response = requests.get(' http://www.nytimes.com/')\n",
    "soup = bs4.BeautifulSoup(response.content,'html.parser')\n",
    "len(soup.find_all('a'))\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "120"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Question-5\n",
    "def fac(n):\n",
    "    x = 1\n",
    "    while n>1:\n",
    "        x*= n\n",
    "        n-= 1\n",
    "        \n",
    "    return(x)\n",
    "fac(5)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#Question-6\n",
    "import string\n",
    "def ciphertext(plaintext):\n",
    "    plaintext = plaintext.lower()\n",
    "    ciphertext = ''\n",
    "  \n",
    "    for b in plaintext:\n",
    "        if b in string.ascii_lowercase:\n",
    "            b = chr(((ord(b)-ord('a') + 13)%26)+ ord('a'))\n",
    "            ciphertext += b\n",
    "        else:\n",
    "            b = ' '\n",
    "            ciphertext += b\n",
    "    return ciphertext\n",
    "ciphertext('I rock')"
   ]
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
   "version": "3.6.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
