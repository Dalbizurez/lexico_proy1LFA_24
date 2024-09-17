def readFile(filepath:str) -> tuple[str]:
    file_text = ""
    error_text = ""
    try:
        file = open(filepath, "rt")
        file_text = file.read()
        file.close()
    except Exception as e:
        error_text = e.__str__()
    return file_text, error_text

