def compress(chars):
    count = 1
    write_index = 0
    chars.append(" ")

    for i in range(len(chars) - 1):
        if chars[i] == chars[i + 1]:
            count += 1
        else:
            chars[write_index] = chars[i]
            write_index += 1

            if count > 1:
                for digit in str(count):
                    chars[write_index] = digit
                    write_index += 1
            count = 1

    chars[:] = chars[:write_index]
    return len(chars)


chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
print(compress(chars))
