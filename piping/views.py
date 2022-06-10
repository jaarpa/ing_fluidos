from typing import Any, Dict

from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic import DeleteView

from CoolProp import CoolProp as CP

from piping.models import Project
from piping.forms import ProjectForm
# Create your views here.


class ProjectCreateView(CreateView):
    model = Project
    template_name = "generic_form.html"
    form_class = ProjectForm


class ProjectListView(ListView):
    model = Project
    template_name = "project_list.html"
    paginate_by: int = 15

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["project_form"] = ProjectForm()
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = "project.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        temp = context["object"].T_av
        pressure = context["object"].P_av
        fluid = context["object"].fluid
        context["viscosity"] = CP.PropsSI("V", "P", pressure, "T", temp, fluid)
        context["density"] = CP.PropsSI("D", "P", pressure, "T", temp, fluid)
        return context


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = "generic_delete.html"
    success_url = "piping:piping_projects"

    def get_success_url(self) -> str:
        return reverse(self.success_url)
