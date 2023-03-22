import gspread


class gsdb:
    def __init__(self, link):
        gs = gspread.service_account()
        self.db = gs.open_by_url(link)

    def set(self, sheet, coord: str, val):
        if type(sheet) == int:
            sheet = self.db.get_worksheet(sheet)
            sheet.update(coord, val)
        else:
            sheet = self.db.worksheet(sheet)
            sheet.update(coord, val)

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

