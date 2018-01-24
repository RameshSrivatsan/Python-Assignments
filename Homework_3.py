{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0 FizzBuzzBang\n",
      "3 Fizz\n",
      "5 Buzz\n",
      "6 Fizz\n",
      "7 Bang\n",
      "9 Fizz\n",
      "10 Buzz\n",
      "12 Fizz\n",
      "14 Bang\n",
      "15 FizzBuzz\n",
      "18 Fizz\n",
      "20 Buzz\n",
      "21 FizzBang\n",
      "24 Fizz\n",
      "25 Buzz\n",
      "27 Fizz\n",
      "28 Bang\n",
      "30 FizzBuzz\n",
      "33 Fizz\n",
      "35 BuzzBang\n",
      "36 Fizz\n",
      "39 Fizz\n",
      "40 Buzz\n",
      "42 FizzBang\n",
      "45 FizzBuzz\n",
      "48 Fizz\n",
      "49 Bang\n",
      "50 Buzz\n",
      "51 Fizz\n",
      "54 Fizz\n",
      "55 Buzz\n",
      "56 Bang\n",
      "57 Fizz\n",
      "60 FizzBuzz\n",
      "63 FizzBang\n",
      "65 Buzz\n",
      "66 Fizz\n",
      "69 Fizz\n",
      "70 BuzzBang\n",
      "72 Fizz\n",
      "75 FizzBuzz\n",
      "77 Bang\n",
      "78 Fizz\n",
      "80 Buzz\n",
      "81 Fizz\n",
      "84 FizzBang\n",
      "85 Buzz\n",
      "87 Fizz\n",
      "90 FizzBuzz\n",
      "91 Bang\n",
      "93 Fizz\n",
      "95 Buzz\n",
      "96 Fizz\n",
      "98 Bang\n",
      "99 Fizz\n"
     ]
    }
   ],
   "source": [
    "# Question 1\n",
    "for i in range(0,100):\n",
    "    if i % 3 == 0 and i % 5 == 0 and i % 7 ==0 :\n",
    "        print( i , \"FizzBuzzBang\")\n",
    "    elif i % 3 == 0 and i % 5 == 0 :\n",
    "        print( i , \"FizzBuzz\")\n",
    "    elif i % 5 ==0 and i % 7 == 0 :\n",
    "        print( i , \"BuzzBang\")\n",
    "    elif i % 3 == 0 and i % 7 == 0 :\n",
    "        print( i , \"FizzBang\")\n",
    "    elif i % 3 == 0 :\n",
    "        print( i , \"Fizz\")\n",
    "    elif i % 5 == 0 :\n",
    "        print( i , \"Buzz\")\n",
    "    elif i % 7 == 0 :\n",
    "        print( i , \"Bang\")\n",
    "        \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "a4b5c5\n"
     ]
    }
   ],
   "source": [
    "# Question 2\n",
    "A = \"aaaabbbbbccccc\"\n",
    "count = 0\n",
    "alpha = 0\n",
    "beta = 0\n",
    "for j in A :\n",
    "    if j == 'a' :\n",
    "        count += 1\n",
    "    elif j == 'b' :\n",
    "        alpha += 1\n",
    "    elif j == 'c' :\n",
    "           beta += 1\n",
    "print(\"a%db%dc%d\"%(count,alpha,beta))\n",
    "     \n",
    "        \n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the denomination for change:0.81\n",
      "{'Quarter': 3, 'Dime': 0, 'Nickel': 1, 'Cent': 1}\n"
     ]
    }
   ],
   "source": [
    "q = []\n",
    "d = []\n",
    "a= []\n",
    "c = []\n",
    "def get_change_for(x) :\n",
    "    for n in range(0 , 10) :\n",
    "        if n * 0.25 < x :\n",
    "            q.append(n)\n",
    "    r = x - (q[len(q)-1]* 0.25)\n",
    " \n",
    "    for p in range(0, 10):\n",
    "        if p * 0.1 < r :\n",
    "            d.append(p)\n",
    "    s= r - (d[len(d)-1]* 0.1)\n",
    "\n",
    "    for t in range(0 , 10) :\n",
    "        if t * 0.05 < s :\n",
    "            a.append(t)\n",
    "    u = s - (a[len(a)-1]* 0.05)\n",
    "   \n",
    "    for v in range(0 , 10) :\n",
    "        if v * 0.01 < u :\n",
    "            c.append(v)\n",
    "    x = u - (c[len(c)-1]* 0.01)\n",
    "    \n",
    "    \n",
    "    dict={ 'Quarter': q[len(q)-1], 'Dime': d[len(d)-1], 'Nickel': a[len(a)-1], 'Cent': c[len(c)-1]}\n",
    "    return(dict)\n",
    "\n",
    "\n",
    "\n",
    "    \n",
    "            \n",
    "x = input(\"Enter the denomination for change:\")\n",
    "y = get_change_for(float(x))\n",
    "print(y)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 82,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Question 4\n",
    "def funcA(func,x):\n",
    "    \n",
    "        return(func(x) + 1)\n",
    "        \n",
    "def funcB(x):\n",
    "    a = x + 1\n",
    "    return(a)\n",
    "\n",
    "\n",
    "funcA(funcB,1)\n",
    "\n"
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
