import functions_framework

@functions_framework.http
def my_function(request):
    return "It worked! Target was respected."