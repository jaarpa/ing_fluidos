from django import forms

from piping.models import Project


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = "__all__"

    def clean_T_av(self):
        data = self.cleaned_data["T_av"]
        data += 273.15
        return data
