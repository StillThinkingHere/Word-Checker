from english_words import get_english_words_set
from rich import print
words, output = get_english_words_set(['web2'], lower=True) , []
for word in list(str(input("Please type in a sentence and press enter to check: ")).split(" ")):
    if word in words:
        output.append(f"[green]{word}[/green]")
    else:
        output.append(f"[red]{word}[/red]")
final_output = f"{output[0]}"
for out in range(1, len(output)):
    final_output = f"{final_output} {output[out]}"
print(final_output)
