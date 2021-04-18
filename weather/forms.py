from django.forms import TextInput,ModelForm
from .models import City,Song
class CityForm(ModelForm):
    class Meta:
        model=City
        fields=["name"]
        widgets={"name":TextInput(attrs={"class":"input",
        "placeholder":"cityname"})}

class SpotifyForm(ModelForm):
    class Meta:
        model=Song
        fields=["song_name"]
        widgets={"song_name":TextInput(attrs={"class":"input",
        "placeholder":"songname"})}