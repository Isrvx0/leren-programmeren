from fruitmand import fruitmand

def longest_word(fruitmand):
    return max(fruitmand, key=lambda name:len(name['name']))

aantal_letters= len(longest_word(fruitmand)['name'])
name= longest_word(fruitmand)['name']
kleur= longest_word(fruitmand)['color']
gewicht= longest_word(fruitmand)['weight']
print ('de %s (%s) heeft een %s kleur en een gewicht van %s' % (name , aantal_letters , kleur , gewicht ))