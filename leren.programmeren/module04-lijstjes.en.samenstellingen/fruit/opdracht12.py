from fruitmand import fruitmand

def fruit_longest_word(fruitmand):
    return max(fruitmand, key=lambda name:len(name['name']))

fruit= fruit_longest_word(fruitmand)


aantal_letters= len(fruit['name'])
name= fruit['name']
kleur= fruit['color']
gewicht= fruit['weight']
print ('de %s (%s) heeft een %s kleur en een gewicht van %s' % (name , aantal_letters , kleur , gewicht ))