from django.utils.translation import ugettext_lazy as _
from typing import Optional, Dict, Any
from django import forms

from piping.models import Project, ProjectAccessory


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = "__all__"


class ProjectAccessoryForm(forms.ModelForm):

    class Meta:
        model = ProjectAccessory
        fields = "__all__"
        widgets = {"project": forms.HiddenInput}

    def clean(self) -> Optional[Dict[str, Any]]:
        cleaned_data = super().clean()
        accessory = cleaned_data["accessory"]
        requires_angle = ["bend_rounded", "K_tilting_disk_check_valve_Crane"]
        requires_d2 = [
            "diffuser_sharp", "contraction_sharp",
            "K_angle_stop_check_valve_Crane", "K_angle_valve_Crane",
            "K_globe_valve_Crane", "K_lift_check_valve_Crane",
        ]
        requires_both = [
            "K_ball_valve_Crane", "K_gate_valve_Crane", "K_plug_valve_Crane",
        ]
        if accessory in requires_both and (
            not cleaned_data["angle"] or not cleaned_data["inner_diameter2"]
        ):
            raise forms.ValidationError(_(
                "This component requires a second inner diameter provided")
            )
        elif accessory in requires_angle and not cleaned_data["angle"]:
            raise forms.ValidationError(_(
                "This component requires a second inner diameter provided")
            )
        elif accessory in requires_d2 and not cleaned_data["inner_diameter2"]:
            raise forms.ValidationError(_(
                "This component requires a second inner diameter provided")
            )
        return cleaned_data
