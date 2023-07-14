from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from . import models


class HomeView(SuccessMessageMixin, generic.CreateView):
    model = models.Transfer
    success_message = 'İsteğiniz başarı ile gönderilmiştir!'
    success_url = reverse_lazy('transfer:home')
    fields = (
        'email',
        'phone',
        'pax',
        'baggage',
        'rfrom',
        'rto',
        'date',
        'time',
    )
    template_name = 'transfer/home.django-html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        return {
            **context,
            'tours': models.Tour.objects.all()[:3]
        }


class AboutView(generic.TemplateView):
    template_name = 'transfer/about.django-html'


class OrderView(SuccessMessageMixin, generic.CreateView):
    model = models.TransferExtended
    fields = (
        'first_name',
        'last_name',
        'email',
        'phone',
        'iata',
        'iata_back',
        'pax',
        'pax_back',
        'baggage',
        'baggage_back',
        'rfrom',
        'rto',
        'date',
        'time',
        'date_back',
        'time_back',
        'comment',
        'back'
    )
    success_message = 'Talebiniz başarı ile Oluşturulmuştur!'
    success_url = reverse_lazy('transfer:order')
    template_name = 'transfer/order.django-html'

    def get_success_url(self):
        print(self.object.baggage)
        return (
            'https://api.whatsapp.com/send?phone=905060335639&text='
            'Merhaba! sahturizm.com.tr web-sitesi üzerinden transfer formunu doldurdum.%0A%0A' # noqa
            f'{self.request.scheme}://{self.request.get_host()}{self.object.get_absolute_url()}' # noqa
        )


class TourDetailView(generic.DetailView):
    model = models.Tour
    template_name = 'transfer/tour-detail.django-html'


class TourListView(generic.ListView):
    model = models.Tour
    template_name = 'transfer/tour-list.django-html'
    paginate_by = 9


class ContactView(SuccessMessageMixin, generic.CreateView):
    model = models.Request
    success_message = 'Formunuz başarı ile gönderilmiştir!'
    success_url = reverse_lazy('transfer:contact')
    template_name = 'transfer/contact.django-html'
    fields = (
        'full_name',
        'email',
        'description'
    )


class FAQListView(SuccessMessageMixin, generic.CreateView):
    template_name = 'transfer/faq-list.django-html'
    model = models.Request
    fields = (
        'full_name',
        'email',
        'description'
    )
    success_message = 'Mesajınız başarı ile gönderilmiştir!'
    success_url = reverse_lazy('transfer:faq')
    extra_context = {
        'faq_list': models.FAQ.objects
    }


class TransferExtendedCheckoutView(generic.DetailView):
    model = models.TransferExtended
    template_name = 'transfer/transfer-extended-checkout.django-html'
