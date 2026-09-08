import random

quotes = [
    "The only way to do great work is to love what you do.",
    "Believe you can and you're halfway there.",
    "It always seems impossible until it's done.",
    "Success is not final, failure is not fatal."
]

def generate_quot():
    quote = random.randint(1, len(quotes))
    print("Today's quote is: ",quotes[quote-1])


while True:
    generate_quot()
    choice = input("\nGenerate another quote? (y/n): ")

    if choice.lower() != 'y':
        print("Goodbye!!")
        break