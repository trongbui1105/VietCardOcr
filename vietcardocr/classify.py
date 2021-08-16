# -*- coding: utf-8 -*-
from vietcardocr.studentCard_class import *
from vietcardocr.idCard_class import *
from vietcardocr.drivingLicense_class import *
from difflib import SequenceMatcher
import re
import unidecode as uni
import vietcardocr.config as config
import os


def searchDataFromFile(data, file):
    maxx = 0.8
    res = ""
    data = uni.unidecode(data)
    with open(file, "r", encoding='utf8') as infile:
        for i in infile.readlines():
            ratio = SequenceMatcher(a=uni.unidecode(i.upper()), b=data.upper()).ratio()
            if ratio > maxx:
                maxx = ratio
                res = i
    return res.strip()


def searchData(words, string):
    maxx = 0
    ratio = SequenceMatcher(a=words, b=string).ratio()
    if ratio > maxx:
        maxx = ratio
    return maxx


def searchLastName(data):
    listAccent = {
        "AN",
        "ANH",
        "AU",
        "CAI",
        "CHUNG",
        "CO",
        "CONG",
        "CU",
        "DAU",
        "DOAN",
        "DONG",
        "DUONG",
        "GIANG",
        "HA",
        "HAN",
        "KHA",
        "LA",
        "LIEU",
        "LO",
        "MA",
        "MAU",
        "ONG",
        "PHI",
        "PHU",
        "QUANG",
        "TONG",
        "TRINH",
        "UNG",
        "KIEU",
        "LY",
        "NGO",
        "CHU",
        "LAI",
        "KWAK",
    }

    temp = ""
    name = data.split()
    lastName = uni.unidecode(name[0].upper())
    maxx = 0
    file = os.path.join(config.txt_dir, 'text/lastName.txt')
    if lastName not in listAccent:
        with open(file, "r", encoding='utf8') as infile:
            for i in infile.readlines():
                ratio = SequenceMatcher(a=uni.unidecode(i.upper()), b=lastName).ratio()
                if ratio > maxx:
                    maxx = ratio
                    temp = i.upper()
        data = data.replace(name[0], temp.strip())
    return data.strip()


def searchAddressOfDL(data, file):
    res = ""
    maxx = 0.8
    data = uni.unidecode(data.upper())
    with open(file, "r", encoding='utf8') as infile:
        for i in infile.readlines():
            if len(data.replace(" ", "")) <= len(i.strip().replace(" ", "")) + 4:
                ratio = SequenceMatcher(
                    a=uni.unidecode(i.upper()), b=data.upper()
                ).ratio()
                if ratio > maxx:
                    maxx = ratio
                    res = i
    return res.strip()

def searchMajor(data, file):
    res = ""
    maxx = 0.7
    data = uni.unidecode(data.upper())
    with open(file, "r", encoding='utf8') as infile:
        for i in infile.readlines():
            if len(data.replace(" ", "")) <= len(i.strip().replace(" ", "")) + 8:
                ratio = SequenceMatcher(
                    a=uni.unidecode(i.upper()), b=data.upper()
                ).ratio()
                if ratio > maxx:
                    maxx = ratio
                    res = i
    return res.strip()

def searchFaculty(data, file):
    res = ""
    maxx = 0.7
    data = uni.unidecode(data.upper())
    with open(file, "r", encoding='utf8') as infile:
        for i in infile.readlines():
            if len(data.replace(" ", "")) <= len(i.strip().replace(" ", "")) + 8:
                ratio = SequenceMatcher(
                    a=uni.unidecode(i.upper()), b=data.upper()
                ).ratio()
                if ratio > maxx:
                    maxx = ratio
                    res = i
    return res.strip()


def extractDate(data):
    match = re.findall(r"\d{2}/\d{2}/\d{4}", data)
    res = ""
    if match:
        res = match[0]
        return res
    else:
        return False


def extractIdOfDL(data):
    match = re.findall(r"\d{12}", data)
    res = ""
    if match:
        res = match[0]
        return res
    else:
        return False


def extractNation(data):
    maxx = 0.7
    res = ""
    file = os.path.join(config.txt_dir, 'text/nation.txt')
    with open(file, "r", encoding='utf8') as infile:
        for i in infile.readlines():
            ratio = SequenceMatcher(a=i.upper(), b=data.upper()).ratio()
            if ratio > maxx:
                res = i
    return res.upper().strip()


def extractIdStudent(data):
    match = re.findall(r"\w/*\d{7}", data)
    res = ""
    if match:
        res = match[0]
        return res
    else:
        return False


def classify(results):
    for item in results:
        if searchData(item, "CĂN CƯỚC CÔNG DÂN") >= 0.5:
            return 1
        if (
            searchData(item, "GIẤY PHÉP LÁI XE") >= 0.5
            or searchData(item, "DRIVER'S LICENSE") >= 0.5
        ):
            return 2
        if searchData(item, "STUDENT") >= 0.5 or searchData(item, "SINH VIÊN") >= 0.5:
            return 3


def output_proc_idCard(results):
    id = ""
    name = ""
    birth = ""
    nationality = ""
    sex = ""
    hometown = ""
    address = ""
    expires = ""

    for i in range(len(results)):
        if results[i].isdigit():
            id = results[i]
            for j in range(i, i + 3):
                if results[j].isupper():
                    name = results[j]

        if extractDate(results[i]) and birth == "":
            birth = extractDate(results[i])

        if searchData(results[i], "Quốc tịch") >= 0.5:
            nationality = results[i][11:]

        if searchData(results[i], "Giới tính") >= 0.5:
            sex = results[i][10:]

        if "Quê quán" in results[i] or "Quê quân" in results[i]:
            hometown = results[i][10:]
            if ":" not in results[i + 1]:
                hometown += ", " + results[i + 1]
            if ":" not in results[i + 1] and ":" not in results[i + 2]:
                hometown += ", " + results[i + 2]

        if "Nơi thường" in results[i]:
            address = results[i][16:]
            if ":" not in results[i + 1]:
                address += ", " + results[i + 1]
            if ":" not in results[i + 1] and ":" not in results[i + 2]:
                address += ", " + results[i + 2]

        if extractDate(results[i]) and extractDate(results[i]) is not birth:
            expires = extractDate(results[i])

    if searchLastName(name):
        name = searchLastName(name)

    if extractNation(nationality):
        nationality = extractNation(nationality)
    
    file = os.path.join(config.txt_dir, 'text/address.txt')
    if searchDataFromFile(hometown, file):
        hometown = searchDataFromFile(hometown, file)

    for i in range(0, 2):
        if address[i] == ',':
            address = address.replace(address[i], "", 1)


    idCard = IdCard(id, name, birth, nationality, sex, hometown, address, expires)
    return idCard


def output_proc_drivingLicense(results):
    idOfDL = ""
    nameOfDL = " "
    birthOfDL = ""
    nationalityOfDL = ""
    addressOfDL = ""
    classOfDL = ""
    expires = "Không thời hạn"
    checkAddress = False

    for i in range(2, len(results)):
        if extractIdOfDL(results[i]):
            idOfDL = extractIdOfDL(results[i])
            for j in range(i, i + 3):
                if results[j].isupper():
                    nameOfDL = results[j]

        if extractDate(results[i]) and birthOfDL == "":
            birthOfDL = extractDate(results[i])

        if extractNation(results[i]) and nationalityOfDL == "":
            nationalityOfDL = extractNation(results[i])

        if "Nơi cư" in results[i] or "Address" in results[i]:
            if "Nationality" in results[i - 1]:
                addressOfDL = results[i + 1]
                # checkAddress = True
            else:
                addressOfDL = results[i - 1] + ", " + results[i + 1]
            if "năm" in results[i + 1]:
                addressOfDL = results[i - 1]
                # checkAddress = True
            if nationalityOfDL in results[i - 1].upper():
                addressOfDL = results[i + 1]
                # checkAddress = True
            if "/" in results[i + 2] or "date" in results[i + 2] or "year" in results[i + 2] or "month" in results[i+2]:
                # checkAddress = True
                continue
            else:
                addressOfDL += ", " + results[i + 2]

        if "Hạng" in results[i]:
            classOfDL = results[i][11:]

        if extractDate(results[i]) and extractDate(results[i]) is not birthOfDL:
            expires = extractDate(results[i])
    if searchLastName(nameOfDL):
        nameOfDL = searchLastName(nameOfDL)

    file = os.path.join(config.txt_dir, 'text/address.txt')
    if searchAddressOfDL(addressOfDL, file):
        addressOfDL = searchAddressOfDL(addressOfDL, file)

    drivingLicense = DrivingLicense(
        idOfDL, nameOfDL, birthOfDL, nationalityOfDL, addressOfDL, classOfDL, expires
    )
    return drivingLicense


def output_proc_studentCard(results):
    id = ""
    name = ""
    major = ""
    faculty = ""
    course = ""

    for i in range(len(results)):
        if (
            "SINH VIÊN" in results[i]
            or "sinh viên" in results[i]
            or "STUDENT" in results[i]
        ):
            faculty = results[i - 1]
            for j in range(i, i + 2):
                if results[j].upper():
                    name = results[j]
        if "SINH VIÊN" in results[i]:
            if searchLastName(name):
                name = searchLastName(name)
        if extractIdStudent(results[i]):
            id = extractIdStudent(results[i])
        if "Ngành" in results[i] or "Nganh" in results[i] or "Major" in results[i]:
            major = results[i][6:]
        if "Khóa học" in results[i] or "Khoa học" in results[i]:
            course = results[i][9:]
        if "Course" in results[i]:
            course = results[i][7:]

    file = os.path.join(config.txt_dir, 'text/major.txt')
    if searchMajor(major, file):
        major = searchMajor(major, file)
    
    file1 = os.path.join(config.txt_dir, 'text/faculty.txt')
    if searchFaculty(faculty, file1):
        faculty = searchFaculty(faculty, file1)

    studentCard = StudentCard(name, id, major, faculty, course)
    return studentCard
