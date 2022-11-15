# Инкапсуляция
# private protected public

# class Product:
#
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def get_info(self):
#         print(f"{self.name} - {self.price}")
#
# potato = Product("potato", 25)
# #print(potato.price)
# potato.get_info()

# import uuid
# class Bank:
#     def __init__(self, name: str):
#         self.name = name
#         self.__account = str(uuid.uuid4())
#
#     def get_account(self):
#         print(f"Your account is: {self.__account}")
#
# nazgul = Bank("Nazgul")
# # print(nazgul.__dict__)
# # print(nazgul._Bank__account)
# nazgul.get_account()


# import uuid
#
# class Bank:
#     def __init__(self, name: str):
#         self.name = name
#         self.__generate_account()
#
#     def __generate_account(self):
#         self.__account = str(uuid.uuid4())
#
#     def get_account(self):
#         print(f"Your account is: {self.__account}")
#
#     def set_account(self):
#         self.__account = str(uuid.uuid4()) + self.name
#
# nazgul = Bank("Nazgul")
# nazgul.get_account()
# nazgul.set_account()
# nazgul.get_account()

# import uuid
# class Bank:
#     def __init__(self, name: str):
#         self.name = name
#         self.__generate_account()
#
#     def __generate_account(self):
#         self.__account = str(uuid.uuid4())
#
#     @property
#     def account(self):
#         print(f"Your account is: {self.__account}")
#
#     @account.setter
#     def account(self, key_word: str):
#         self.__account = str(uuid.uuid4()) + key_word
#
# nazgul = Bank("Nazgul")
# nazgul.account
# nazgul.account = "no_name"
# nazgul.account

# list_names = ["nazgul", "abay", "apgen", "nuray"]
# validate_username()
# class Registration:
#     def __init__(self, user_name, password, email):
#         sef.validate_username = user_name
#         self.password = password
#         self.email = email
#
#     def chek_username(self):
#         if self.user_name in list_names:
#             raise Exception("Имя ползователья уже существует, выберите другое имя")
#         else:
#             validate_username.append(self.user_name)
#
#     def get_info(self):
#         print(self.user_name, self.password, self.email)
#
#
# sergey = Registration("Sergey","vnkdjfnasjk", "kndsf@mail.ru")


# list_names = ["nazgul", "abay", "apgen", "nuray"]
#
# class Registration:
#     def __init__(self, username: str, password: str):
#         self.username = self.__validate_username(username)
#         self.password = self.__validate_password(password)
#
#     def __validate_username(self, username):
#         if username not in list_names:
#             list_names.append(username)
#             return username
#         raise Exception("Имя ползователья уже существует, выберите другое имя")
#
#     def __validate_password(self, password):
#         if len(password) < 8 or self.password.isalpha() or self.password.isdigit() or self.password[0].islower():
#             raise Exception("Пароль должен содержать не менее 8 символов включая символы и числа")
#
#
# sergey = Registration("Sergey", "vnkdjfnasjk")


# username_list = ["Sman", ]
# email_tail_list = ["@gmail.com", "@outlook.com", "@mail.ru"]
# class Registration:
#
#     def __init__(self, username: str, password: str, email: str):
#         self.save(username, password, email)
#
#     def __validate_username(self, username):
#         if username not in username_list:
#             username_list.append(username)
#             return True
#         raise Exception("пользователь уже существует!!!")
#
#     def __validate_password(self, password):
#         if len(password) < 8 or password.isalpha() or password.isdigit() or password[0].islower():
#             raise Exception("Пароль должен содержать не менее 8 символов включая символы и числа")
#         return True
#
#     def __validate_email(self, email: str):
#         for i in email_tail_list:
#             if email.endswith(i):
#                 return True
#             raise Exception(" error email")
#
#     def save(self, username, password, email):
#         if (self.__validate_email(email) and
#                 self.__validate_password(password) and
#                 self.__validate_username(username)):
#             self.username = username
#             self.password = password
#             self.email = email
#
#
# nazgul = Registration("Nazgul", "K,dfjvblf23", "t@gmail.com")
# sergey = Registration("Sergey", "K,dfjvblf23", "t@gmail.com")
# rano = Registration("Rano", "Khfhdhlf23", "sdsgsgt@gmail.com")
# # print(nazgul.username)
# print(username_list)
