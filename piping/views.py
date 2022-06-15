from typing import Any, Dict

from django.urls import reverse
from django.forms.models import model_to_dict
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic import UpdateView, DeleteView


from piping.models import Project, ProjectAccessory
from piping.forms import ProjectForm, ProjectAccessoryForm
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
        project = context["object"]
        context["density"] = project.get_rho()
        context["viscosity"] = project.get_mu()
        context["accessories"] = ProjectAccessory.objects.filter(
            project=project
        )
        intial_accesory = context["accessories"].order_by("id").last()
        inital_values = {"project": project.id}
        if intial_accesory:
            inital_values.update({
                "inner_diameter": intial_accesory.inner_diameter,
                "material": intial_accesory.material
            })
        context["accessory_form"] = ProjectAccessoryForm(
            initial=inital_values
        )
        context["update_project_form"] = ProjectForm(
            initial=model_to_dict(project)
        )
        return context


class ProjectUpdateView(UpdateView):
    model = Project
    template_name = "generic_form.html"
    form_class = ProjectForm


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = "generic_delete.html"
    success_url = "piping:piping_projects"

    def get_success_url(self) -> str:
        return reverse(self.success_url)


class ProjectAccessoryCreateView(CreateView):
    model = ProjectAccessory
    template_name = "generic_form.html"
    form_class = ProjectAccessoryForm

    def post(self, request, *args: Any, **kwargs: Any):
        return super().post(request, *args, **kwargs)

    def get_success_url(self) -> str:
        return self.object.project.get_absolute_url()


class ProjectAccessoryDeleteView(DeleteView):
    model = ProjectAccessory
    template_name = "generic_delete.html"

    def get_success_url(self) -> str:
        return self.object.project.get_absolute_url()
