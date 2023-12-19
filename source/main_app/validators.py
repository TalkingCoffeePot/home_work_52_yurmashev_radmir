from django import forms

def clean_description(self):
    desc = self.cleaned_data['description']
    if 'fuck' in desc:
        raise forms.ValidationError("Нецензурные выражения недопустимы!")
    return desc
    
def clean_tite(self):
    title = self.cleaned_data['title']
    if len(title) < 5:
        raise forms.ValidationError("Слишком короткое название")
    return title