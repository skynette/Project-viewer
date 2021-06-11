from django.shortcuts import render, redirect
from .models import Payment
from django.conf import settings
from django.contrib import messages


def initiate_payment(request):
	# if not request.user.is_authenticated:
	# 	return redirect('/')
	if request.method == "POST":
		print(request.POST)
		amount = request.POST['amount']
		email = request.POST['email']

		pk = settings.PAYSTACK_PUBLIC_KEY

		payment = Payment.objects.create(
			amount=amount, email=email, user=request.user)
		payment.save()

		context = {
			'payment': payment,
			'field_values': request.POST,
			'paystack_pub_key': pk,
			'amount_value': payment.amount_value(),
		}
		return render(request, 'make-payment.html', context)

	return render(request, 'initiate-payments.html')


def verify_payment(request, ref):
	payment = Payment.objects.get(ref=ref)
	verified = payment.verify_payment()
	ver = Payment.objects.filter(user=request.user)
	for txn in ver:
		if txn.verified:
			print(request.user.username, "Has successfully")
	if verified:
		messages.success(request, "verified successfully")
	return redirect('/')
