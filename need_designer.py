from sys import exit


def start():
    print "Do you need a designer?"
    start_answer = raw_input()
    if start_answer == "yes":
        print "That was easy, we should talk!"
        exit(0)
    elif start_answer == "no":
        success()
    else:
        print "yes or no, please"
        start()


def success():
    print "Do you want to be successful?"
    success_answer = raw_input()
    if success_answer == "yes":
        appearance()
    elif success_answer == "no":
        money()
    else:
        print "yes or no, please"
        success()


def appearance():
    print "Do you think appearance matters?"
    appearance_answer = raw_input()
    if appearance_answer == "yes":
        busi_visual()
    elif appearance_answer == "no":
        morning()
    else:
        print "yes or no, please"
        appearance()


def money():
    print "Do you want to make money?"
    money_answer = raw_input()
    if money_answer == "yes":
        appearance()
    elif money_answer == "no":
        fulfillment()
    else:
        print "yes or no, please"
        money()


def morning():
    print "Do you look in the mirror in the morning / ",
    print "take a shower / brush your teeth?"
    morning_answer = raw_input()
    if morning_answer == "yes":
        pers_appearance()
    elif morning_answer == "no":
        print "Seriously? Eww, I think you should go back to the start!"
        exit(0)
    else:
        print "yes or no, please"
        morning()


def fulfillment():
    print "Do you want fulfillment?"
    fulfillment_answer = raw_input()
    if fulfillment_answer == "yes":
        f_dream()
    elif fulfillment_answer == "no":
        print "Ok, keep on doing whatever you are doing."
        exit(0)
    else:
        print "yes or no, please"
        fulfillment()


def f_dream():
    print "Do you want to fulfill your life's dream?"
    f_dream_answer = raw_input()
    if f_dream_answer == "yes":
        start_busi()
    elif f_dream_answer == "no":
        print "Ok, keep on doing whatever you are doing."
        exit(0)
    else:
        print "yes or no, please"
        f_dream()


def start_busi():
    print "Do you want to start your own business or maximize your ",
    print "current business's potential?"
    start_busi_answer = raw_input()
    if start_busi_answer == "yes":
        appearance()
    elif start_busi_answer == "no":
        print "Ok, keep on doing whatever you are doing."
        exit(0)
    else:
        print "yes or no, please"
        start_busi()


def pers_appearance():
    print "Does your personal appearance matter to you ",
    print "when meeting an important client?"
    pers_appearance_answer = raw_input()
    if pers_appearance_answer == "yes":
        appearance()
    elif pers_appearance_answer == "no":
        rather_buy()
    else:
        print "yes or no, please"
        pers_appearance()


def rather_buy():
    print "Would you rather buy your food from a clean shop than a filthy one?"
    rather_buy_answer = raw_input()
    if rather_buy_answer == "yes":
        appearance()
    elif rather_buy_answer == "no":
        print "Ok, keep on doing whatever you are doing."
        exit(0)
    else:
        print "yes or no, please"
        rather_buy()


def busi_visual():
    print "Do you think your business's visual identity ",
    print "represents what your business does best?"
    busi_visual_answer = raw_input()
    if busi_visual_answer == "yes":
        hire_pro()
    elif busi_visual_answer == "no":
        want_change()
    else:
        print "yes or no, please"
        busi_visual()


def want_change():
    print "Do you want to change that?"
    want_change_answer = raw_input()
    if want_change_answer == "yes":
        helpful()
    elif want_change_answer == "no":
        print "Ok, keep on doing whatever you are doing."
        exit(0)
    else:
        print "yes or no, please"
        want_change()


def hire_pro():
    print "Did you hire a professional designer to design ",
    print "your logo/website/brochure?"
    hire_pro_answer = raw_input()
    if hire_pro_answer == "yes":
        compare()
    elif hire_pro_answer == "no":
        feedback()
    else:
        print "yes or no, please"
        hire_pro()


def helpful():
    print "Do you think it would be helpful to ",
    print "have a logo/stationary/website/advertising/brochures ",
    print "that strengthen your business and attract new clients?"
    helpful_answer = raw_input()
    if helpful_answer == "yes":
        print "We should talk! www.alicenspurlin.com"
        exit(0)
    elif helpful_answer == "no":
        want_work()
    else:
        print "yes or no, please"
        helpful()


def compare():
    print "Compare your visual identity to your competitors. ",
    print "Would you hire yourself?"
    compare_answer = raw_input()
    if compare_answer == "yes":
        brand()
    elif compare_answer == "no":
        print "An attractive visual identity will strengthen your ",
        print "business, help you gain clients and lead you onward to success."
        exit(0)
    else:
        print "yes or no, please"
        compare()


def feedback():
    print "Have you recieved positive feedback about your visual ",
    print "identity from clients?"
    feedback_answer = raw_input()
    if feedback_answer == "yes":
        brand()
    elif feedback_answer == "no":
        print "An attractive visual identity will strengthen your ",
        print "business, help you gain clients and lead you onward to success."
        exit(0)
    else:
        print "yes or no, please"
        feedback()


def want_work():
    print "Do you want to work with an experienced designer, who has ",
    print "talent and expertise in setting up visual identities?"
    want_work_answer = raw_input()
    if want_work_answer == "yes":
        print "We should talk! www.alicenspurlin.com"
    elif want_work_answer == "no":
        print "What? Go back to the start!"
        exit(0)
    else:
        print "yes or no, please"
        want_work()


def brand():
    print "Are your logo and promotional materials (brochures/website/",
    print "stationary package) part of a bigger brand identity?"
    brand_answer = raw_input()
    if brand_answer == "yes":
        print "Well Done!"
        print "Business environments are constantly changing, so your visual ",
        print "identity should evolve with your business. I would be happy ",
        print "to help you out!"
        print "We should talk! www.alicenspurlin.com"
        exit(0)
    elif brand_answer == "no":
        print "A consistant visual identity helps to make a stronger, ",
        print "recognisable and trusted brand. Do you want this for ",
        print "your business?"
        brand_answer_second = raw_input()
        if brand_answer_second == "yes":
            print "We should talk! www.alicenspurlin.com"
        elif brand_answer_second == "no":
            print "What? Go back to the start!"
            exit(0)
        else:
            print "yes or no, please"
            brand()
    else:
        print "yes or no, please"
        brand()


start()
