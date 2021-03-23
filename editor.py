simple = "plain bold italic inline-code".split()
editor = []
while True:
    choice = input("- Choose a formatter: ")
    if choice == "!done":
        with open("output.md", "w") as f:
            f.write("".join(editor))
        exit()
    elif choice == "!help":
        print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
        print("Special commands: !help !done")
    elif choice in simple:
        text = input("- Text: ")
        suffix = ""
        if choice == "bold":
            suffix = "**"
        if choice == "italic":
            suffix = "*"
        if choice == "inline-code":
            suffix = "`"
        editor.append(suffix + text + suffix)
    elif choice == "header":
        level = int(input("- Level: "))
        if level > 6 or level < 1:
            print("The level should be within the range of 1 to 6")
        else:
            text = input("- Text: ")
            header = ("#" * level) + " " + text + "\n"
            editor.append(header)
    elif choice == "link":
        label = input("- Label: ")
        text = input("- URL: ")
        editor.append(f'[{label}]({text})')
    elif choice == "new-line":
        editor.append("\n")
    elif choice == "ordered-list":
        n_rows = int(input("- Number of rows: "))
        while n_rows < 1:
            print("The number of rows should be greater than zero")
            n_rows = int(input("- Number of rows: "))
        else:
            for i in range(1, n_rows + 1):
                editor.append(f"{i}. " + input(f"- Row #{i}") + "\n")
    elif choice == "unordered-list":
        n_rows = int(input("- Number of rows: "))
        while n_rows < 1:
            print("The number of rows should be greater than zero")
            n_rows = int(input("- Number of rows: "))
        else:
            for i in range(1, n_rows + 1):
                editor.append(f"* " + input(f"- Row #{i}") + "\n")
    else:
        print("Unknown formatting type or command")
    print("".join(editor))
