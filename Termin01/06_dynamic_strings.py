# Python3.6+
# ime = "Gregor"
# starost = 13

# moj_izpis = f"{ime:^10} je star {starost:.5f} let."
# print(moj_izpis)
# print(type(moj_izpis))

# .format() -> Python2.6 +
# ime = "Gregor"
# starost = 10
# moj_izpis = "{} je start {} let".format(ime, starost)
# print(moj_izpis)

# %-formating
ime = "Gregor"
starost = 10
moj_niz = "%s je star %d let." % (ime, starost)
print(moj_niz)