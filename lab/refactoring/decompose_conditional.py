# By Kami Bigdely
# Decompose conditional: You have a complicated conditional(if-then-else) statement. Extract
# methods from the condition, then part, and else part(s).

def make_alert_sound():
    print('made alert sound.')
def make_accept_sound():
    print('made acceptance sound')


ingredients = ['sodium benzoate', 'soap']
    

def logic(array):
    toxic = {'sodium nitrate':1,'sodium benzoate':1, 
                'sodium oxide':1}

    for compound in ingredients:
        if compound in toxic:
            print('!!!')
            print('there is a toxin in the food!')    
            print('!!!')
            make_alert_sound()

        else:
    
            print('***')
            print('Toxin Free')
            print('***')
            make_accept_sound()
    
ingredients = ['sodium benzoate']
print(ingredients(ingredients))