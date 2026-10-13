#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Felsefi Tost Makinesi
=====================
Bu kod gerçekten çalışır. Tostunuzu kızartırken varoluşsal kriz geçirir.
Çıkış yok. Veya var. Belki de tost zaten yanmıştır.
"""

import time
import random
import sys

# Gizli mesaj: c2l5YXNldCBpbGUgYWthcmsgb2xhYmlsaXIgbWEgY2F5IGRlbWxlbWVrIGd1emVsIGJpciBkaXkgZWxlbWVudGly
# (bu satırı okuyan herkes bir şey anlamış sayılır)

FELSEFELER = [
    "Tost, aslında ekmek ile ateş arasındaki diyalektik süreçtir.",
    "Neden kızartıyoruz? Çünkü çiğ olmak, evrenin temel hâlidir.",
    "Tereyağı, varoluşun yağlı yüzüdür.",
    "Bu tost, sana değil, sana bakan kişiye kızartılıyor.",
    "Isı, sadece moleküllerin dansıdır. Dans etmezsen yanarsın.",
    "Kahvaltı, günün ilk varoluşsal krizidir.",
    "Eğer tost konuşabilseydi, 'daha çok tereyağı' derdi.",
    "Zaman, tostun kızarmasını beklerken geçen süredir.",
    "Hiçbir tost, ikinci kez aynı kızarmışlıkta olamaz. (Herakleitos, muhtemelen)",
    "Yanmış tost, başarısız bir denemenin lezzetli sonucudur."
]

def tost_yap(derece=3, tereyagi=True):
    print("\n🍞 Felsefi Tost Makinesi başlatılıyor...")
    print("Uyari: Bu makine tostunuzu kızartırken sizi de kızartabilir. Felsefi olarak.\n")
    
    for i in range(1, 6):
        print(f"Kızartma seviyesi: {i}/5 ...")
        print(f"  → {random.choice(FELSEFELER)}")
        time.sleep(random.uniform(0.8, 2.2))
        if random.random() < 0.3:
            print("  (Makine bir an durdu. Hayatın anlamını düşünüyor.)")
            time.sleep(1.5)
    
    print("\n✅ Tost hazır!")
    if tereyagi:
        print("Tereyağı sürüldü. Ama tereyağı sürülürken eridi. Tıpkı hayallerimiz gibi.")
    else:
        print("Tereyağsız. Cesur bir tercih. Veya unuttun.")
    
    print(f"\nFinal felsefesi: {random.choice(FELSEFELER)}")
    print("\nAfiyet olsun. Veya olmasın. Seçim senin.\n")

if __name__ == "__main__":
    print("Felsefi Tost Makinesi v1.0 - Kayyum Onaylı")
    tost_yap()
    # Çıkış kodu: 0 (başarı) veya 42 (hayatın anlamı)
    sys.exit(0 if random.random() > 0.1 else 42)
