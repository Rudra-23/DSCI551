import pandas as pd

class Join():
    def __init__(self, table1, table2, col1, col2) -> None:
        self.table1 = table1
        self.table2 = table2
        self.col1 = col1
        self.col2 = col2

        self.data_dir = "./Data/"
        self.tmp_dir = "./TMP/"

        self.final_file = "_joined_"+  self.table1 + "_" + self.table2 

    def join_tables(self):

        col1 = self.col1
        col2 = self.col2
        header = False
        
        with open(self.data_dir + self.final_file + '.csv', 'a', newline="") as output:
            try:
                reader1 = pd.read_csv(self.data_dir + self.table1 + ".csv", chunksize = 1000)
                df1 = next(reader1, None)

                while df1 is not None:
                    reader2 = pd.read_csv(self.data_dir + self.table2 + ".csv", chunksize = 1000)
                    df2 = next(reader2, None)

                    if header != True:
                        header = True
                        list1 = [f"{self.table1}.{c1}" for c1 in list(df1.columns)]
                        list2 = [f"{self.table2}.{c2}" for c2 in list(df2.columns)]

                        output.write(",".join(list1 + list2) + '\n')


                    while df2 is not None:
                        for _, row1 in df1.iterrows():
                            for _, row2 in df2.iterrows():
                                row1 = dict(row1)
                                row2 = dict(row2)

                                if row1[col1] == row2[col2]:
                                    temp = []
                                    for v in row1.values():
                                        temp.append(str(v))
                                    for v in row2.values():
                                        temp.append(str(v))
                                    output.write(",".join(temp) + "\n")    

                        df2 = next(reader2, None)
        
                    df1 = next(reader1, None)

            except:
                raise SyntaxError("Error: Some error occurred with joining. Please check variables")
        