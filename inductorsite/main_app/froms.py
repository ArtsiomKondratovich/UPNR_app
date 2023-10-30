from django import forms

from main_app.models import Inductors, TubeShapes


class AddInductorForm(forms.ModelForm):
    tube_shape = forms.ModelChoiceField(queryset=TubeShapes.objects.all(), label= 'Вид трубки')
    class Meta:
        model = Inductors
        fields = '__all__'