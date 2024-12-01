import wikipedia

while True:
    search = input("Enter page title: ")
    if not search:
        print("Thank you.")
        break
    try:
        page = wikipedia.page(search, autosuggest=True)
        print(page.title)
        print(page.summary[:500])  # Print first 500 characters
        print(page.url)
    except wikipedia.DisambiguationError as e:
        print("We need a more specific title. Try one of the following:")
        print(e.options)
    except wikipedia.PageError:
        print(f"Page '{search}' does not exist.")
