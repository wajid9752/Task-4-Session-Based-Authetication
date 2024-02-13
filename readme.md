

# output

<b> In this task there is no ui output. I have done Session based authentication in this task <b>


Note :This configuration is only for Windows users.



## Step 1 : Clone the repository first

```
git clone https://github.com/wajid9752/Task-4-Session-Based-Authetication.git
```


## Step 2 : Install and Create a env.


```
pip install virtualenv 
```

```
virtualenv project_env
```

## Step 3: Activate the Env.

```
project_env\Scripts\activate
```

## Step 4 : Install the requirements using requirements.txt file

```
pip install -r requirements.txt
```

## step 5: Migrate the db 

```
python manage.py migrate
```


## step 6 : Run the server now 
```
python manage.py runserver
```