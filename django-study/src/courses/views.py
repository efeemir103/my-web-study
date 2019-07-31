from django.shortcuts import render
from django.views import View


# Base View Class = View
class CourseView(View):
    template_name='index.html'
    def get(self, request, *args, **kwargs):
        # GET method
        return render(request, self.template_name, {})
    
    #def post(self, request, *args, **kwargs):
    #    return render(request, self.template_name, {})

# HTTP METHODS
def my_fbv(request, *args, **kwargs):
    return render(request, 'courses.html', {})