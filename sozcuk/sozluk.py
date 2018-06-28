import sqlite3 as sql


def add(ask,ans):
    db = sql.connect("data.db")
    db.text_factory = str
    im = db.cursor()
    im.execute('INSERT INTO sozluk VALUES (?,?)', (ask,ans))
    db.commit()
    db.close()


def control(aranan):
    dizi = []
    db = sql.connect("data.db")
    db.text_factory = str
    im = db.cursor()
    im.execute("SELECT cevap FROM sozluk WHERE soru = ?", [aranan])
    veriler = im.fetchall()
    db.close()
    if veriler:
        for i in veriler:
            dizi.append(i[0])
        return dizi
    else:
        return None
