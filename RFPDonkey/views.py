from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.decorators.csrf import csrf_protect
from .models import system_user,product,product_type,customer,customer_type,partner,rfp,questions_and_answers
from .models import system_user_role
from django.urls import reverse
from django.db.models import Q
import logging
import math

items_per_page = 10
dict_user_roles ={"User":"USR","Administrator":"ADM","Other":"OTH"}

@csrf_protect
def test(request,a,b):
    
    print (a,b)
    template = loader.get_template('test.html')
    context = {
        "test":"test content",
    }
    return HttpResponse(template.render(context, request))

@csrf_protect
def login(request):
    request.session["AUTH"] = False
    template = loader.get_template("login.html")
    context = {
        "login":"true"
    }
    return HttpResponse(template.render(context, request))

@csrf_protect
def authenticate(request):
    user_name = request.POST.get("user_name")
    user_password = request.POST.get("user_password")
    user = system_user.objects.filter(user_name=user_name, user_password=user_password).count()
    if user>0:
        template = loader.get_template("main.html")    
        context = {
        "user_name":user_name,
        "user_password":user_password
        }
        request.session["AUTH"] = True
    else:
        request.session["AUTH"] = False
        template = loader.get_template("login.html") 
        context = {
            "login":"false"
        }
    return HttpResponse(template.render(context, request))

@csrf_protect
def product_new(request,c_page,t_pages):
    previous = False
    next = False
    start_page = (c_page-1)*items_per_page
    prod =  product.objects.all()[start_page:start_page+items_per_page]
    prod_types = product_type.objects.all()
    template = loader.get_template("product.html")
    t_pages = math.ceil(product.objects.all().count()/items_per_page)
    if (c_page>1):
        previous = True
    if (c_page<t_pages):
        next = True
    context = {
        "c_page":int(c_page),
        "t_pages":t_pages,
        "prev_pg":previous,
        "next_pg":next,
        "products":prod,
        "product_types":prod_types,
        "auth":  request.session["AUTH"]
    }
    return HttpResponse(template.render(context, request))

@csrf_protect
def product_add(request,c_page,t_pages):
    previous = False
    next = False
    start_page = (c_page-1)*items_per_page
    prod_active = False
    prod_name = request.POST.get("product_name")
    prod_description = request.POST.get("product_description")
    prod_types = product_type.objects.all()
    prod_type = product_type.objects.filter(product_type_name=request.POST.get("product_type")).first()
    if request.POST.get("product_active") == "on":
        prod_active = True
    p = product(product_name = prod_name,product_description = prod_description,product_type=prod_type,product_active=prod_active)
    p.save()
    prod =  product.objects.all()[start_page:start_page+items_per_page]
    template = loader.get_template("product.html")
    t_pages = math.ceil(product.objects.all().count()/items_per_page)
    if (c_page>1):
        previous = True
    if (c_page<t_pages):
        next = True
    context = {
        "c_page":int(c_page),
        "t_pages":t_pages,
        "prev_pg":previous,
        "next_pg":next,
        "products":prod,
        "product_types":prod_types,
         "auth":  request.session["AUTH"]
    }
    return HttpResponse(template.render(context, request))

@csrf_protect
def prod_search(request,c_page,t_pages):
    previous = False
    next = False
    start_page = (c_page-1)*items_per_page
    prod_active = False
    prod_name = request.POST.get("product_name")
    prod_description = request.POST.get("product_description")
    prod_type = product_type.objects.filter(product_type_name=request.POST.get("product_type")).first()
    print (f"product type: {prod_type}")
    prod =  product.objects.all()
    if request.POST.get("product_active") == "on":
        prod_active = True    
    prod = product.objects.filter(product_active=prod_active)
    if prod_name !="":
        prod = prod.filter (product_name__icontains=prod_name)
    if prod_description !="":
        prod = prod.filter (product_description__icontains=prod_description)
    if prod_type != None:
        prod = prod.filter(product_type = prod_types)
    prod =  prod[start_page:start_page+items_per_page]
    t_pages = math.ceil(product.objects.all().count()/items_per_page)
    if (c_page>1):
        previous = True
    if (c_page<t_pages):
        next = True
    prod_types = product_type.objects.all()
    template = loader.get_template("product.html")
    context = {
        "c_page":int(c_page),
        "t_pages":t_pages,
        "prev_pg":previous,
        "next_pg":next,
        "products":prod,
        "product_types":prod_types,
         "auth":  request.session["AUTH"]
    }
    return HttpResponse(template.render(context, request))

@csrf_protect
def product_update(request,c_page,t_pages):
    previous = False
    next = False
    start_page = (c_page-1)*items_per_page
    prod_active = False
    prod_id  = request.POST.get("product_id")
    prod_name = request.POST.get("product_name")
    prod_description = request.POST.get("product_description")
    prod_type = product_type.objects.first()
    if request.POST.get("product_active") == "on":
        prod_active = True
    prod = product.objects.filter(id=prod_id).all()
    prod.update( product_name = prod_name,
                product_description = prod_description,
                product_type= prod_type,
                product_active=prod_active)
    prod_types = product_type.objects.all()
    prod =  product.objects.all()[start_page:start_page+items_per_page]
    t_pages = math.ceil(product.objects.all().count()/items_per_page)
    template = loader.get_template("product.html")
    if (c_page>1):
        previous = True
    if (c_page<t_pages):
        next = True
    context = {
        "c_page":int(c_page),
        "t_pages":t_pages,
        "prev_pg":previous,
        "next_pg":next,
        "products":prod,
        "product_types":prod_types,
         "auth":  request.session["AUTH"]
    }
    return HttpResponse(template.render(context, request))

@csrf_protect
def product_delete(request,c_page,t_pages):
    previous = False
    next = False
    start_page = (c_page-1)*items_per_page
    prod_id  = request.POST.get("product_id")
    prod = product.objects.filter(id=prod_id).all()
    prod.delete()
    prod_types = product_type.objects.all()
    t_pages = math.ceil(product.objects.all().count()/items_per_page)
    prod =  product.objects.all()[start_page:start_page+items_per_page]
    template = loader.get_template("product.html")
    if (c_page>1):
        previous = True
    if (c_page<t_pages):
        next = True
    context = {
        "c_page":int(c_page),
        "t_pages":t_pages,
        "prev_pg":previous,
        "next_pg":next,
        "products":prod,
        "product_types":prod_types, 
         "auth":  request.session["AUTH"]
    }
    return HttpResponse(template.render(context, request))

@csrf_protect
def customer_new(request,c_page,t_pages):
    previous = False
    next = False
    start_page = (c_page-1)*items_per_page
    cust = customer.objects.all()[start_page:start_page+items_per_page]
    cust_types = customer_type.objects.all()
    template = loader.get_template("customer.html")
    t_pages = math.ceil(customer.objects.all().count()/items_per_page)
    if (c_page>1):
        previous = True
    if (c_page<t_pages):
        next = True
    context = {
        "c_page":int(c_page),
        "t_pages":t_pages,
        "prev_pg":previous,
        "next_pg":next,
        "customers":cust,
        "customer_types":cust_types,
         "auth":  request.session["AUTH"]
    }
    return HttpResponse(template.render(context, request))

@csrf_protect
def customer_add(request,c_page,t_pages):
    previous = False
    next = False
    start_page = (c_page-1)*items_per_page
    cust_name = request.POST.get("customer_name")
    cust_desctiption = request.POST.get("customer_description")
    cust_country = request.POST.get("customer_country")
    cust_type = customer_type.objects.filter(customer_type_name = request.POST.get("customer_type")).first()
    cust = customer(customer_name=cust_name, customer_description = cust_desctiption, customer_type=cust_type, customer_country = cust_country)
    cust.save()
    cust = customer.objects.all()[start_page:start_page+items_per_page]
    cust_types = customer_type.objects.all()
    t_pages = math.ceil(cust.count()/items_per_page)    
    if (c_page>1):
        previous = True
    if (c_page<t_pages):
        next = True
    template = loader.get_template("customer.html")
    context = {
        "c_page":int(c_page),
        "t_pages":t_pages,
        "prev_pg":previous,
        "next_pg":next,
        "customers":cust,
        "customer_types":cust_types, 
         "auth":  request.session["AUTH"]
    }
    return HttpResponse(template.render(context, request))

@csrf_protect
def customer_update(request,c_page, t_pages):
    previous = False
    next = False
    start_page = (c_page-1)*items_per_page
    cust_id = request.POST.get("customer_id")
    cust_name = request.POST.get("customer_name")
    cust_desctiption = request.POST.get("customer_description")
    cust_country = request.POST.get("customer_country")
    cust_type = customer_type.objects.filter(customer_type_name = request.POST.get("customer_type")).first()
    cust = customer.objects.filter(id=cust_id).all()
    cust.update(customer_name = cust_name,
        customer_description = cust_desctiption,
        customer_type = cust_type,
        customer_country = cust_country
    )
    cust = customer.objects.all()[start_page:start_page+items_per_page]
    cust_types = customer_type.objects.all()
    t_pages = math.ceil(cust.count()/items_per_page)    
    if (c_page>1):
        previous = True
    if (c_page<t_pages):
        next = True
    template = loader.get_template("customer.html")
    context = {
        "c_page":int(c_page),
        "t_pages":t_pages,
        "prev_pg":previous,
        "next_pg":next,
        "customers":cust,
        "customer_types":cust_types,
         "auth":  request.session["AUTH"]
    }
    return HttpResponse(template.render(context, request))

@csrf_protect
def customer_delete(request,c_page,t_pages):
    previous = False
    next = False
    start_page = (c_page-1)*items_per_page
    cust_id = request.POST.get("customer_id")   
    cust = customer.objects.filter(id=cust_id).all()
    cust.delete()
    cust = customer.objects.all()
    cust_types = customer_type.objects.all()
    template = loader.get_template("customer.html")
    t_pages = math.ceil(cust.count()/items_per_page) 
    cust = customer.objects.all()[start_page:start_page+items_per_page]   
    if (c_page>1):
        previous = True
    if (c_page<t_pages):
        next = True
    context = {
        "c_page":int(c_page),
        "t_pages":t_pages,
        "prev_pg":previous,
        "next_pg":next,
        "customers":cust,
        "customer_types":cust_types,
         "auth":  request.session["AUTH"]
    }
    return HttpResponse(template.render(context, request))

@csrf_protect
def customer_search(request,c_page,t_pages):
    previous = False
    next = False
    start_page = (c_page-1)*items_per_page
    cust_name = request.POST.get("customer_name")
    cust_desctiption = request.POST.get("customer_description")
    cust_country = request.POST.get("customer_country")
    cust_type = customer_type.objects.filter(customer_type_name = request.POST.get("customer_type")).first()
    cust = customer.objects.all()    
    if cust_type != None:
        cust =  customer.objects.filter(customer_type = cust_type)
    if cust_name !="":
        cust = cust.filter(customer_name__icontains=cust_name)
    if cust_desctiption !="":
        cust = cust.filter(customer_description__icontains=cust_desctiption)
    if cust_country !="":
        cust = cust.filter(customer_country__icontains = cust_country)
    t_pages = math.ceil(cust.count()/items_per_page) 
    cust = cust[start_page:start_page+items_per_page]
       
    if (c_page>1):
        previous = True
    if (c_page<t_pages):
        next = True
    cust_types = customer_type.objects.all()
    template = loader.get_template("customer.html")
    context = {
        "c_page":int(c_page),
        "t_pages":t_pages,
        "prev_pg":previous,
        "next_pg":next,
        "customers":cust,
        "customer_types":cust_types,
         "auth":  request.session["AUTH"]
    }
    return HttpResponse(template.render(context, request))

@csrf_protect
def partner_new(request,c_page,t_pages):
    previous = False
    next = False
    start_page = (c_page-1)*items_per_page
    part = partner.objects.all()[start_page:start_page+items_per_page]
    template = loader.get_template("partner.html")
    t_pages = math.ceil(partner.objects.all().count()/items_per_page)
    if (c_page>1):
        previous = True
    if (c_page<t_pages):
        next = True
    context = {
        "c_page":int(c_page),
        "t_pages":t_pages,
        "prev_pg":previous,
        "next_pg":next,
        "part":part,
         "auth":  request.session["AUTH"]
    }
    return HttpResponse(template.render(context, request))

@csrf_protect
def partner_add(request,c_page,t_pages):
    previous = False
    next = False
    start_page = (c_page-1)*items_per_page
    part_name  = request.POST.get("partner_name")
    part_description =request.POST.get ("partner_description")
    part_comment = request.POST.get("partner_comment")
    part = partner (partner_name=part_name, partner_description=part_description,partner_comment=part_comment)
    part.save()
    part = partner.objects.all()[start_page:start_page+items_per_page]
    t_pages = math.ceil(partner.objects.all().count()/items_per_page)
    template = loader.get_template("partner.html")
    if (c_page>1):
        previous = True
    if (c_page<t_pages):
        next = True
    context = {
        "c_page":int(c_page),
        "t_pages":t_pages,
        "prev_pg":previous,
        "next_pg":next,
        "part":part,
         "auth":  request.session["AUTH"]
    }
    return HttpResponse(template.render(context, request))
    
@csrf_protect
def partner_delete(request,c_page,t_pages):
    previous = False
    next = False
    start_page = (c_page-1)*items_per_page
    part_id = request.POST.get("partner_id")
    part = partner.objects.filter(id=part_id).all()
    part.delete()
    part = partner.objects.all()[start_page:start_page+items_per_page]
    t_pages = math.ceil(partner.objects.all().count()/items_per_page)
    template = loader.get_template("partner.html")
    if (c_page>1):
        previous = True
    if (c_page<t_pages):
        next = True
    context = {
        "c_page":int(c_page),
        "t_pages":t_pages,
        "prev_pg":previous,
        "next_pg":next,
        "part":part,
         "auth":  request.session["AUTH"]
    }
    return HttpResponse(template.render(context, request))

@csrf_protect
def partner_update(request,c_page,t_pages):
    previous = False
    next = False
    start_page = (c_page-1)*items_per_page
    part_name  = request.POST.get("partner_name")
    part_description =request.POST.get ("partner_description")
    part_comment = request.POST.get("partner_comment")
    part_id = request.POST.get("partner_id")
    part = partner.objects.filter(id=part_id).all()
    part.update (partner_name=part_name, partner_description=part_description,partner_comment=part_comment)
    part = partner.objects.all()[start_page:start_page+items_per_page]
    t_pages = math.ceil(partner.objects.all().count()/items_per_page)
    template = loader.get_template("partner.html")
    if (c_page>1):
        previous = True
    if (c_page<t_pages):
        next = True
    context = {
        "c_page":int(c_page),
        "t_pages":t_pages,
        "prev_pg":previous,
        "next_pg":next,
        "part":part,
         "auth":  request.session["AUTH"]
    }
    return HttpResponse(template.render(context, request))

@csrf_protect
def partner_search(request,c_page,t_pages):
    previous = False
    next = False
    start_page = (c_page-1)*items_per_page
    part_name  = request.POST.get("partner_name")
    part_description =request.POST.get ("partner_description")
    part_comment = request.POST.get("partner_comment")

    part = partner.objects.filter(partner_name__icontains=part_name, partner_description__icontains=part_description).all()
    t_pages = math.ceil(part.count()/items_per_page)
    part = part[start_page:start_page+items_per_page]
    template = loader.get_template("partner.html")
    if (c_page>1):
        previous = True
    if (c_page<t_pages):
        next = True
    context = {
    "c_page":int(c_page),
    "t_pages":t_pages,
    "prev_pg":previous,
    "next_pg":next,
    "part":part,
     "auth":  request.session["AUTH"]
    }
    return HttpResponse(template.render(context, request))

@csrf_protect
def rfp_new(request,c_page,t_pages):
    previous = False
    next = False
    start_page = (c_page-1)*items_per_page
    r =  rfp.objects.all()[start_page:start_page+items_per_page]
    cust = customer.objects.all()
    part = partner.objects.all()
    t_pages = math.ceil(rfp.objects.all().count()/items_per_page)
    tender = rfp.objects.all()[start_page:start_page+items_per_page]
    template = loader.get_template("rfp.html")
    
    if (c_page>1):
        previous = True
    if (c_page<t_pages):
        next = True
    context = {
        "c_page":int(c_page),
        "t_pages":t_pages,
        "prev_pg":previous,
        "next_pg":next,
        "rfps":tender,
        "customers":cust,
        "partners":part,
         "auth":  request.session["AUTH"]
    }
    return HttpResponse(template.render(context, request))

@csrf_protect
def rfp_add(request,c_page,t_pages):
    previous = False
    next = False
    start_page = (c_page-1)*items_per_page
    winloss = False
    submitted = False
    man_approved = False
    name = request.POST.get("rfp_name")
    description = request.POST.get("rfp_description")    
    value = request.POST.get("rfp_value")
    liabilities = request.POST.get("rfp_liabilities")
    comments = request.POST.get("rfp_comments")
    doc_folder = request.POST.get("rfp_documents_folder")
    if request.POST.get("rfp_winloss")  == "on":
        winloss = True
    if request.POST.get("rfp_submitted") == "on":
        submitted = True
    if request.POST.get("rfp_management_approved") =="on":
        man_approved = True
    cust = customer.objects.filter(customer_name=request.POST.get("rfp_customer_name")).first()
    part = partner.objects.filter(partner_name=request.POST.get("rfp_partner")).first()
    tender = rfp (rfp_name = name,
         rfp_description = description,
         rfp_customer = cust,
         rfp_winloss = winloss,
         rfp_value = value,
         rfp_liabilities = liabilities,
         rfp_comments = comments,
         rfp_partner = part,
         rfp_submitted = submitted,
         rfp_documents_folder = doc_folder,
         rfp_management_approved = man_approved)
    tender.save()
    t_pages = math.ceil(rfp.objects.all().count()/items_per_page)
    tender = rfp.objects.all()[start_page:start_page+items_per_page]
    cust = customer.objects.all()
    part = partner.objects.all()
    template = loader.get_template("rfp.html")
    if (c_page>1):
        previous = True
    if (c_page<t_pages):
        next = True
    context = {
        "c_page":int(c_page),
        "t_pages":t_pages,
        "prev_pg":previous,
        "next_pg":next,
        "rfps":tender,
        "customers":cust,
        "partners":part,
         "auth":  request.session["AUTH"],
    }
    return HttpResponse(template.render(context, request))

@csrf_protect
def rfp_delete(request,c_page,t_pages):
    previous = False
    next = False
    start_page = (c_page-1)*items_per_page
    rfp_id = request.POST.get("rfp_id")
    tender = rfp.objects.filter(id=rfp_id)
    tender.delete()
    cust = customer.objects.all()
    part = partner.objects.all()
    
    t_pages = math.ceil(rfp.objects.all().count()/items_per_page)
    tender = rfp.objects.all()[start_page:start_page+items_per_page]
    template = loader.get_template("rfp.html")
    if (c_page>1):
        previous = True
    if (c_page<t_pages):
        next = True
    context = {
        "c_page":int(c_page),
        "t_pages":t_pages,
        "prev_pg":previous,
        "next_pg":next,
        "rfps":tender,
        "customers":cust,
        "partners":part,
         "auth":  request.session["AUTH"],
    }
    return HttpResponse(template.render(context, request))

@csrf_protect
def rfp_update(request,c_page,t_pages):
    previous = False
    next = False
    start_page = (c_page-1)*items_per_page
    rfp_id = request.POST.get("rfp_id")
    tender = rfp.objects.filter(id=rfp_id)
    winloss = False
    submitted = False
    man_approved = False
    name = request.POST.get("rfp_name")
    description = request.POST.get("rfp_description")    
    value = request.POST.get("rfp_value")
    liabilities = request.POST.get("rfp_liabilities")
    comments = request.POST.get("rfp_comments")
    doc_folder = request.POST.get("rfp_documents_folder")
    if request.POST.get("rfp_winloss")  == "on":
        winloss = True
    if request.POST.get("rfp_submitted") == "on":
        submitted = True
    if request.POST.get("rfp_management_approved") =="on":
        man_approved = True
    cust = customer.objects.filter(customer_name=request.POST.get("rfp_customer_name")).first()
    part = partner.objects.filter(partner_name=request.POST.get("rfp_partner")).first()
    tender.update(
        rfp_name = name,
        rfp_description = description,
        rfp_customer = cust,
        rfp_winloss = winloss,
        rfp_value = value,
        rfp_liabilities = liabilities,
        rfp_comments = comments,
        rfp_partner = part,
        rfp_submitted = submitted,
        rfp_documents_folder = doc_folder,
        rfp_management_approved = man_approved)
    t_pages = math.ceil(rfp.objects.all().count()/items_per_page)
    tender = rfp.objects.all()[start_page:start_page+items_per_page]
    cust = customer.objects.all()
    part = partner.objects.all()
    template = loader.get_template("rfp.html")
    if (c_page>1):
        previous = True
    if (c_page<t_pages):
        next = True
    context = {
        "c_page":int(c_page),
        "t_pages":t_pages,
        "prev_pg":previous,
        "next_pg":next,
        "rfps":tender,
        "customers":cust,
        "partners":part,
         "auth":  request.session["AUTH"],
    }
    return HttpResponse(template.render(context, request))

@csrf_protect
def rfp_search(request,c_page,t_pages):
    previous = False
    next = False
    start_page = (c_page-1)*items_per_page
    winloss = False
    submitted = False
    man_approved = False
    name = request.POST.get("rfp_name")
    description = request.POST.get("rfp_description")    
    value = request.POST.get("rfp_value")
    liabilities = request.POST.get("rfp_liabilities")
    comments = request.POST.get("rfp_comments")
    doc_folder = request.POST.get("rfp_documents_folder")
    cust_field = customer.objects.filter(customer_name=request.POST.get("rfp_customer_name")).first()
    part_field = partner.objects.filter(partner_name = request.POST.get("rfp_partner")).first()
    if request.POST.get("rfp_winloss")  == "on":
        winloss = True
    if request.POST.get("rfp_submitted") == "on":
        submitted = True
    if request.POST.get("rfp_management_approved") =="on":
        man_approved = True
    tender = rfp.objects.all()    
    if name !="":
        tender = tender.filter(rfp_name__icontains = name)    
    if description != "":
        tender = tender.filter(rfp_description__icontains = description)
    if cust_field != None:         
        tender = tender.filter(rfp_customer = cust_field)

    # The search on value shall be greather than !!!     
    if value !="":
        tender = tender.filter(rfp_value__icontains = value)
    if liabilities !="":
        tender = tender.filter(rfp_liabilities__icontains = liabilities)
    if comments !="":
        tender = tender.filter(rfp_comments__icontains = comments)
    if part_field != None:
        tender = tender.filter(rfp_partner =part_field)
    if doc_folder != "":
        tender = tender.filter(rfp_document_folder__icontains = doc_folder)
    if winloss:
        tender = tender.filter(rfp_winloss = True)
    if man_approved:
        tender = tender.filter(rfp_management_approved = True)
    if submitted:
        tendet = tender.filter(rfp_submitted = True)
    t_pages = math.ceil(tender.all().count()/items_per_page)
    tender = tender[start_page:start_page+items_per_page]
    cust = customer.objects.all()
    part = partner.objects.all()
    template = loader.get_template("rfp.html")
    if (c_page>1):
        previous = True
    if (c_page<t_pages):
        next = True
    context = {
        "c_page":int(c_page),
        "t_pages":t_pages,
        "prev_pg":previous,
        "next_pg":next,
        "rfps":tender,
        "customers":cust,
        "partners":part,
         "auth":  request.session["AUTH"],
    }
    return HttpResponse(template.render(context, request))

@csrf_protect
def qa_new(request,c_page,t_pages):
    previous = False
    next = False
    start_page = (c_page-1)*items_per_page
    qa =  questions_and_answers.objects.all()[start_page:start_page+items_per_page]
    prod = product.objects.all()
    tender = rfp.objects.all()
    qa = questions_and_answers.objects.all()[start_page:start_page+items_per_page]
    template = loader.get_template("questions_answer.html")
    t_pages = math.ceil(questions_and_answers.objects.all().count()/items_per_page)
    if (c_page>1):
        previous = True
    if (c_page<t_pages):
        next = True
    context = {
        "c_page":int(c_page),
        "t_pages":t_pages,
        "prev_pg":previous,
        "next_pg":next,
        "qas":qa,
        "products":prod,
        "tenders":tender,
         "auth":  request.session["AUTH"],
    }
    return HttpResponse(template.render(context, request))

@csrf_protect
def qa_add(request,c_page,t_pages):
    previous = False
    next = False
    start_page = (c_page-1)*items_per_page
    question = request.POST.get("qa_question")
    answer = request. POST.get("qa_answer")
    tender = rfp.objects.filter(rfp_name = request.POST.get("qa_tender")).first()
    prod = product.objects.filter(product_name = request.POST.get("qa_product")).first()
    qa=questions_and_answers(qa_question = question,
                             qa_answer = answer,
                             qa_rfp= tender,
                             qa_product = prod)
    qa.save()
    prod = product.objects.all()
    tender = rfp.objects.all()
    t_pages = math.ceil(questions_and_answers.objects.all().count()/items_per_page)
    qa = questions_and_answers.objects.all()[start_page:start_page+items_per_page]
    template = loader.get_template("questions_answer.html")
    if (c_page>1):
        previous = True
    if (c_page<t_pages):
        next = True

    context = {
        "c_page":int(c_page),
        "t_pages":t_pages,
        "prev_pg":previous,
        "next_pg":next,
        "qas":qa,
        "products":prod,
        "tenders":tender,
         "auth":  request.session["AUTH"],
    }
    return HttpResponse(template.render(context, request))

@csrf_protect
def qa_update(request,c_page,t_pages):
    previous = False
    next = False
    start_page = (c_page-1)*items_per_page
    qa_id = request.POST.get("qa_id")
    question = request.POST.get("qa_question")
    answer = request. POST.get("qa_answer")
    tender = rfp.objects.filter(rfp_name = request.POST.get("qa_tender")).first()
    prod = product.objects.filter(product_name = request.POST.get("qa_product")).first()
    qa = questions_and_answers.objects.filter(id=qa_id)
    qa.update(qa_question = question,
              qa_answer = answer,
              qa_product = prod,
              qa_rfp = tender)
    prod = product.objects.all()
    tender = rfp.objects.all()
    t_pages = math.ceil(questions_and_answers.objects.all().count()/items_per_page)
    qa = questions_and_answers.objects.all()[start_page:start_page+items_per_page]
    template = loader.get_template("questions_answer.html")
    if (c_page>1):
        previous = True
    if (c_page<t_pages):
        next = True
    context = {
        "c_page":int(c_page),
        "t_pages":t_pages,
        "prev_pg":previous,
        "next_pg":next,
        "qas":qa,
        "products":prod,
        "tenders":tender,
        "auth":  request.session["AUTH"],
    }
    return HttpResponse(template.render(context, request))
    
@csrf_protect
def qa_delete(request,c_page,t_pages):
    previous = False
    next = False
    start_page = (c_page-1)*items_per_page
    qa_id=request.POST.get("qa_id")
    q = questions_and_answers.objects.filter(id=qa_id).first()
    q.delete()
    prod = product.objects.all()
    tender = rfp.objects.all()
    t_pages = math.ceil(questions_and_answers.objects.all().count()/items_per_page)
    qa = questions_and_answers.objects.all()[start_page:start_page+items_per_page]
    template = loader.get_template("questions_answer.html")
    if (c_page>1):
        previous = True
    if (c_page<t_pages):
        next = True
    context = {
    "c_page":int(c_page),
    "t_pages":t_pages,
    "prev_pg":previous,
    "next_pg":next,
    "qas":qa,
    "products":prod,
    "tenders":tender,
     "auth":  request.session["AUTH"],
    }
    return HttpResponse(template.render(context, request))


@csrf_protect
def qa_search(request,c_page,t_pages):
    previous = False
    next = False
    start_page = (c_page-1)*items_per_page
    question = request.POST.get("qa_question")
    answer = request. POST.get("qa_answer")
    tender = rfp.objects.filter(rfp_name = request.POST.get("qa_tender")).first()
    prod = product.objects.filter(product_name = request.POST.get("qa_product")).first()
    qa = questions_and_answers.objects.all()
    if question !="":
        qa =qa.filter(qa_question__icontains = question)
    if answer !="":
        qa = qa.filter(qa_answer__icontains = answer)
    if tender != None:
        qa = qa.filter(qa_rfp=tender)
    if prod !=None:
        qa = qa.filter(qa_product=prod)
    prod = product.objects.all()
    tender = rfp.objects.all()
    t_pages = math.ceil(questions_and_answers.objects.all().count()/items_per_page)
    template = loader.get_template("questions_answer.html")
    # print (f"start page:{start_page} end:{start_page+items_per_page}")
    qa = qa[start_page:start_page+items_per_page]
    if (c_page>1):
        previous = True
    if (c_page<t_pages):
        next = True

    context = {
        "c_page":int(c_page),
        "t_pages":t_pages,
        "prev_pg":previous,
        "next_pg":next,
        "qas":qa,
        "products":prod,
        "tenders":tender,
         "auth":  request.session["AUTH"],
    }
    return HttpResponse(template.render(context, request))

@csrf_protect
def product_type_lookup(request,p_type):
    if p_type!='none':            
        sel_prod_type = product_type.objects.filter(product_type_name = p_type).first()
        context = {
        "id":sel_prod_type.id,
        "prod_name":sel_prod_type.product_type_name,
        "prod_desc":sel_prod_type.product_type_description
    }
    else:
        context = {
            "id":"",
            "prod_name":"",
            "prod_desc":"",
             "auth":  request.session["AUTH"],
        }
    template = loader.get_template("product_type_lookup.html")
    return HttpResponse(template.render(context, request))

@csrf_protect
def product_type_add(request):    
    prod_name = request.POST.get("product_type_name")
    prod_description = request.POST.get("product_type_description")
    pt = product_type(product_type_name=prod_name, product_type_description=prod_description)
    pt.save()
    sel_prod_type = product_type.objects.filter(product_type_name = prod_name).first()
    template = loader.get_template("product_type_lookup.html")
    context = {
        "id":sel_prod_type.id,
        "prod_name":sel_prod_type.product_type_name,
        "prod_desc":sel_prod_type.product_type_description,
         "auth":  request.session["AUTH"],
    }
    return HttpResponse(template.render(context, request))

@csrf_protect
def product_type_del(request):
    prod_id = request.POST.get("id")
    pt = product_type.objects.filter(id=prod_id)
    pt.delete()
    context = {
            "id":"",
            "prod_name":"",
            "prod_desc":"",
             "auth":  request.session["AUTH"],
        }
    template = loader.get_template("product_type_lookup.html")
    return HttpResponse(template.render(context, request))

@csrf_protect
def product_type_update(request):
    print ("product type update")
    prod_id = request.POST.get("id")
    # prod_name = request.POST.get("prduct_type_name")
    prod_desc = request.POST.get("product_type_description")
    pt = product_type.objects.filter(id=prod_id)
    pt.update(product_type_description=prod_desc)
    sel_prod_type = product_type.objects.filter(id = prod_id).first()
    template = loader.get_template("product_type_lookup.html")
    context = {
        "id":sel_prod_type.id,
        "prod_name":sel_prod_type.product_type_name,
        "prod_desc":sel_prod_type.product_type_description,
         "auth":  request.session["AUTH"],
    }
    return HttpResponse(template.render(context, request))

@csrf_protect
def customer_type_lookup(request,c_type):
    if c_type != 'none':
        sel_cust_type = customer_type.objects.filter(customer_type_name=c_type).first()
        context = {
            "id":sel_cust_type.id,
            "cust_name":sel_cust_type.customer_type_name,
            "cust_desc":sel_cust_type.customer_type_description,
             "auth":  request.session["AUTH"],
        }
    else:
        context = {
            "id":"",
            "cust_name":"",
            "cust_desc":"",
             "auth":  request.session["AUTH"],
        }
    template = loader.get_template("CUSTOMER_type_lookup.html")
    return HttpResponse(template.render(context, request))

@csrf_protect
def customer_type_add(request):
    cust_name = request.POST.get("customer_type_name")
    cust_description = request.POST.get("customer_type_description")
    ct = customer_type(customer_type_name=cust_name, customer_type_description=cust_description)
    ct.save()
    sel_cust_type = customer_type.objects.filter(customer_type_name = cust_name).first()
    template = loader.get_template("customer_type_lookup.html")
    context = {
        "id":sel_cust_type.id,
        "cust_name":sel_cust_type.customer_type_name,
        "cust_desc":sel_cust_type.customer_type_description,
         "auth":  request.session["AUTH"],
    }
    return HttpResponse(template.render(context, request))

@csrf_protect
def customer_type_del(request):
    cust_id = request.POST.get("id")
    ct = customer_type.objects.filter(id=cust_id)
    ct.delete()
    context = {
            "id":"",
            "cust_name":"",
            "cust_desc":"",
             "auth":  request.session["AUTH"],
        }
    template = loader.get_template("CUSTOMER_type_lookup.html")
    return HttpResponse(template.render(context, request))

@csrf_protect
def customer_type_update(request):
    cust_id = request.POST.get("id")
    cust_name = request.POST.get("customer_type_name")
    cust_description = request.POST.get("customer_type_description")
    ct = customer_type.objects.filter(id=cust_id)
    ct.update(customer_type_name=cust_name, customer_type_description=cust_description)
    ct = customer_type.objects.filter(id=cust_id).first()
    context = {
            "id":ct.id,
            "cust_name":ct.customer_type_name,
            "cust_desc":ct.customer_type_description,
             "auth":  request.session["AUTH"],
        }
    template = loader.get_template("CUSTOMER_type_lookup.html")
    return HttpResponse(template.render(context, request))

@csrf_protect
def partner_lookup(request,p_type):
    if p_type!='none':            
        sel_partner = partner.objects.filter(partner_name = p_type).first()
        context = {
        "id":sel_partner.id,
        "part_name":sel_partner.partner_name,
        "part_desc":sel_partner.partner_description,
        "part_comment":sel_partner.partner_comment,
         "auth":  request.session["AUTH"],
    }
    else:
        context = {
            "id":"",
            "part_name":"",
            "part_desc":"",
            "part_comment":"",
             "auth":  request.session["AUTH"],
        }
    template = loader.get_template("partner_lookup.html")
    return HttpResponse(template.render(context, request))

@csrf_protect
def partner_lu_add(request):
    part_name = request.POST.get("partner_name")
    part_description = request.POST.get("partner_description")
    part_comment = request.POST.get("partner_comment")
    p = partner(partner_name=part_name, partner_description=part_description,partner_comment=part_comment)
    p.save()
    sel_partner = partner.objects.filter(partner_name = part_name).first()
    template = loader.get_template("partner_lookup.html")
    context = {
        "id":sel_partner.id,
        "part_name":sel_partner.partner_name,
        "part_desc":sel_partner.partner_description,
        "part_comment":sel_partner.partner_comment,
         "auth":  request.session["AUTH"],
    }
    return HttpResponse(template.render(context, request))

@csrf_protect
def partner_lu_del(request):
    part_id = request.POST.get("id")
    p = partner.objects.filter(id=part_id).first()
    p.delete()
    template = loader.get_template("partner_lookup.html")
    context = {
        "id":"",
        "part_name":"",
        "part_desc":"",
        "part_comment":"",
         "auth":  request.session["AUTH"],
    }
    return HttpResponse(template.render(context, request))

@csrf_protect
def partner_lu_update(request):
    part_id = request.POST.get("id")
    part_name = request.POST.get("partner_name")
    part_description = request.POST.get("partner_description")
    part_comment = request.POST.get("partner_comment")
    p = partner.objects.filter(id=part_id)
    p.update(partner_name=part_name,partner_description=part_description, partner_comment=part_comment)
    p = partner.objects.filter(id=part_id).first()
    template = loader.get_template("partner_lookup.html")
    context = {
        "id":p.id,
        "part_name":p.partner_name,
        "part_desc":p.partner_description,
        "part_comment":p.partner_comment,
         "auth":  request.session["AUTH"],
    }
    return HttpResponse(template.render(context, request))

@csrf_protect
def tender_lookup(request,t):
    if t !='none':
        t = rfp.objects.filter(rfp_name=t).first()
        context = {
            "id":t.id,
            "rfp_name":t.rfp_name,
            "rfp_description":t.rfp_description,
            "rfp_customer":t.rfp_customer,
            "rfp_winloss":t.rfp_winloss,
            "rfp_value":t.rfp_value,
            "rfp_liabilities":t.rfp_liabilities,
            "rfp_comments":t.rfp_comments,
            "rfp_partner":t.rfp_partner,
            "rfp_submitted":t.rfp_submitted,
            "rfp_documents_folder":t.rfp_documents_folder,
            "rfp_management_approved":t.rfp_management_approved,
             "auth":  request.session["AUTH"],
        }
    else:
        context = {
            "id":"",
            "rfp_name":"",
            "rfp_description":"",
            "rfp_customer":"",
            "rfp_winloss":"",
            "rfp_value":"",
            "rfp_liabilities":"",
            "rfp_comments":"",
            "rfp_partner":"",
            "rfp_submitted":"",
            "rfp_documents_folder":"",
            "rfp_management_approved":"",
             "auth":  request.session["AUTH"],
        }
    template = loader.get_template("tender_lookup.html")
    return HttpResponse(template.render(context, request))
@csrf_protect
def tender_lu_add(request):
    t_id = request.POST.get("id")
    t_name = request.POST.get("rfp_name")
    t_description = request.POST.get("rfp_description")
    t_customer = request.POST.get("rfp_customer")
    t_winloss = request.POST.get("rfp_winloss")
    t_value = request.POST.get("rfp_value")
    t_liability = request.POST.get("rfp_liabilities")
    t_comments = request.POST.get("rfp_comments")
    t_partner = request.POST.get("rfp_partner")
    t_submitted = request.POST.geT("rfp_submitted")
    t_documents_folder = request.POST.get("rfp_documents_folder")
    t_management_approved = request.POST.get("rfp_management_approved")
    t = rfp(rfp_name = t_name, 
            rfp_description=t_description,
            rfp_customer = t_customer,
            rfp_winloss=t_winloss,
            rfp_value = t_value,
            rfp_liabilities = t_liability,
            rfp_comments = t_comments,
            rfp_partner = t_partner,
            rfp_submitted = t_submitted,
            rfp_documents_folder = t_documents_folder,
            rfp_management_approved =t_management_approved
            )
    t.save()
    t = rfp.objects.filter(rfp_name=t_name).first()
    context = {
            "id":t.id,
            "rfp_name":t.rfp_name,
            "rfp_description":t.rfp_description,
            "rfp_customer":t.rfp_customer,
            "rfp_winloss":t.rfp_winloss,
            "rfp_value":t.rfp_value,
            "rfp_liabilities":t.rfp_liabilities,
            "rfp_comments":t.rfp_comments,
            "rfp_partner":t.rfp_partner,
            "rfp_submitted":t.rfp_submitted,
            "rfp_documents_folder":t.rfp_documents_folder,
            "rfp_management_approved":t.rfp_management_approved,
             "auth":  request.session["AUTH"],
        }
    template = loader.get_template("tender_lookup.html")
    return HttpResponse(template.render(context, request))    

@csrf_protect
def product_lookup(request,p):
    if p != 'none':
        sel_prod = product.objects.filter(product_name = p).first()
        context = {
                "product_name":sel_prod.product_name,
                "product_description":sel_prod.product_description,
                "product_type":sel_prod.product_type,
                "product_active":sel_prod.product_active,
                 "auth":  request.session["AUTH"],
        }
    else:
        context= {
            "product_name":"",
            "product_description":"",
            "product_type":"",
            "product_active":"",
             "auth":  request.session["AUTH"],
        }
    template = loader.get_template("product_lookup.html")
    return HttpResponse(template.render(context, request))

@csrf_protect
def user_new(request,c_page,t_pages):
    previous = False
    next = False
    start_page = (c_page-1)*items_per_page
    u =  system_user.objects.all()[start_page:start_page+items_per_page]
    roles = system_user_role.objects.all()
    
    template = loader.get_template("users.html")
    t_pages = math.ceil(system_user.objects.all().count()/items_per_page)
    if (c_page>1):
        previous = True
    if (c_page<t_pages):
        next = True
    context = {
        "c_page":int(c_page),
        "t_pages":t_pages,
        "prev_pg":previous,
        "next_pg":next,
        "users":u,
        "user_roles":roles,
         "auth":  request.session["AUTH"],
    
    }
    return HttpResponse(template.render(context, request))

@csrf_protect
def user_search(request):
    role = ""
    s_user_name = request.POST.get("user_name")
    s_user_first_name = request.POST.get("user_first_name")
    s_user_last_name = request.POST.get("user_last_name")
    s_user_role = system_user_role.objects.filter(role_name = request.POST.get("user_role")).first()
    user = system_user.objects.all()   
    
    if s_user_name != None:
        user =  system_user.objects.filter(user_name__icontains =s_user_name)
    if s_user_first_name !="":
        user = user.filter(user_first_name__icontains=s_user_first_name)
    if s_user_last_name !="":
        user = user.filter(user_last_name__icontains=s_user_last_name)
    if s_user_role != None:    
        role = s_user_role.role_name
    if role !="":
        user = user.filter(user_role = role)
        
    user_roles = system_user_role.objects.all()
    template = loader.get_template("users.html")
    context = {
        "users":user,
        "user_roles":user_roles,
         "auth":  request.session["AUTH"],
    }
    return HttpResponse(template.render(context, request))

@csrf_protect
def user_delete(request):
    s_user_id = request.POST.get("user_id")
    user = system_user.objects.filter(id=s_user_id).first()
    user.delete
    user_roles = system_user_role.objects.all()
    template = loader.get_template("users.html")
    user = system_user.objects.all()
    context = {
        "users":user,
        "user_roles":user_roles,
         "auth":  request.session["AUTH"],
    }
    return HttpResponse(template.render(context, request))

@csrf_protect
def user_add(request):
    s_user_name = request.POST.get("user_name")
    s_user_password = request.POST.get("user_password")
    s_user_first_name = request.POST.get("user_first_name")
    s_user_last_name = request.POST.get("user_last_name")
    s_user_role = request.POST.getlist("user_role")
    s_user_role_str =""
    for r in s_user_role:
        s_user_role_str = s_user_role_str + r +";"
    s_user_role_str = s_user_role_str[:-1]
    
    user = system_user(user_name=s_user_name, user_password=s_user_password,user_first_name=s_user_first_name, user_last_name = s_user_last_name, user_role=s_user_role_str)
    user.save()
    user_roles = system_user_role.objects.all()
    template = loader.get_template("users.html")
    user = system_user.objects.all()
    context = {
        "users":user,
        "user_roles":user_roles,
         "auth":  request.session["AUTH"],
    }
    return HttpResponse(template.render(context, request))

@csrf_protect
def user_update(request):
    s_id = request.POST.get("user_id")
    s_user_name = request.POST.get("user_name")
    s_user_password = request.POST.get("user_password")
    s_user_first_name = request.POST.get("user_first_name")
    s_user_last_name = request.POST.get("user_last_name")
    
    s_user_role = request.POST.getlist("user_role")
    s_user_role_str =""
    for r in s_user_role:
        s_user_role_str = s_user_role_str + r +";"
    s_user_role_str = s_user_role_str[:-1]
    
    
    
    user = system_user.objects.filter(id=s_id)
    user.update(
        user_name = s_user_name,
        user_password = s_user_password,
        user_first_name = s_user_first_name,
        user_last_name = s_user_last_name, 
        user_role = s_user_role_str
    )
    user_roles = system_user_role.objects.all()
    template = loader.get_template("users.html")
    user = system_user.objects.all()
    context = {
        "users":user,
        "user_roles":user_roles,
         "auth":  request.session["AUTH"],
    }
    return HttpResponse(template.render(context, request))
