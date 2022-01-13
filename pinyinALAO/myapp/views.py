from typing import final
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import json, spacy, random
from pypinyin import lazy_pinyin,Style
# from django.http import HttpResponse

# Opening JSON file 词汇文件
with open('static/hskLexique.json', 'r', encoding='utf-8') as f:
    # returns JSON object as a dictionary
    data = json.load(f)
    # Iterating through the json list
    hsk1_lex = data['hsk1']
    hsk2_lex = data['hsk2']
    hsk3_lex = data['hsk3']

# Opening JSON file 声母韵母文件
with open('static/pinyin_Initials_finals.json', 'r') as f:
    # returns JSON object as a dictionary
    data = json.load(f)
    # Iterating through the json list
    pinyin_initials = data["initials"]
    pinyin_finals = data["finals"]

# 返回单个汉字的正确拼音信息
def get_py_details(hans):
    pyDetails=[]
    for i in hans:
        form = i
        pyAvecTone = lazy_pinyin(i,style=Style.TONE)[0]
        spell = lazy_pinyin(i, style=Style.NORMAL)[0]
        tone = lazy_pinyin(i, style=Style.TONE3,neutral_tone_with_five=True)[0][-1]
        initial = lazy_pinyin(i, style=Style.INITIALS, strict=False)[0]
        final = lazy_pinyin(i, style=Style.FINALS)[0]
        pyInfo = {
            form:
            {
            "pyAvecTone":pyAvecTone,
            "spell":spell,
            "tone":tone,
            "initial":initial,
            "final":final,
            }
        }
        pyDetails.append(pyInfo)
    return pyDetails

# 返回用户输入拼音的声母
def get_shengmu(pinyin):
    # 获取声母
    if len(pinyin) == 0:
        return None
    elif len(pinyin) == 1:
        if pinyin in pinyin_initials:
            return pinyin
        else:
            return None
    else:
        if pinyin[:2] in pinyin_initials:
            return pinyin[:2]
        elif pinyin[:1] in pinyin_initials:
            return pinyin[:1]
        else:
            return None
# 返回用户输入拼音的韵母
def get_yunmu(pinyin,shengmu):
    yunmu = pinyin.lstrip(shengmu)
    return yunmu

# Create your views here.
def index(request):
    return render(request, "t_myapp/index.html")

def pinyin_dict(request):
    return render(request, "t_myapp/HSKpinyin/pinyinDict.html/")

def hsk1_view(request):
    print(hsk1_lex)

    if request.method == 'GET':
        return render(request, "t_myapp/HSKpinyin/hsk1.html",{'hsk1_lex':hsk1_lex})
    elif request.method == 'POST':
        query_dict = request.POST
        data = query_dict.dict()
        print(data)
        for key, value in data.items():
            shengmu = get_shengmu(value)
            yunmu = get_yunmu(value, shengmu)
            correctPinYinInfo = get_py_details(key)
            print("每个字的正确拼音信息: ",correctPinYinInfo)
            print("用户输入的拼音:  "+key+":"+value,"用户输入拼音的声母: ", shengmu,"用户输入拼音的韵母: ", yunmu)

        return JsonResponse(data)
        # data= get_py_details(hsk1_mot)
        # jsdata = json.dumps(data,indent=4,ensure_ascii=False)
        # print(jsdata)
        # pinyin_hsk1_input = request.POST.getlist('pinyin_hsk1')
        # pinyin_correct = lazy_pinyin(hsk1_mot, style=Style.TONE3)
        # print(pinyin_hsk1_input)
        # return JsonResponse({"正确的汉字拼音":data})

def hsk2(request):
    return render(request, "t_myapp/HSKpinyin/hsk2.html")

def hsk3(request):
    return render(request, "t_myapp/HSKpinyin/hsk3.html")



def analyze_spacy(request):
    return render(request, "t_myapp/analyse_spacy.html")




def test_get_post(request):
    if request.method == 'GET':
        print(request.GET)
        print(request.GET.getlist('a'))
        print(request.GET.get('c','no c'))
        # return HttpResponse(POST_FORM)

    elif request.method == 'POST':
        print('uname is', request.POST['uname'])
        return HttpResponse('post is ok')

    else:
        pass


    return HttpResponse('--test get post is ok--')



def test_request(request):
    print('path info is', request.path_info)
    print('method is', request.method)
    print('querystring is', request.GET)
    print('full path is', request.get_full_path())

    return HttpResponse('test request ok')


def variables(request):
    nom = "Édouard"
    hobbies = ["ping pong", "lecture", "musique"]

    return render(request, 't_myapp/variables.html', {"nom":nom, "hobbies":hobbies})

# def boucle(request):
#     membres = [
#         {"nom":"Dupond", "prenom":"Sophie"},
#         {"nom":"Hache", "prenom":"Anne"},
#         {"nom":"Von Ergstadt", "prenom":"Émile"},
#         {"nom":"Dupuit", "prenom":"Alex"},
#     ]
#     return render(request, 't_myapp/boucle.html',{"membres":membres})

def boucle(request):
    bigmac = {
            "Énergie": "504kcal",
            "Matières grasses": "25g",
            "Dont acides gras saturés": "9,2g",
            "Sucres": "8,2g",
            "Sel": "2,2g"
    }
    membres = [
        {"nom":"Dupond", "prenom":"Sophie"},
        {"nom":"Hache", "prenom":"Anne"},
        {"nom":"Von Ergstadt", "prenom":"Émile"},
        {"nom":"Dupuit", "prenom":"Alex"},
    ]

    return render(request, 't_myapp/boucle.html',{"bigmac":bigmac,"membres":membres})

def analyze(request):
    colis = json.loads(request.body)
    text = colis['inText']
    print("À analyser :",text)





def analyze(request):
    colis = json.loads(request.body)
    text = colis['inText']
    print("À analyser :",text)

    nlp = spacy.load("zh_core_web_sm")

    output = nlp(text)
    rep = []
    for token in output:
        rep.append((token.text, token.pos_))

    return JsonResponse({ "reponse":rep })

