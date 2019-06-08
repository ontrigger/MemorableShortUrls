from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from urlshort.forms import URLShortenForm
from urlshort.models import ShortUrl
from urlshort.util import gen_absolute_link, gen_shortlink, urldigest


def index(request):
    if request.method == 'POST':
        form = URLShortenForm(request.POST)
        # TODO: handle errors
        if form.is_valid():
            url = form.cleaned_data['url']

            urlhash = urldigest(url)
            shortlink_obj = ShortUrl.objects.filter(urlhash=urlhash)

            # return link if it exists
            if shortlink_obj.exists():
                return render(request, 'index.html', {
                    'form': URLShortenForm(),
                    'shortlink': gen_absolute_link(
                        request,
                        shortlink_obj.get().shortlink
                    )
                })

            new_link = ShortUrl(
                url=url,
                urlhash=urlhash,
                shortlink=gen_shortlink(url)
            )
            new_link.save()

            return render(request, 'index.html', {
                'shortlink': gen_absolute_link(request, new_link.shortlink),
                'form': URLShortenForm(),
            })

    return render(request, 'index.html', {
        'form': URLShortenForm()
    })


def redirect(request, shortlink):
    link = get_object_or_404(ShortUrl, shortlink__exact=shortlink)

    return HttpResponseRedirect(link.url)
