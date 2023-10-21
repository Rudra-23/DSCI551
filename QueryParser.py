from DDL.CreateTable import CreateTable
from DDL.DropTable import DropTable

from DML.InsertValues import InsertValues
from DML.UpdateValues import UpdateValues
from DML.DeleteValues import DeleteValues

from DisplayValues import DisplayValues

def parseQuery(query: str):

    if query.lower().startswith("create"):
        table = CreateTable(query)
        status = table.process_query()

        if status == "VALID":
            output = table.create_table()
            print(output)
        else:
            print("ERROR: ", status)

        del table

    if query.lower().startswith("insert"):
        insert = InsertValues(query)
        status = insert.process_query()

        if status == "VALID":
            message = insert.insert_values()
            print(message)
        else:
            print("ERROR: ", status)

        del insert

    if query.lower().startswith("drop"):
        drop = DropTable(query)
        status = drop.process_query()
        
        if status == "VALID":
            message = drop.drop_table()
            print(message)
        else:
            print("ERROR: ", status)

        del drop

    if query.lower().startswith("update"):
        update = UpdateValues(query)
        status = update.process_query()
        
        if status == "VALID":
            message = update.update_values()
            print(message)
        else:
            print("ERROR: ", status)

        del update

    if query.lower().startswith("delete"):
        delete = DeleteValues(query)
        status = delete.process_query()
        
        if status == "VALID":
            message = delete.delete_values()
            print(message)
        else:
            print("ERROR: ", status)

        del delete

    if query.lower().startswith("get"):
        display = DisplayValues(query)
        status = display.process_query()

        if status == "VALID":
            message = display.display_values()
            print(message)
        else:
            print("Error: ", status)
        
        del display

if __name__ == "__main__":
    print("Please Enter your Queries: ")
    while True:
        query = input("> ")
        if query == "":
            continue
        
        if query == "exit":
            break
        
        parseQuery(query)



