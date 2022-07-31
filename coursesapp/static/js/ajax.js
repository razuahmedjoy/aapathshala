$.ajax({
    type: "POST",
    url: "{% url 'createaccount' %}",
    data: {
        'name': name,
        'account': account,
        'charge': charge,
        'balance': balance,
        'csrfmiddlewaretoken': '{{csrf_token}}',
    },

    success: function (response) {
        $('#form').trigger("reset");
        $(".fa-spinner").toggleClass("d-none");
        $(".addWalletModal").toggleClass("show");
        swal(response, '', "success");
    },
    failure: function (e) {
        console.log(e)
    }


})