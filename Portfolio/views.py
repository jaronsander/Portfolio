from django.views import generic

from Portfolio.models import Project

class IndexView(generic.TemplateView):
    template_name = 'Portfolio/index.html'

class ProjectListView(generic.ListView):
    template_name = 'Portfolio/projects.html'
    model = Project

    def get_queryset(self):
        return Project.objects.all()