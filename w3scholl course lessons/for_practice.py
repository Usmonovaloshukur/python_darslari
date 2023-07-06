
# #################### unpack a list  ( listni ochish )
#
# mevalar = ["olma", "anor", "uzum"]
#
# x, y, z = mevalar
# print(x)
# print(y)
# print(z)
# # natija:
# # olma
# # anor
# # uzum



# ###############################  global variables

# x = "awesome"
#
# def myfunk():
#     print("Python is", x)
# myfunk()
#
#
# x = "awesome"
#
# def myfunc1():
#     x = "fantastic"
#     print("Python is " + x)
#
# myfunc1()
#
# print("Python is " + x)

# def myfunc2():
#   global x
#   x = "fantastic"
#
# myfunc2()
#
# print("Python is " + x)

# ##### change the value of variable by using function

# x = "awesome"
#
# def myfunc():
#   global x
#   x = "fantastic"
#
# myfunc()
#
# print("Python is " + x)

# #####################  type conversion

# z = 10
# x = complex(z)
# print(x)
# print(type(x))
#
# z_float = float(z)
# print(z_float)

# a = -25.7
# b = int(a)
# print(b)

# a = 12 + 13j
# b = int(a)
# print(b)
# # typeError argument of int() must be string, bytes-like object or a real number


# numbers tugadi w3scholldan

# #############################   pythpon strings  ########################

# txt = "The best thing in life is free!"
#
# print('free' in txt)  # result: True

# a = "Hello world"
# print(a[2:5])
# print(a[-5:-2])