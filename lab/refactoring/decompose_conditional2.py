# By Kami Bigdely
# Decompose conditional
# Reference: https://www.healthline.com/health/high-cholesterol/levels-by-age

# Blood test analysis program
total_cholostrol = 70
ldl = 30
triglyceride = 120

def good_cholestorol(total, ldl, triglyceride):
    if total < 200 and ldl < 100 and triglyceride < 150:
    # good level
        print('*** Good level of cholestrol ***')
        return 
    
    elif high_cholestorol(total, ldl, triglyceride) == True:
        return 
    
    elif tlc_diet(total, ldl, triglyceride) == True:
        return 
    else:
        print('Error: unhandled case.')

def high_cholestorol(total, ldl, triglyceride):
    if 200 < total > 240 or ldl > 160 or triglyceride >= 200:
        # High cholestrol level
        print('*** High cholestrol level ***')
        print('start taking pills such as statins')
        print('start TLC diet')
        return True 
    
def tlc_diet(total, ldl, triglyceride):
    if 200 <total_cholostrol < 240 or 130 < ldl < 160 or 150 <= triglyceride < 200:
        #TLC_diet
        print('*** Borderline to moderately elevated ***')
        print("Start TLC diet")
        print("Under this meal plan, only 7 percent of your daily calories \nshould come from saturated fat.")
        print('Some foods help your digestive tract absorb less cholesterol. For example,\nyour doctor may encourage you to eat more:')
        print('oats, barley, and other whole grains.')
        print('fruits such as apples, pears, bananas, and oranges.')

