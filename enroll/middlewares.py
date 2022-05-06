
#######################################################################################################

# def my_middleware(get_resopnse):
#     print("one time inilitiazation")
#     def my_function(request):
#         print("this is before the view")
#         response = get_resopnse(request)
#         print("this is after view")
#         return response
#     return my_function



# now add in setting.py middleware    


#############################################################################################


#class based middleware


class MyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("one time inilitiazation")  
    def __call__(self, request):
        print("This is before view")
        response = self.get_response(request)
        print("This is after view")
        return response
         

        
        