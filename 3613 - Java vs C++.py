input_string = input()

answer = ""
before = ""

if input_string[0].isupper() or input_string[0] == "_" or input_string[-1] == "_":
    answer = "Error!"

else:
    if "_" in input_string:
        is_java = False
    else:
        is_java = True

    if is_java:

        for ele in input_string:

            if ele.isupper():
                answer += "_" + ele.lower()
                continue
            answer += ele

    else:
        before = ""
        for ele in input_string:

            if ele.isupper():
                answer = "Error!"
                break

            if ele == "_" and not before:
                before = "_"
                continue

            if before == "_":

                if ele == "_" or ele.isupper():
                    answer = "Error!"
                    break

                answer += ele.upper()
                before = ""
                continue

            answer += ele
            before = ""

print(answer)
