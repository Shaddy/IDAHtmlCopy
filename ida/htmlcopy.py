from chtml import HtmlClipboard

class HtmlCopy:
    def __init__(self):
        self.add_to_menu()

    def modify_template(self, data):
        bgcolor = re.findall('<body bgcolor="#[a-f0-9]{6}">\n', data)
        if len(bgcolor) == 1:
            data = data.replace(bgcolor[0], "")
        background = re.findall('; background: #[a-f0-9]{6}"', data)
        if len(background) == 1:
            data = data.replace(background[0], '; font-size: 10.5px"')
        return data

    def snippet_to_html(self):
        GenerateFile(OFILE_LST, "c:\\temp\\buffer.html", SelStart(), SelEnd(),  GENFLG_GENHTML)
        data = file(r'c:\\temp\\buffer.html', 'rb').read()

        self.cb = HtmlClipboard()
        self.cb.PutFragment(self.modify_template(data))

    def add_to_menu(self):
        idaapi.add_menu_item("Edit/Plugins/", "HtmlCopy: Copy selected area to clipboard-html", "Ctrl+F2", 0, self.snippet_to_html, ()) 


if __name__ == "__main__":
    hcopy = HtmlCopy()

