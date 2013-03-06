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
    else:
        form = DocumentForm()

    return render_to_response('index.html', 
        { 'form': DocumentForm()  },
        context_instance=RequestContext(request)
    )

def directory(request, path):

    import os
    try:
        if os.path.isdir(path):

            files = glob.glob(path + '/*.mzML')
            #tpl = loader.get_template('directory.html')
            #c = Context(request, {
            #    'flist': [{'name':f, 'type':t} for (f, d, t) in files if not d],
            #    'path': path } )
            c = RequestContext(request, {'flist': files, 'path': path})
            #return HttpResponse(tpl.render(c), 
            #    content_type="application/xhtml+xml" )
            #return render_to_response('directory.html', {
            #    context_instance=c )
            return c

        else:
            c = RequestContext(request)
            #return render_to_response('index.html',
            #    { 'form': DocumentForm(),  },
            #    context_instance=RequestContext(request)
            #)
            return c

    except ValueError: raise Http404
    except IOError: raise Http404

def waiting(request):

    return HttpResponse('Waiting for search')
