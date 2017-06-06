# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from new_app.models import messa
from new_app.models import genes
from new_app.models import seqe
from django.template import Context
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import data_helper


# Create your views here.
def search(request):
    return render_to_response('search.html')

def searchby(request, a, conten):
    content = str(conten)
    if content=="":
        return render_to_response('search.html')
    elif content.find("!")!=-1 or content.find("@")!=-1!=-1 or content.find("$")!=-1 or content.find("%")!=-1 or content.find("^")!=-1 or content.find("*")!=-1 or content.find(",")!=-1 or content.find("/")!=-1:
        return render_to_response('search_error.html')
    else:
        if a=="1":
            lists1 = messa.objects.filter(Q(ids__icontains=content)|Q(alias__icontains=content))
            ran = "lncRNA"
        if a=="2":
            lists1 = messa.objects.filter(Q(snp__icontains=content))
            ran = "SNP"
        if a=="3":
            lists1 = messa.objects.filter(Q(dise__icontains=content))
            ran = "Disease"
        if len(lists1)==0:
            return render_to_response('search_none.html')
        else:
            if len(lists1)>20:
                p = Paginator(lists1, 20)
                page = request.GET.get('page')
                page = str(page)
                print page
                try:
                    lists = p.page(page)
                except PageNotAnInteger:
                    page = "1"
                    lists = p.page(1)
                except EmptyPage:
                    page = str(p.num_pages)
                    lists = p.page(p.num_pages)
                num_pages = p.num_pages
                print "num_pages", num_pages
                asa = []
                if int(page)>3 and int(page)<num_pages-2:
                    asa = ["1", str(int(page)-2), str(int(page)-1), page, str(int(page)+1), str(int(page)+2), str(num_pages)]
                if page=="1":
                    asa = ["1", "2", "3", str(num_pages)]
                if page=="2":
                    asa = ["1", "2", "3", "4", str(num_pages)]
                if page=="3":
                    asa = ["1", "2", "3", "4", "5", str(num_pages)]
                if page==str(num_pages):
                    asa = [1, num_pages-2, num_pages-1, num_pages]
                if page==str(num_pages-1):
                    asa = [1, num_pages-3, num_pages-2, num_pages-1, num_pages]
                if page==str(num_pages-2):
                    asa = [1, num_pages-4, num_pages-3, num_pages-2, num_pages-1, num_pages]
                print asa
                c = {"lists":lists, "asa":asa, "ran":ran, "contents":content}
                return render(request, 'result.html', c)
            else:
                c = {"lists":lists1, "ran":ran, "contents":content}
                return render_to_response('result_single.html', c)

def searchfor(request, dise):
    ran = "Disease"
    content = dise
    objects = messa.objects.filter(dise=dise)
    p = Paginator(objects, 20)
    page = request.GET.get('page')
    page = str(page)
    print page
    try:
        lists = p.page(page)
    except PageNotAnInteger:
        page = "1"
        lists = p.page(1)
    except EmptyPage:
        page = str(p.num_pages)
        lists = p.page(p.num_pages)
    num_pages = p.num_pages
    print "num_pages", num_pages
    asa = []
    if int(page)>3 and int(page)<num_pages-2:
        asa = ["1", str(int(page)-2), str(int(page)-1), page, str(int(page)+1), str(int(page)+2), str(num_pages)]
    if page=="1":
        asa = ["1", "2", "3", str(num_pages)]
    if page=="2":
        asa = ["1", "2", "3", "4", str(num_pages)]
    if page=="3":
        asa = ["1", "2", "3", "4", "5", str(num_pages)]
    if page==str(num_pages):
        asa = [1, num_pages-2, num_pages-1, num_pages]
    if page==str(num_pages-1):
        asa = [1, num_pages-3, num_pages-2, num_pages-1, num_pages]
    if page==str(num_pages-2):
        asa = [1, num_pages-4, num_pages-3, num_pages-2, num_pages-1, num_pages]
    print asa
    c = {"lists":lists, "asa":asa, "ran":ran, "contents":content}
    return render(request, 'result.html', c)

def result(request, ids):
    if request.method=="POST":
        lists = messa.objects.filter(ids=ids)
        list0 = seqe.objects.filter(ids=ids)
        for line in list0:
            strs = line.expre
        list_expre = strs.split()
        list_expre = [float(i) for i in list_expre]
        list_gen = genes.objects.filter(ids=ids)
        c = {"lists":lists, "list0":list0, "list_gen":list_gen, "list_expre":list_expre}
        return render_to_response('detail.html', c)

def home(request):
    return render_to_response('home.html')

def browse(request, a, b):
    n = 67445/int(b)+1
    start = (int(a)-1)*int(b)
    enddd = int(a)*int(b)+1
    previous = int(a)-1
    nexttt = int(a)+1
    if enddd>67445:
        enddd = 67446
    print start, enddd
    if int(a)>3 and int(a)<n-2:
        asa = ["1", str(int(a)-2), str(int(a)-1), str(int(a)), str(int(a)+1), str(int(a)+2), str(n)]
    if int(a)==1:
        asa = [int(a), int(a)+1, int(a)+2, str(n)]
    if int(a)==2:
        asa = [int(a)-1, int(a), int(a)+1, int(a)+2, str(n)]
    if int(a)==3:
        asa = [str(int(a)-2), str(int(a)-1), str(int(a)), str(int(a)+1), str(int(a)+2), str(n)]
    if int(a)==n:
        asa = ["1", int(a)-2, int(a)-1, int(a)]
    if int(a)==n-1:
        asa = ["1", int(a)-2, int(a)-1, int(a), int(a)+1]
    if int(a)==n-2:
        asa = ["1", str(int(a)-2), str(int(a)-1), str(int(a)), str(int(a)+1), str(int(a)+2)]
    lists = messa.objects.filter(number__gt=start, number__lt=enddd)
    if int(a)<n and int(a)>1:
        c = {"lists":lists, "asa":asa, "a":int(a), "b":int(b), "previous":[previous], "nexttt":[nexttt]}
    if int(a)==1:
        c = {"lists":lists, "asa":asa, "a":int(a), "b":int(b), "previous":[], "nexttt":[nexttt]}
    if int(a)==n:
        c = {"lists":lists, "asa":asa, "a":int(a), "b":int(b), "previous":[previous], "nexttt":[]}
    return render_to_response('browse.html', c)

def download(request):
    return render_to_response('download.html')

def help(request):
    return render_to_response('help.html')

def test(request):
    return render_to_response('test.html')

def data(request, filename):
    response = HttpResponse()
    response['Content-Disposition'] = 'attachment;filename=downfile.txt'
    full_path = filename
    if os.path.exists(full_path):
        response['Content-Length'] = os.path.getsize(full_path)
        content = open(full_path, 'rb').read()
        response.write(content)
        return response
    else:
        return HttpResponse(u'cannot find the file')

def savegene(request, ids):
    response = HttpResponse()
    response['Content-Disposition'] = 'attachment;filename='+ids+'_gene.txt'
    list_gen = genes.objects.filter(ids=ids)
    f = open("downfile/file", 'w')
    for i in list_gen:
        f.write(i.gene+"\t"+i.gen_sco+"\n")
    f.close()
    full_path = "downfile/file"
    response['Content-Length'] = os.path.getsize(full_path)
    content = open(full_path, 'rb').read()
    response.write(content)
    os.system("rm downfile/file")
    return response

def saveexpre(request, ids):
    response = HttpResponse()
    response['Content-Disposition'] = 'attachment;filename='+ids+'_gene.zip'
    list0 = seqe.objects.filter(ids=ids)
    for line in list0:
        strs = line.expre
    list_expre = strs.split()
    f = open("downfile/file", 'w')
    f.write(list_expre)
    f.close()
    full_path = "downfile/file"
    response['Content-Length'] = os.path.getsize(full_path)
    content = open(full_path, 'rb').read()
    response.write(content)
    os.system("rm downfile/file")
    return response

def savedise(request, ids):
    response = HttpResponse()
    response['Content-Disposition'] = 'attachment;filename='+ids+'_disease.txt'
    lists = messa.objects.filter(ids=ids)
    f = open("downfile/file", 'w')
    for i in lists:
        f.write(i.dise+"\t"+i.dis_sco+"\n")
    f.close()
    full_path = "downfile/file"
    response['Content-Length'] = os.path.getsize(full_path)
    content = open(full_path, 'rb').read()
    response.write(content)
    os.system("rm downfile/file")
    return response

def showpic(request, ids, dise):
    return render_to_response('help.html')
