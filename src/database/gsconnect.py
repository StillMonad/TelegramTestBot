import gspread
import os

try:
    import src.config
except:
    pass


class Gsdb:
    def __init__(self):
        with open("service_account.json", 'w') as f:
            f.write(os.getenv('SERVICE_ACC'))

        gs = gspread.service_account("service_account.json")
        os.remove("service_account.json")
        link = os.getenv('GS_LINK')
        self.db = gs.open_by_url(link)

    @staticmethod
    def get_coord(x, y):
        return chr(x + 64) + str(y)

    def get(self, sheet, coord):
        """
        Getting value from coords, coords starts from 1
        """
        s = None
        if type(sheet) == type(1):
            s = self.db.get_worksheet(sheet)
        else:
            s = self.db.worksheet(sheet)

        if type(coord) == type("str"):
            return s.get(coord).first()
        else:
            return s.cell(*coord).value

    def get_sheet_data(self, name):
        sheet = self.db.worksheet(name)
        return sheet.get_values()

    def add_data(self, name, arr):
        sheet = self.db.worksheet(name)
        sheet.append_row(arr)

    def get_line_index_by_data(self, sheet_name, d):
        sheet = self.db.worksheet(sheet_name)
        cell = sheet.find(str(d))
        if cell is None:
            return cell
        cell = cell.row
        return cell
    def get_line_by_data(self, s_name, d):
        sheet = self.db.worksheet(s_name)
        cell = sheet.find(str(d))
        if cell is None:
            return cell
        cell = cell.row
        return sheet.row_values(cell)
