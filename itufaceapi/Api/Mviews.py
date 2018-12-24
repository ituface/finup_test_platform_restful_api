
list=[
        {
            "material_type": "PERSONAL_INFO"
        },
        {
            "material_type": "CONTACT_INFO"
        },
        {
            "material_type": "LOAN_DEMAND"
        },
        {
            "material_type": "OCCUPATION_INFO"
        },
        {
            "material_type": "INCOME_PROVE"
        },
        {
            "material_type": "ID_PHOTO"
        },
        {
            "material_type": "OPERATOR_IDENTITY"
        },
        {
            "material_type": "CREDIT_REPORT"
        },
        {
            "material_type": "ALIPAY"
        },
        {
            "material_type": "JD"
        }
    ]

data=[]
for inner in list:
    data.append(inner["material_type"])
print(data)