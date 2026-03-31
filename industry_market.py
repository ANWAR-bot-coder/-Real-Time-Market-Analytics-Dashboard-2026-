import sqlite3
import pandas as pd
import numpy as np
import os

# Database-a direct-ah C drive folder-la create panrom
db_path = r'C:\Users\Asus\project pro\industry_market.db'

# Oru vela folder illana create pannidum
if not os.path.exists(r'C:\Users\Asus\project pro'):
    os.makedirs(r'C:\Users\Asus\project pro')
    
conn = sqlite3.connect('industry_market.db')

# 1000 rows generate panrom
df_large = pd.DataFrame({
    'Job_ID': range(1, 1001),
    'Role': np.random.choice(['Data Analyst', 'AI Engineer', 'Python Dev', 'ML Engineer'], 1000),
    'City': np.random.choice(['Coimbatore', 'Bangalore', 'Chennai', 'Hyderabad'], 1000),
    'Salary_LPA': np.random.randint(4, 25, 1000)
})

df_large.to_sql('job_listings', conn, if_exists='replace', index=False)
conn.close()
print("Semma machaa! Database ippo sariyaana folder-la create aayiduchu.")
