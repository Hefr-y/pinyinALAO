from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import json
from pypinyin import lazy_pinyin,Style
# from django.http import HttpResponse


# Opening JSON file(vocabulaire de l’examen HSK)
with open('static/hskLexique.json', 'r', encoding='utf-8') as f:
    # returns JSON object as a dictionary
    data = json.load(f)
    # Iterating through the json list
    hsk1_lex = data['hsk1']
    hsk2_lex = data['hsk2']
    hsk3_lex = data['hsk3']
    hsk4_lex = data['hsk4']

# Opening JSON file(Les initiales et les finales du pinyin)
with open('static/pinyin_Initials_finals.json', 'r') as f:
    # returns JSON object as a dictionary
    data = json.load(f)
    # Iterating through the json list
    pinyin_initials = data["initials"]
    pinyin_finals = data["finals"]

def get_py_details(hans):
    """Récupérer les informations pinyin correctes d'un seul caractère chinois
    par la librairie python --- pypinyin

    Args:
        hans {str}:
            un caractère chinois

    Returns:
        pyInfo {dict}:
            le caractère: les informations pinyin du caractère
    """
    pyDetails=[]
    for i in hans:
        form = i
        # la librairie python --- pypinyin
        pyAvecTone = lazy_pinyin(i,style=Style.TONE)[0]
        pySansTone = lazy_pinyin(i, style=Style.TONE3,neutral_tone_with_five=True)[0]
        spell = lazy_pinyin(i, style=Style.NORMAL)[0]
        tone = lazy_pinyin(i, style=Style.TONE3,neutral_tone_with_five=True)[0][-1]
        initial = lazy_pinyin(i, style=Style.INITIALS, strict=False)[0]
        final = lazy_pinyin(i, style=Style.FINALS,strict=False)[0]
        # combinaison d'informations sur le caractère et le pinyin
        pyInfo = {
            form:
            {
            "pySansTone":pySansTone,
            "pyAvecTone":pyAvecTone,
            "spell":spell,
            "tone":tone,
            "initial":initial,
            "final":final,
            }
        }
    return pyInfo


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
# 返回用户输入拼音的音调
def get_tone(pinyin):
    tone = pinyin[-1]
    if tone.isdigit():
        return tone
    else:
        return None
# 返回用户输入拼音的韵母
def get_yunmu(pinyin,shengmu):
    tone = get_tone(pinyin)
    yunmu = pinyin.lstrip(shengmu)
    if tone == None:
        if yunmu == '':
            return None
        else:
            return yunmu
    else:
        yunmu = yunmu.rstrip(tone)
        if yunmu == '':
            return None
        else:
            return yunmu


def Levenshtein_Distance(str1, str2):
    """Calculer la distance d'édition entre str1 et str2

    Args:
        str1{str}: N'importe quelle chaîne
        str1{str}: N'importe quelle chaîne

    Returns:
        sim{float}: similarité des chaînes.
                    La similarité est obtenue par 1/(1+x).
                    La variable {x} est la distance d'édition de Levenshtein.
    """
    matrix = [[ i + j for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]

    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            if(str1[i-1] == str2[j-1]):
                d = 0
            else:
                d = 1

            matrix[i][j] = min(matrix[i-1][j]+1, matrix[i][j-1]+1, matrix[i-1][j-1]+d)

    dist = matrix[len(str1)][len(str2)]
    sim = 1/(1+dist)
    sim = round(sim,3)
    return sim

# Create your views here.
def index(request):
    return render(request, "t_myapp/index.html")

def pinyin_dict(request):
    if request.method == 'GET':
        return render(request, "t_myapp/HSKpinyin/pinyinDict.html")

def pinyin_dict_affiche(request):
    if request.method == 'POST':
        query_dict = request.POST
        data = query_dict.dict()
        print(data)
        data_pinyin = {}
        for value in data.values():
            for hanzi in value:
                correctPinYinInfo = get_py_details(hanzi)
                pyinfo = correctPinYinInfo[hanzi] # 当前字的pinyin信息
                shengmu_correct = pyinfo.get("initial")
                yunmu_correct = pyinfo.get("final")
                tone_correct = pyinfo.get('tone')
                pyAvecTone = pyinfo.get('pyAvecTone')
                pySansTone = pyinfo.get('pySansTone')
                        # 处理空字符串
                if tone_correct == '':
                    tone_correct = None
                elif shengmu_correct == '':
                    shengmu_correct = None
                mot_pinyin = {
                    "pyAvecTone":pyAvecTone,
                    'pySansTone':pySansTone,
                    "initial_corr":shengmu_correct,
                    "final_corr":yunmu_correct,
                    "tone_corr":tone_correct
                }
                data_pinyin[hanzi] = mot_pinyin
        print(json.dumps(data_pinyin,ensure_ascii=False,indent=4))
        return render(request, "t_myapp/HSKpinyin/pinyinAffi.html", {"data":data_pinyin})



# hsk1的代码
def hsk1_view(request):
    if request.method == 'GET':
        data_hsk1_question = {"hsk1_lex":hsk1_lex}
        return render(request, "t_myapp/HSKpinyin/hsk1_view.html",data_hsk1_question)

def hsk1(request):
    query_dict = request.POST
    data = query_dict.dict()
    # print(query_dict,data)
    data_pinyin = {}
    for key, value in data.items():
        shengmu = get_shengmu(value)
        tone = get_tone(value)
        yunmu = get_yunmu(value, shengmu)
        correctPinYinInfo = get_py_details(key)
        pyinfo = correctPinYinInfo[key] # 当前字的pinyin信息
        shengmu_correct = pyinfo.get("initial")
        yunmu_correct = pyinfo.get("final")
        tone_correct = pyinfo.get('tone')
        pyAvecTone = pyinfo.get('pyAvecTone')
        pySansTone = pyinfo.get('pySansTone')
                # 处理空字符串
        if tone_correct == '':
            tone_correct = None
        elif shengmu_correct == '':
            shengmu_correct = None

        sim = Levenshtein_Distance(pySansTone, value)
        sim = "%.2f%%" % (sim * 100)
        mot_pinyin = {
            "pinyin_user":value,
            "initial_user":shengmu,
            "final_user":yunmu,
            "tone_user":tone,
            "pyAvecTone":pyAvecTone,
            'pySansTone':pySansTone,
            "initial_corr":shengmu_correct,
            "final_corr":yunmu_correct,
            "tone_corr":tone_correct,
            "similarite":sim
        }
        data_pinyin[key] = mot_pinyin # 每个单独字的拼音信息（用户输入和正确拼音）
        # print("每个字的正确拼音信息: ",correctPinYinInfo)
        # print("每个字的正确声母", shengmu_correct, "每个字的正确韵母", yunmu_correct, "每个字的正确音调", tone_correct)
        # print("用户输入的拼音:  "+key+":"+value,"用户输入拼音的声母: ", shengmu,"用户输入拼音的韵母: ", yunmu, "用户输入拼音的音调: ", tone)
    print(json.dumps(data_pinyin,ensure_ascii=False,indent=4))
    return render(request, "t_myapp/HSKpinyin/hsk1.html", {"data":data_pinyin})

# hsk2的代码
def hsk2_view(request):
    if request.method == 'GET':
        data_hsk2_question = {"hsk2_lex":hsk2_lex}
        return render(request, "t_myapp/HSKpinyin/hsk2_view.html",data_hsk2_question)

def hsk2(request):
    query_dict = request.POST
    data = query_dict.dict()
    # print(data)
    data_pinyin = {}
    for key, value in data.items():
        shengmu = get_shengmu(value)
        tone = get_tone(value)
        yunmu = get_yunmu(value, shengmu)
        correctPinYinInfo = get_py_details(key)
        pyinfo = correctPinYinInfo[key] # 当前字的pinyin信息
        shengmu_correct = pyinfo.get("initial")
        yunmu_correct = pyinfo.get("final")
        tone_correct = pyinfo.get('tone')
        pyAvecTone = pyinfo.get('pyAvecTone')
        pySansTone = pyinfo.get('pySansTone')
                # 处理空字符串
        if tone_correct == '':
            tone_correct = None
        elif shengmu_correct == '':
            shengmu_correct = None

        sim = Levenshtein_Distance(pySansTone, value)
        sim = "%.2f%%" % (sim * 100)
        mot_pinyin = {
            "pinyin_user":value,
            "initial_user":shengmu,
            "final_user":yunmu,
            "tone_user":tone,
            "pyAvecTone":pyAvecTone,
            'pySansTone':pySansTone,
            "initial_corr":shengmu_correct,
            "final_corr":yunmu_correct,
            "tone_corr":tone_correct,
            "similarite":sim
        }
        data_pinyin[key] = mot_pinyin # 每个单独字的拼音信息（用户输入和正确拼音）
        # print("每个字的正确拼音信息: ",correctPinYinInfo)
        # print("每个字的正确声母", shengmu_correct, "每个字的正确韵母", yunmu_correct, "每个字的正确音调", tone_correct)
        # print("用户输入的拼音:  "+key+":"+value,"用户输入拼音的声母: ", shengmu,"用户输入拼音的韵母: ", yunmu, "用户输入拼音的音调: ", tone)
    print(json.dumps(data_pinyin,ensure_ascii=False,indent=4))
    return render(request, "t_myapp/HSKpinyin/hsk2.html", {"data":data_pinyin})

#hsk3代码
def hsk3_view(request):
    if request.method == 'GET':
        data_hsk3_question = {"hsk3_lex":hsk3_lex}
        return render(request, "t_myapp/HSKpinyin/hsk3_view.html",data_hsk3_question)

def hsk3(request):
    query_dict = request.POST
    data = query_dict.dict()
    # print(data)
    data_pinyin = {}
    for key, value in data.items():
        shengmu = get_shengmu(value)
        tone = get_tone(value)
        yunmu = get_yunmu(value, shengmu)
        correctPinYinInfo = get_py_details(key)
        pyinfo = correctPinYinInfo[key] # 当前字的pinyin信息
        shengmu_correct = pyinfo.get("initial")
        yunmu_correct = pyinfo.get("final")
        tone_correct = pyinfo.get('tone')
        pyAvecTone = pyinfo.get('pyAvecTone')
        pySansTone = pyinfo.get('pySansTone')
                # 处理空字符串
        if tone_correct == '':
            tone_correct = None
        elif shengmu_correct == '':
            shengmu_correct = None

        sim = Levenshtein_Distance(pySansTone, value)
        sim = "%.2f%%" % (sim * 100)
        mot_pinyin = {
            "pinyin_user":value,
            "initial_user":shengmu,
            "final_user":yunmu,
            "tone_user":tone,
            "pyAvecTone":pyAvecTone,
            'pySansTone':pySansTone,
            "initial_corr":shengmu_correct,
            "final_corr":yunmu_correct,
            "tone_corr":tone_correct,
            "similarite":sim
        }
        data_pinyin[key] = mot_pinyin # 每个单独字的拼音信息（用户输入和正确拼音）
        # print("每个字的正确拼音信息: ",correctPinYinInfo)
        # print("每个字的正确声母", shengmu_correct, "每个字的正确韵母", yunmu_correct, "每个字的正确音调", tone_correct)
        # print("用户输入的拼音:  "+key+":"+value,"用户输入拼音的声母: ", shengmu,"用户输入拼音的韵母: ", yunmu, "用户输入拼音的音调: ", tone)
    print(json.dumps(data_pinyin,ensure_ascii=False,indent=4))
    return render(request, "t_myapp/HSKpinyin/hsk3.html", {"data":data_pinyin})



#hsk4代码
def hsk4_view(request):
    if request.method == 'GET':
        data_hsk4_question = {"hsk4_lex":hsk4_lex}
        return render(request, "t_myapp/HSKpinyin/hsk4_view.html",data_hsk4_question)

def hsk4(request):
    query_dict = request.POST
    data = query_dict.dict()
    # print(data)
    data_pinyin = {}
    for key, value in data.items():
        shengmu = get_shengmu(value)
        tone = get_tone(value)
        yunmu = get_yunmu(value, shengmu)
        correctPinYinInfo = get_py_details(key)
        pyinfo = correctPinYinInfo[key] # 当前字的pinyin信息
        shengmu_correct = pyinfo.get("initial")
        yunmu_correct = pyinfo.get("final")
        tone_correct = pyinfo.get('tone')
        pyAvecTone = pyinfo.get('pyAvecTone')
        pySansTone = pyinfo.get('pySansTone')
                # 处理空字符串
        if tone_correct == '':
            tone_correct = None
        elif shengmu_correct == '':
            shengmu_correct = None

        sim = Levenshtein_Distance(pySansTone, value)
        sim = "%.2f%%" % (sim * 100)
        mot_pinyin = {
            "pinyin_user":value,
            "initial_user":shengmu,
            "final_user":yunmu,
            "tone_user":tone,
            "pyAvecTone":pyAvecTone,
            'pySansTone':pySansTone,
            "initial_corr":shengmu_correct,
            "final_corr":yunmu_correct,
            "tone_corr":tone_correct,
            "similarite":sim
        }
        data_pinyin[key] = mot_pinyin
    print(json.dumps(data_pinyin,ensure_ascii=False,indent=4))
    return render(request, "t_myapp/HSKpinyin/hsk4.html", {"data":data_pinyin})