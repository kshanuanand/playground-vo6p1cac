import sys

def tester_import(txt):
    '''
    Permet de tester si le module n'a pas d'erreur de syntaxe ou d'indentation pour pouvoir les rattraper.
    '''
    try :
        return exec(txt)
    except IndentationError as e:
        print("Attention il y a un problème d'indentation dans votre code à la ligne "+str(e.args[1][1]),file=sys.stderr)
        print("Vérifiez bien que vous avez correctement décaler votre code",file=sys.stderr)
        print("Après un if, else, elif, for, while ou la création d'une fonction, il faut ajouter un décalage.",file=sys.stderr)
    except SyntaxError as e:
        print("Attention , il y a un problème de syntaxe dans votre code à la ligne "+str(e.args[1][1]),file=sys.stderr)
        print("Vérifiez que vous n'avez pas oublié des deux points ':' en fin de ligne par exemple.",file=sys.stderr)
    except NameError as e:
        print("Attention , vous utilisez le nom '"+str(e.args[0].split("'")[1])+"' alors qu'il n'est pas défini",file=sys.stderr)
        print("En général, c'est soit une erreur de frappe soit que vous n'avez pas créé votre variable ou fonction avant de l'utiliser.",file=sys.stderr)