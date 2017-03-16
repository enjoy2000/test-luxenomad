# Test LuxeNomad

### 1. In python what’s the difference between *args **kwargs explain with an example
`*` is something like `tuple` while ``**` is something like `dictionary` for function parameters.

example:
```python
def demo_args(*args):
    print(*args)

demo_args(1) # output (1)
demo_args(2, 3, 4, 2) # output (2, 3, 4, 2)

def demo_kwargs(**kwargs):
    print(**kwargs)

demo_kwargs(a=1, b=2, c=3) # output {'a': 1, 'b': 2, 'c': 3}
demo_kwargs()  # output {}

def print_three_things(a, b, c):
    print(a)
    print(b)
    print(c)

three_things = [1, 2, 3]
print_three_things(*three_things) # output 1 2 3

def print_two_things_with_kwargs(first_param=1, second_param=2):
    print(first_param)
    print(second_param)

two_things = {'first_param': 1000, 'second_param': 2000}
print_two_things_with_kwargs(**two_things) # output 1000 2000

```

### 2. What will happened if you pass to a function with 2 arguments  def print_three_things(a,b,c)

Raise type error missing argument

### 3. Write a function that sorts the following array of numbers  [1,3,4,536,13,1234,6,31,3,5,6]
without using any inbuilt utility methods, just the conventional code

```python
python3 test3.py
```
### 4. Explain MV* patterns and in particular the MVT pattern in Django. What are the advantages of such patterns?
is that `model` - `view`?

If that, only for separate the logic and layout so can be maintenance easier, sames goes for `controller`, `presenter`, etc..

I never heard about MVT before


### 5. What is the purpose of async/await in Python.
What are the restrictions, and what does it “replace”. Code a simple example of usage with a "timeout"

`async/await` is combined of `yield` and `asyncio` use for asynchronous programming, I'm not much familiar with that
only use when I need to do `event handling` like when I do on a `chatbot` for discord, I use it for listen to `outgoing webhooks`
and send `events` whenever have a new message, then I will do stuff on that message.

Or use for some `event loop` when I want that task keep doing all the time.
[demo](https://github.com/enjoy2000/discord-pokemon-go-snipe-bot/blob/master/bot.py)

Anw, I don't know this well.


### 6. Implement a reverse polish notation calculator. Assume the inputs are in RPN.
An arithmetic expression such as '12 * 1 - 5' is translated to '12 1 * 5 -'
Input: 12 1 * 5 -
Output: 7

```python
python3 test6.py
```
