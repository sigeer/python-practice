import pandas

excel_path = r"./input.xlsx"
    
def read_excel(file_path: str):
    dataframe = pandas.read_excel(file_path)
    
    #  获取行数与列数
    (row_count, column_count) = dataframe.shape

    for i in range(row_count):
        print(dataframe.loc[i,"姓名"])
        
def write_excel(file_path):
    # 创建一个DataFrame对象
    data = {
        'Column3': ['A', 'B', 'C', 'I', 'J'],
        'Column1': [6, 7, 8, 9, 10],
            'Column2': ['F', 'G', 'H', 'I', 'J']}
    df = pandas.DataFrame(data)

    # 将DataFrame数据追加到已有的Excel文件
    with pandas.ExcelWriter(file_path, mode='w', engine='openpyxl') as writer:
        # df.to_excel按列写入，df.T.to_excel按行写入
        df.T.to_excel(writer, sheet_name='Sheet1', index=False, header=['Header1', 'Header2', 'Header3', 'Header4', 'Header5'])
    

# read_excel(excel_path)
write_excel("./out.xlsx")