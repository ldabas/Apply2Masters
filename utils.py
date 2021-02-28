import pandas as pd
EU_countries = [
"Austria",	"Italy",
"Belgium",	"Latvia",
"Bulgaria",	"Lithuania",
"Croatia",	"Luxembourg",
"Cyprus",	"Malta",
"Czechia",	"Netherlands",
"Denmark",	"Poland",
"Estonia",	"Portugal",
"Finland",	"Romania",
"France",	"Slovakia",
"Germany",	"Slovenia",
"Greece",	"Spain",
"Hungary",	"Sweden",
"Ireland"
]

#Maybe add question do you have a bachelor's degree
persona = {"Country":"USA",
           "hasBachelors":True,
            "Subject":"Management",
            "Start":"Fall 2022",
            "Geography":"Urban",
            "Location": ["Italy"],
            "Degree":"Bachelors",
            "Language":"English",
            "Experience":3,
            "GPA":3.2,
            "GMAT":600,
            "Budget":20000}
df = pd.read_csv("LBS Hackathon Data - University Data.csv", thousands=',')

if persona["Country"] not in EU_countries:
    persona["NeedVisa"] = True


##Preference
def get_preferred_universities(person):
    uni_list = pd.DataFrame()

    region = df.SettingType==persona["Geography"]
    program = df['School Program'].str.contains(persona["Subject"], case=False)
    for location in persona["Location"]:
        location_flag = df.Country == location
        new_dat = df[region & program & location_flag]
        uni_list = uni_list.append(new_dat)


    return uni_list

## Check if applicant is eligible
def is_eligible(uni_dataframe, applicant):
    if(applicant["hasBachelors"] and applicant["GPA"]>=3.0):
        return True
    return False





if is_eligible(df, persona):
    answer = get_preferred_universities(persona)
    answer[['School Name', 'Country', 'City', 'School Program', 'Citysize', 'VISA Need (NON EU student)', 'Average GPA for admissions', 'GMAT/GRE Required --> Y/N']].to_csv(r'Results.csv', index=False)
    print([['School Name', 'Country', 'City', 'School Program', 'Citysize', 'VISA Need (NON EU student)',
            'Average GPA for admissions', 'GMAT/GRE Required --> Y/N']])


