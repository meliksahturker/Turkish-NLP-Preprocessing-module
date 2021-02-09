from Suffix import Suffix

# We need to check these suffixes in an order (given by #x)
# Inflectional Suffixes (Çekim ekleri):

                                                                    #Check Previous #Delete Previous (Bu termleri test edip düzenlemem gerek)

s1 = Suffix('-(n)ca',  ['ca', 'ce'],                                   'n',  True, True)  #
s2 = Suffix("-ki",     ["ki"],                                        None, False, False)  #
s3 = Suffix('-(y)la',  ['la', 'le'],                                   'y',  False, True)  #
s4 = Suffix('-ndan',   ['ndan', 'ntan', 'nden', 'nten'],              None, False, False)
s5 = Suffix("-dan",    ['dan', 'tan', 'den', 'ten'],                  None, False, False)
s6 = Suffix("-nda",    ['nta', 'nte', 'nda', 'nde'],                  None, False, False)
s7 = Suffix("-da",     ['ta', 'te', 'da', 'de'],                      None, False, False)
s8 = Suffix("-na",     ['na', 'ne'],                                  None, False, False)
s9 = Suffix("-(y)a",   ['a', 'e'],                                      "y",  True, True)
s10 = Suffix("-(n)un", ['ın', 'in', 'un', 'ün'],                       "n",  True, False)
s11 = Suffix("-nu",    ['nı', 'ni', 'nu', 'nü'],                      None, False, False)
s12 = Suffix("-(y)u",  ['ı', 'i', 'u', 'ü'],                           "y", False, False)
s13 = Suffix("-ları",  ['ları', 'leri'],                              None, False, False)
s14 = Suffix("-(s)u",  ['ı', 'i', 'u', 'ü'],                           "s",  True, False)
s15 = Suffix("-(u)nuz",['nız', 'niz', 'nuz', 'nüz'],  ['ı', 'i', 'u', 'ü'], False, False)
s16 = Suffix("-un",    ['ın', 'in', 'un', 'ün'],                      None, False, False)
s17 = Suffix("-(u)muz",['mız', 'miz', 'muz', 'müz'],  ['ı', 'i', 'u', 'ü'],  False, True)
s18 = Suffix("-(u)m",  ["m"],                         ['ı', 'i', 'u', 'ü'],  False, True)
s19 = Suffix("-lar",   ['lar', 'ler'],                                 None, False, False)
s20 = Suffix("-lara",   ['lara', 'lere'],                                 None, False, False)
s21 = Suffix("-ki2",   ["ki"],                                        None, False, False)  #** ikinci **

# Bazı yapım ekleri:
s22 = Suffix('-lik',   ['lik', 'lık', 'luk', 'lük'],                   None, False, False)
s23 = Suffix('-li',    ['li', 'lı', 'lu', 'lü'],                       None, False, False)
s24 = Suffix('-cı',    ['cı', 'ci', 'çı', 'çi'],                       None, False, False)


noun_suffix_list = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s20, s21, s22, s23, s24]
noun_derivational_suffix_list = [s22, s23, s24]

