from english_words import get_english_words_set
from rich import print
words = get_english_words_set(['web2'], lower=True)
output = []

while 1:
    # Checks if words are correct
    for word in list(str(input("Please type in a sentence and press enter to check: ")).split(" ")):
        if word.lower() in words:
            output.append(f"[green]{word}[/green]")
        else:
            output.append(f"[red]{word}[/red]")

    # Turns List to string
    final_output = f"{output[0]}"
    for iteration in range(1, len(output)):
        final_output = f"{final_output} {output[iteration]}"
    print(final_output)
