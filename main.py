import pandas as pd
import openpyxl

data = {
    'Nome': ["God Of War Ragnarok",
             "Assassin's Creed Valhalla", 
             "Resident Evil 4 - Remake", 
             "Call of Duty - Modern Warfare 2", 
             "Far Cry 6", 
             "Marvel's Spider-Man", 
             "Ghost Recon - Breakpoint", 
             "Forza Horizon 5", 
             "Hogwarts Legacy", 
             "The Last of Us",
             "Ghost of Tsuchima"
             ],
    'Ano': [2022, 2020, 2023, 2022, 2021, 2018, 2019, 2021, 2023, 2013, 2020],
    'Empresa Desenvolvedora': [
        'Sony',
        'Ubisoft',
        'Capcom',
        'Infinity Ward',
        'Ubisoft',
        'Sony',
        'Ubisoft',
        'Playground Games',
        'Avalanche Software',
        'Sony',
        'Sony'
    ],
    'Gênero': [
        'Ação-Aventura',
        'RPG/Ação',
        'Sobrevivência',
        'Tiro',
        'Tiro',
        'Ação-Aventura',
        'Tiro',
        'Corrida',
        'RPG/Ação',
        'Sobrevivência',
        'Ação-Aventura'
    ],
    'Avaliação': [
        4.7,
        4.0,
        4.8,
        4.6,
        4.2,
        4.8,
        4.1,
        4.5,
        4.9,
        4.5,
        4.7
    ],
    'Preço': [
        349.9,
        249.9,
        299.9,
        449.9,
        149.9,
        189.9,
        99.9,
        124.5,
        299.9,
        57.5,
        189.9
    ]

}

df = pd.DataFrame(data)

excel_file = './base.xlsx'
writer = pd.ExcelWriter(excel_file, engine='openpyxl')
df.to_excel(writer, sheet_name='Sheet1', index=False)
writer.save()
writer.close()
