from django import forms

class CompilerForm(forms.Form):
    lang =( 
    ("1", "C++"), 
    ("2", "Python"), 
    ("3", "Java"), 
) 
    code = forms.CharField(widget=forms.Textarea)
    input = forms.CharField(widget=forms.Textarea,required=False)
    language = forms.ChoiceField(choices = lang, initial=2) 