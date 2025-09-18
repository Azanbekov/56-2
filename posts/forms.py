from django import forms
from posts.models import Post, Category

class PostForm(forms.Form):
    image = forms.ImageField(required=True)
    title = forms.CharField(max_length=200, required=True)
    content = forms.CharField(max_length=550, required=True)

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data("title")
        content = cleaned_data("content")
        if (title and content) and (title.lower() == content.lower):
            raise  forms.ValidationError("Title and content cannot be same")
        return cleaned_data


class PostForm2(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["image", "title", "content"]

    def clean_title(self):
        cleaned_data = super().clean()
        if title and ttitle.lower() == "Python":
            raise forms.ValidationError("Titke cannot be python")
        return title

class SearchForm(forms.Form):
    search = forms.CharField(max_length=290, min_length=1, required=False)
    category_id = forms.ModelChoiceField(queryset=Category.objects.all(), required=False, label="Category")
    orderings = (
        ("created_at", "По дате создания") , 
        ("title","По названию"),
        ("rate", "По рейтингу"),
        ("-created_at", "По дате создания(по убыванию)"),
        ("-title","По названию(по убыванию)"), 
        ("-rate","По рейтингу(по убыванию)"),
        (
        None,
        "---"
        ),
    )
    ordering = forms.ChoiceField(choices=orderings, required=False)
