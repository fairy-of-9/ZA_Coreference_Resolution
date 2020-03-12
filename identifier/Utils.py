import json, os

def document_iter(c):
    for d in c["document"]:
        yield c["id"], d


def sentence_iter(c):
    for cid, d in document_iter(c):
        for s in d["sentence"]:
            yield cid, d["id"], s


# 모든 document iteration - corpus id, gold document, pred document
def document_iter_zip(d1, d2):
    for gd, pd in zip(d1["document"], d2["document"]):
        yield d1["id"], gd, pd


# 모든 sentence iteration - corpus id, documenti id, gold sentence, pred sentence
def sentence_iter_zip(d1, d2):
    for corpus_id, gd, pd in document_iter_zip(d1, d2):
        for gs, ps in zip(gd["sentence"], pd["sentence"]):
            yield corpus_id, gd["id"], gs, ps


# 디렉토리 안의 모든 파일에 대한 absolute path return
def diriter(path):
    for p, d, f in os.walk(path):
        for ff in f:
            yield "/".join([p, ff])


def readfile(path):
    with open(path, encoding="utf-8") as f:
        for line in f.readlines():
            yield line.strip()


# 파일 이름으로 json 로드(utf-8만 해당)
def jsonload(fname, encoding="utf-8"):
    with open(fname, encoding=encoding) as f:
        j = json.load(f)
    return j


# json 개체를 파일이름으로 깔끔하게 저장
def jsondump(j, fname):
    with open(fname, "w", encoding="UTF8") as f:
        json.dump(j, f, ensure_ascii=False, indent="\t")