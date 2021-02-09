from Suffix import Suffix

# Nominal Verb Suffixes:
                                                                                        # Check Previous #Delete Previous (Bu termleri test edip düzenlemem gerek)

s1 = Suffix("-(y)ken",    ["ken"],                                                      "y",  False, True)
s2 = Suffix("-(y)muş",    ['mış', 'miş', 'muş', 'müş'],                                  "y",  True, True)
s3 = Suffix("-(y)sa",     ['sa', 'se'],                                                 "y",  False, True)
s4 = Suffix("-(y)du",     ['dı', 'di', 'du', 'dü', 'tı', 'ti', 'tu', 'tü'],             "y",  False, True)
s5 = Suffix("-casına",    ['casına', 'cesine', 'çasına', 'çesine'],                    None, False, False)
s6 = Suffix("-dur",       ['dır', 'dir', 'dur', 'dür', 'tır', 'tir', 'tur', 'tür'],    None, False, False)
s7 = Suffix("-nuz",       ['nız', 'niz', 'nuz', 'nüz'],                                None, False, False)
s8 = Suffix("-k",         ["k"],                                                       None, False, False)
s9 = Suffix("-n",         ["n"],                                                       None, False, False)
s10 = Suffix("-m",        ["m"],                                                       None, False, False)
s11 = Suffix("-lar",      ['lar', 'ler'],                                              None, False, False)
s12 = Suffix("-sunuz",    ['sınız', 'siniz', 'sunuz', 'sünüz'],                        None, False, False)
s13 = Suffix("-(y)uz",    ['ız', 'iz', 'uz', 'üz'],                                     "y", False,  True)
s14 = Suffix("-sun",      ['sın', 'sin', 'sun', 'sün'],                                None, False, False)
s15 = Suffix("-(y)um",    ['ım', 'im', 'um', 'üm'],                                      "y", False, True)
s16 = Suffix("-(ğ)inde",  ['inde', 'ünde', 'ında', 'unda'],                               "ğ", True, True)
s17 = Suffix("-sana",     ['sana', 'sene'],                                             None, False, False)


nominal_verb_suffix_list = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16,s17]


# Verb suffixes:

s1 = Suffix("-nuz",    ['nız', 'niz', 'nuz', 'nüz'],                                 None, False, False)
s2 = Suffix("-nuz",    ['ız', 'iz', 'uz', 'üz'],                                     None, False, False)
s3 = Suffix("-dum",    ['dım', 'dim', 'dum', 'düm', 'tım', 'tim', 'tum', 'tüm'],     None, False, False)
s4 = Suffix("-duk",    ['dık', 'dik', 'duk', 'dük', 'tık', 'tik', 'tuk', 'tük'],     None, False, False)
s5 = Suffix("-du",     ['dın', 'din', 'dun', 'dün', 'tın', 'tin', 'tun', 'tün'],     None, False, False)
s6 = Suffix("-du",     ['dı', 'di', 'du', 'dü', 'tı', 'ti', 'tu', 'tü'],             None, False, False)
s7 = Suffix("-muş",    ['mış', 'miş', 'muş', 'müş'],                                 None, False, False)
s8 = Suffix("-lar",    ['lar', 'ler'],                                               None, False, False)
s9 = Suffix("-acak",   ['acak', 'ecek', 'acağ', 'eceğ'],                               'y', False, True)
s10 = Suffix("-yor",   ['yor'],                                                      None, False, False)
s11 = Suffix("-im",    ['ım', 'im', 'um', 'üm'],                                       'y', False, True)
s12 = Suffix("-sın",   ['sın', 'sin', 'sun', 'sün'],                                 None, False, False)
s13 = Suffix("-tır",   ['tır', 'tir', 'dır', 'dir'],                                 None, False, False)
s14 = Suffix("-sı",    ['sı', 'si', 'su', 'sü'],                                     None, False, False)
s15 = Suffix("-ar",    ['ar', 'ur', 'ir', 'ır', 'ür', 'er'],                         None, False, False)
s16 = Suffix("-ı",     ['ı', 'i', 'u', 'ü'],                                         None, False, False)
s17 = Suffix("-mak",   ['mak', 'mek'],                                               None, False, False)
s18 = Suffix("-ma",    ['ma','me','mı','mi','mu','mü'],                              None, False, False)
s19 = Suffix("-malı",  ['malı', 'meli'],                                             None, False, False)
s20 = Suffix("-abil",  ['abil', 'ebil'],                                             None, False, False)
s21 = Suffix("-la",    ['la', 'le'],                                                 None, False, False)  #gözet - le - mek
s22 = Suffix("-a",     ['a', 'e'],                                                   None, False, False)  #bil - e - miyorum

# Fiil yapım ekleri: (s15, s22)


verb_suffix_list = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s20, s21, s22]


# Fiilden isim:

s1 = Suffix("-me",    ['me', 'ma'],                                 None, False, False)
s2 = Suffix("-ce",    ['ca', 'ce'],                                 None, False, False)

verb_to_noun_suffix_list = [s1,s2]