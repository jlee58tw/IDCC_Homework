# -*- coding: utf-8 -*-

from django import forms

class DocumentForm(forms.Form):
	jobname = forms.CharField(max_length=20)
	file1 = forms.CharField( widget=forms.Textarea())
	file2 = forms.CharField( widget=forms.Textarea())
	file3 = forms.CharField( widget=forms.Textarea())