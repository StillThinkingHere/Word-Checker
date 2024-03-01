from english_words import get_english_words_set;from rich import print;x,o=get_english_words_set(['web2'],lower=True),[]
while 1:
    for w in list(input("Please type in a sentence and press enter to check: ").split(" ")):o.append(f"[green]{w}[/green]")if w.lower() in x else o.append(f"[red]{w}[/red]")
    f=f"{o[0]}"
    for i in range(1,len(o)):f=f"{f} {o[i]}"
    print(f)
