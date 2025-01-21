# from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
# from django.dispatch import receiver
# from django.contrib.auth.models import User
# from django.db.models.signals import pre_init,pre_save, pre_delete,post_init, post_delete,post_save
# from django.core.signals import request_started,request_finished,got_request_exception

# #Authentication Signals
# @receiver(user_logged_in,sender=User)
# def login_success(sender,request,user, **kwargs):
#     print("--------------------------")
#     print("logged-in Signal")
#     print("sender:",sender)
#     print("request:",request)
#     print("user:",user)
#     print("User Password:", user.password)
#     print(f'kwargs: {kwargs}')

# # user_logged_in.connect(login_success,sender=User)

# @receiver(user_logged_out,sender=User)
# def log_out(sender,request,user,**kwargs):
#     print("--------------------------")
#     print("logged-out Signal")
#     print("sender:",sender)
#     print("request:",request)
#     print("user:",user)
#     print(f'kwargs: {kwargs}')

# # user_logged_out.connect(log_out,sender=User)

# @receiver(user_login_failed)
# def login_failed(sender,credentials,request,**kwargs):
#     print("--------------------------")
#     print("login failed  Signal")
#     print("sender:",sender)
#     print("Credentials:",credentials)
#     print("request:",request)
#     print(f'kwargs: {kwargs}')
# # user_login_failed.connect(log_out)

# # Model Signal> set of signal send by the model system

# @receiver(pre_save,sender=User)
# def at_begining_save(sender,instance,**kwargs):
#     print("--------------------------")
#     print("Pre Save Signal...")
#     print("Sender:",sender)
#     print("Instance:",instance)
#     print(f'kwargs: {kwargs}')

# # pre_save.connect(at_begining_save,sender=User)


# @receiver(post_save,sender=User)
# def at_ending_save(sender,instance,created,**kwargs):
#     if created:
#         print("--------------------------")
#         print("Post Save Signal...")
#         print("New Recored Created")
#         print("Sender:",sender)
#         print("Instance:",instance)
#         print("Created",created)
#         print(f'kwargs: {kwargs}')
#     else:
#         print("--------------------------")
#         print("Post Save Signal...")
#         print("Update")
#         print("Sender:",sender)
#         print("Instance:",instance)
#         print("Created",created)
#         print(f'kwargs: {kwargs}')

# # post_save.connect(at_begining_save,sender=User)

# # Delete Signals
# @receiver(pre_delete,sender=User)
# def at_begining_delete(sender,instance,**kwargs):
#     print("--------------------------")
#     print("At Begining Delete...")
#     print("Sender:",sender)
#     print("Instance:",instance)
#     print(f'kwargs: {kwargs}')

# # pre_delete.connect(at_begining_save,sender=User)

# @receiver(post_delete,sender=User)
# def at_ending_delete(sender,instance,**kwargs):
#         print("--------------------------")
#         print("Post Delete Signal...")
#         print("Sender:",sender)
#         print("Instance:",instance)
#         print(f'kwargs: {kwargs}')

# # post_delete.connect(at_begining_save,sender=User)

# # init signals

# @receiver(pre_init,sender=User)
# def at_begining_init(sender,*args,**kwargs):
#     print("--------------------------")
#     print("Pre init Signal...")
#     print("Sender:",sender)
#     print(f'Args: {args}')
#     print(f'kwargs: {kwargs}')

# # pre_init.connect(at_begining_save,sender=User)

# @receiver(post_init,sender=User)
# def at_ending_init(sender,*args,**kwargs):
#         print("--------------------------")
#         print("Post init Signal...")
#         print("Sender:",sender)
#         print(f'Args: {args}')
#         print(f'kwargs: {kwargs}')
   
# # post_init.connect(at_begining_save,sender=User)


# #request response signal
# # sent by the   core framework when processing a request


# @receiver(request_started)  
# def at_begining_request(sender,environ,**kwargs):
#     print("--------------------------")
#     print("At Begining Request...")
#     print("Sender:",sender)
#     print(f'Environ: {environ}')
#     print(f'kwargs: {kwargs}')

# # request_started.connect(at_begining_save,sender=User)

# @receiver(request_finished)
# def at_ending_request(sender,**kwargs):
#     print("--------------------------")
#     print("At Ending Request...")
#     print("Sender:",sender)
#     print(f'kwargs: {kwargs}')
# # request_finished.connect(at_begining_save,sender=User)


# @receiver(got_request_exception)
# def at_req_exception(sender,request,**kwargs):
#     print("--------------------------")
#     print("At Request Exception...")
#     print("Sender:",sender)
#     print("Request:", request)
#     print(f'kwargs: {kwargs}')
# # got_request_exception.connect(at_begining_save,sender=User)

# # Management Signals
# # Signal sent by Django Admin