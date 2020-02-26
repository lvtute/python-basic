# Python basic
This is my workspace for learning basic Python by following the instruction from an Udemy course.


## Important notes
**Data types**
```python
  first_name= 'John'
age = 39

# This is a list- list can be changed
first_name = ["John", "Bob", "Tina"]

#This is a tuple- tuple CAN NOT be changed
# but tuple is a little bit faster than list
last_name = ("Cruise", "Hanks", "Cumberbatch")
print(first_name)
print(last_name[1])

#This is a dictionary
fav_pizza= {
    "John":"Pepperoni",
    "Bob":"Cheese",
    "Tina":"Supreme"
}

print(fav_pizza)
print(fav_pizza["Tina"])

```
```python
talking = 'My mom yelled "Clean your room!"'
# My mom yelled "Clean your room!"
```

---


**pip commands**
* To check installed packages 
```
pip freeze
```
* To install a package 
```pip
pip install virtualenv
```

* To create virtual environment
```pip
pip -m venv venv
```

* To turn on virtual environment
```pip
source venv/Scripts/activate
```

* To turn off virtual environment
```pip
deactivate
```

* To create a django project
```pip
django-admin.py startproject weather
```



