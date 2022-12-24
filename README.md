# W4-Task

with **`CRUD`** oprations on **`Blog`** model

## Routes
by using **`Django-Ninja`**, i create a 4-routes for the **`CRUD`** oprations, by using schemas to validata the payload and parse the response in it, and the Router to provide an access to each endpoints
> * check it after run on 'http://127.0.0.1:8000/api/docs'

## Schema
1. **`blog.py`**:
```python=1
from ninja import Schema

class BlogSchema(Schema):
    id: int
    title: str
    description: str


class BlogIn(Schema):
    title: str
    description: str

``` 
2. **`response`**:
```python=1
from ninja import Schema

class MessageSchema(Schema):
    message: str
```
## templates 
1. i create **`table_form.html`** **`table.html`**,and **`table_row.html`** for design the page.
2. in **`/partials/`** i update in **`table_opereations`** by adding:
    * **`get_blogs`**: The Main Function that incude all below methods:
        * **`init()`**: To fetch the blogs and put it in the table
        * **`create_blog`**: with Two Vars (**`Title`**, **`description`**) That Binding with form field, and return async function (**`add_blog`**)
        * **`delete_blog`**: That recive **`Blog.id`** and send it as params to delete it
        * **`update_blog`**: That recive **`Blog.id`** and send it as a payload 


## Note
in Alpine code, i check if the response is success or not depending on **`message`** i sent from the backend with the response schema, cause i didn't know how to access **`status code`** (**`cause it is my first time in django- ninja`**)
    so the code become:
    
```javascript=1
if (response.message === "Ok"){
    this.msg = 'deleted'
}
else{
    this.error_msg = 'there was an error !!'
}
```

**`i try`** : 
```javascript=1
if (response.status >= 200 && response.status < 300){
    this.msg = 'deleted'
}
```
**`and `**
```javascript=1
if (response.statusCode >= 200 && response.statusCode < 300){
    this.msg = 'deleted'
}
```
**`but both of it return undefind`**
