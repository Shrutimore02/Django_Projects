from django import forms 
from iplapp.models import CSKTable
from iplapp.models import DCTable
from iplapp.models import GTTable
from iplapp.models import KKRTable
from iplapp.models import LSGTable
from iplapp.models import MITable
from iplapp.models import PKTable
from iplapp.models import RCBTable
from iplapp.models import RRTable
from iplapp.models import SRHTable

class CSKTableForm(forms.ModelForm):
    class Meta:
        model = CSKTable
        fields = ('__all__')

class DCTableForm(forms.ModelForm):
    class Meta:
        model = DCTable
        fields = ('__all__')

class GTTableForm(forms.ModelForm):
    class Meta:
        model = GTTable
        fields = ('__all__')

class KKRTableForm(forms.ModelForm):
        class Meta:
            model = KKRTable
            fields = ('__all__')

class LSGTableForm(forms.ModelForm):
    class Meta:
        model = LSGTable
        fields = ('__all__')

class MITableForm(forms.ModelForm):
    class Meta:
        model = MITable
        fields = ('__all__')

class PKTableForm(forms.ModelForm):
    class Meta:
        model = PKTable
        fields = ('__all__')

class RCBTableForm(forms.ModelForm):
    class Meta:
        model = RCBTable
        fields = ('__all__')

class RRTableForm(forms.ModelForm):
    class Meta:
        model = RRTable
        fields = ('__all__')

class SRHTableForm(forms.ModelForm):
    class Meta:
        model = SRHTable
        fields = ('__all__')
    
    
    
    
    
    
            
    


