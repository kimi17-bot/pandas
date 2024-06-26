import pandas as pd

# 데이터 프레임 생성
data = {
    "Component": ["Displacement (lbs)", "Waterline Length (Lwl) (ft)", "Displacement/Length Ratio"],
    "Value": [20000, 35, "=(B2/2240)/((B3/100)^3)"]
}

df = pd.DataFrame(data)

# 엑셀 파일로 저장
file_path = "/mnt/data/Displacement_Length_Ratio_Calculation.xlsx"
df.to_excel(file_path, index=False)

import ace_tools as tools; tools.display_dataframe_to_user(name="Displacement/Length Ratio Calculation", dataframe=df)
