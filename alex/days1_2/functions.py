def kgs_to_lbs(fun_kgs):
    fun_lbs = 2.2 * fun_kgs
    return fun_lbs


kgs = float(input("What is your weight in kgs? "))

lbs = kgs_to_lbs(kgs)

print(lbs, "lbs")