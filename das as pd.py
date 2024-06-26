import pandas as pd

# 데이터 프레임 생성
data = {
    "항목": ["Initial Cost", "Annual Operating Cost", "Annual Revenue", "Proud Number"],
    "값": [1000000, 200000, 400000, "=B4/(B2+B3)"]
}

df = pd.DataFrame(data)

# 엑셀 파일로 저장
file_path = "/mnt/data/Proud_Number_Calculation.xlsx"
df.to_excel(file_path, index=False)

import ace_tools as tools; tools.display_dataframe_to_user(name="Proud Number Calculation", dataframe=df)
