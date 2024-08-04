from django import forms
class ApplyCouponForm(forms.Form):
    coupon_code = forms.CharField(max_length = 20,required = True)