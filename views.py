import glob
import os
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.template import Context, Template, loader
from django.http import Http404, HttpResponse


from quameteratlas.models import Document
from quameteratlas.forms import DocumentForm

def index(request):

    if request.method == 'POST': # If the form has been submitted...
        form = DocumentForm(request.POST) # A form bound to the POST data    
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            c = directory(request, request.POST['filepath'])
            return render_to_response('directory.html',
                context_instance=c)

    return render_to_response('index.html', 
        { 'form': DocumentForm()  },
        context_instance=RequestContext(request)
    )

def directory(request, path):

    import os
    try:
        if os.path.isdir(path):

            files = glob.glob(path + '/*.mzML')
            if (len(files) == 0):
                files = ['no mzML files found']
            c = RequestContext(request, {'flist': files, 'path': path})
            return c

        else:
            c = RequestContext(request, {'flist': ['directory does not exist'], 'path': path})
            return c

    except ValueError: raise Http404
    except IOError: raise Http404

def waiting(request):

    return HttpResponse('Waiting for search')
