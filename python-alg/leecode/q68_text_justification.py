def fullJustify(words, maxWidth):
    res, line, width = [], [], 0

    for w in words:
        if width + len(w) + len(line) > maxWidth:
            for i in range(maxWidth - width):
                line[i % (len(line) - 1 or 1)] += " "
            res, line, width = res + ["".join(line)], [], 0
        line += [w]
        width += len(w)

    return res + [" ".join(line).ljust(maxWidth)]


words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
print(fullJustify(words, maxWidth))
