from django.forms import ModelForm
from django import forms
from civam.models import *
from guardian.models import Group
from django.core.exceptions import NON_FIELD_ERRORS

# Civam forms are defined here

class StoryForm(ModelForm):
    class Meta:
        model = Story
        fields = ['content', 'author']
        
class CollectionForm(ModelForm):
    class Meta:
        model = Collection
        fields = ['title', 'description', 'public']


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description']

# Displayed on same page as ItemForm
class ImageForm(forms.Form):
    content = forms.ImageField(required=False)

# Displayed on same page as ItemForm
class VideoForm(forms.Form):
    link = forms.URLField(required=False)

    
class CollectionGroupForm(ModelForm):
    class Meta:
        model = CollectionGroup
        fields = ['name', 'default', 'collection']
        widgets = {'collection': forms.HiddenInput()} # The collection is a hidden input that is automatically filled
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "A group with that name already exists for this collection.",
            }
        }

# The form for assigning permissions to a CollectionGroup
# Seperate form object but displayed on the same page as CollectionGroupForm
class GroupPermissionsForm(forms.Form):

    # List objects belonging the collection specified by collection_id
    def __init__(self,*args,**kwargs):
        collection_id = kwargs.pop('collection_id')
        super(GroupPermissionsForm,self).__init__(*args,**kwargs)
        self.fields['items'].queryset = Item.objects.filter(collection_id=collection_id)

    # Items in the collection can be checked/unchecked to grant/remove permission on that Item for the CollectionGroup
    items = forms.ModelMultipleChoiceField(queryset = Item.objects.none(), widget = forms.CheckboxSelectMultiple, required=False)
