# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
MyClass = type('MyClass', (), {
    'class_variable': 'Hello, World!',
    '__init__': lambda self: print('Initializing MyClass'),
    'my_method': lambda self: print('Hello from MyClass')
})


# %%
a = MyClass()

# %%
a.class_variable

# %%
b = MyClass()

# %%
a.class_variable, b.class_variable

# %%
MyClass.class_variable = 1000

# %%
