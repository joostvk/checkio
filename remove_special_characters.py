

import unicodedata
def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')
   
   
strip_accents(u"préfèrent") == u"preferent"
strip_accents(u"loài trăn lớn") == u"loai tran lon"