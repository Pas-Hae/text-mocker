import pyperclip

class textmocker:
    def __init__(self, text):
        self.text = text # Objekt mit Text initialisieren

    def mock(self):
        resultat = '' # Leere Zeichenfolge für Resultat
            
    # Durch jeden Charakter im Text iterieren. i ist Index
        for i, char in enumerate(self.text):
            
            # Methode isalpha wird verwendet um zu überprüfen ob Charackter Buchstabe ist
            if char.isalpha():
                
                if i % 2 == 1:
                    resultat += char.upper() # Ungerader Index = Buchstabe wird zu Grossbuchstabe
                else:
                    resultat += char.lower() # Gerader Index = Buchstabe wird zu Kleinbuchstabe

            # Wenn Charakter kein Buchstabe ist, wird er unverändert hinzugefügt
            else:
                resultat += char
        
        # resultat wird mit Anführungszeichen zurückgegeben
        return f'"{resultat}"'
    
    # Text wird verändert und in Zwischenablage kopiert
    def kopieren_zwischenablage(self):
        text_neu = self.mock() # Text wird mit mock-Methode verändert
        pyperclip.copy(text_neu)
        print('Text wurde in Zwischenablage kopiert')

text = input('Text Eingeben: ')
text_mocker = textmocker(text)
text_mocker.kopieren_zwischenablage()



