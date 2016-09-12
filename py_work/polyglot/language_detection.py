# -*- encoding: utf-8 -*-
from polyglot.detect import Detector
arabic_text = u"""
أفاد مصدر امني في قيادة عمليات صلاح الدين في العراق بأن " القوات الامنية تتوقف لليوم
الثالث على التوالي عن التقدم الى داخل مدينة تكريت بسبب
انتشار قناصي التنظيم الذي يطلق على نفسه اسم "الدولة الاسلامية" والعبوات الناسفة
والمنازل المفخخة والانتحاريين، فضلا عن ان القوات الامنية تنتظر وصول تعزيزات اضافية ".
"""
detector = Detector(arabic_text)
print detector.language


mixed_text = u"""
China (simplified Chinese: 中国; traditional Chinese: 中國),
officially the People's Republic of China (PRC), is a sovereign state located in East Asia.
"""
for language in Detector(mixed_text).languages:
    print language

'''
detector = Detector("pizza")
print(detector)

print(Detector("4"))
'''
from polyglot.utils import pretty_list
print(pretty_list(Detector.supported_languages()))
