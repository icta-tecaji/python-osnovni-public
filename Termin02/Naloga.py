country_gdp = [['United States', 22996100, 22145244],
                    ['China', 17734063, 17077902],
                    ['Japan', 4937422, 4754737],
                    ['Germany', 4223116, 4066860],
                    ['United Kingdom', 3186860, 3068946],
                    ['India', 3173398, 3055982],
                    ['France', 2937473, 2828786],
                    ['Italy', 2099880, 2022184],
                    ['Canada', 1990762, 1917103],
                    ['Korea, Rep.', 1798534, 1731988]]

#naloga izpisite gdp drzave v eur
# print(len(country_gdp))
# for i in range(0, len(country_gdp)):
#     print(country_gdp[i])
# print(country_gdp[0][0])
for country in country_gdp:
    print(f"GDP dryave {country[0]} je {country[2]} EUR")