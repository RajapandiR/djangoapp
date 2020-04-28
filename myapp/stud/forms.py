from django import forms
from .models import Computer
class computerAdd(forms.ModelForm):
	class Meta:
		model = Computer
		# fields = ['fullName' , 'fatherName', 'dob', 'gender', 'email', 'degree', 'dept', 'year']
		fields = '__all__'
		widgets = {
			'fullName': forms.TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Full Name'
			}),
			'fatherName': forms.TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Father Name'
			}),
			'dob': forms.TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'dob'
			}),
			'gender': forms.Select( attrs={
				'class': 'form-control',

			}),
			'email': forms.EmailInput(attrs={
				'class': 'form-control',
				'placeholder': 'Email'
			}),
			'degree': forms.Select(attrs={
				'class': 'form-control',

			}),
			'dept': forms.Select(attrs={
				'class': 'form-control',
			}),
			'year': forms.Select(attrs={
				'class': 'form-control',
			}),
			'address': forms.Textarea(attrs={
				'class': 'form-control',
				'placeholder': 'Address'
			}),
			'city': forms.TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'City'
			}),
			'state': forms.TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'State'
			}),
			'pin': forms.TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Pin Code'
			}),
		}