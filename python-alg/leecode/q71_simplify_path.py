def simplifyPath(path):
    paths = path.split("/")
    print(paths)
    stack = []

    for p in paths:
        if p == "" or p == ".":
            continue

        if p == "..":
            if stack:
                stack.pop()
        else:
            stack.append(p)

    return "/" + "/".join(stack)


path = "/../"
print(simplifyPath(path))
