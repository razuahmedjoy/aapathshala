from django.shortcuts import HttpResponse,render, redirect,HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.contrib import messages
from coursesapp.forms.join_us_form import JoinUsForm
from coursesapp.models.joinus import JoinUs


def join_us(request):
    join_form = JoinUsForm()

    if request.method == "POST":
        full_name = request.POST.get("full_name")
        hsc_batch = request.POST.get("hsc_batch")
        department = request.POST.get("department")
        your_aap_roll = request.POST.get("your_aap_roll")
        currently_studying = request.POST.get('currently_studying')
        your_free_time = request.POST.get("your_free_time")
        contact = request.POST.get("contact")
        why_choose_us = request.POST.get("why_choose_us")

        join_request = JoinUs(full_name=full_name, hsc_batch=hsc_batch,
        department=department, your_aap_roll=your_aap_roll, currently_studying=currently_studying, your_free_time=your_free_time,
        contact=contact, why_choose_us=why_choose_us
        )

        try:
            join_request.full_clean()
            join_request.save()
            messages.add_message(
                    request, messages.SUCCESS, "তোমার ফর্মটি সফল ভাবে সাবমিট হয়েছে, আগ্রহ প্রকাশের জন্য ধন্যবাদ। আমরা তোমার আগ্রহ যাচাই করে তোমার সাথে যোগাযোগ করব, ইনশাল্লাহ।"
                )
        except ValidationError:
            messages.add_message(
                    request, messages.ERROR, "তোমার ফর্মটি সাবমিট হয়নি, সঠিক তথ্য দিয়ে আবার চেষ্টা করো । "
                )



    return render(request,'coursesapp/join.html', {
        "join_form" : join_form,
    })



def write_question(request, id):
    if request.method == "POST":
        book = Books.objects.get(id=id)
        user = Customers.objects.get(user=request.user)
        q = request.POST.get("question")
        question = QnA(book=book, user=user, question=q)

        try:
            question.full_clean()
            question.save()
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

        except ValidationError:
            pass