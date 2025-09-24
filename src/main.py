import subprocess

mapping = {
"കാണിക്കുക":"print","kaanikku":"print",
"എടുക്കുക":"input","eduthu":"input",
"എങ്കിൽ":"if","enkil":"if",
"അഥവാ എങ്കിൽ":"elif","athavaenkil":"elif",
"അല്ലെങ്കിൽ":"else","allenkil":"else",
"വേണ്ടി":"for","vendiy":"for",
"കാലം":"while","kalam":"while",
"പരിഭാഷിക്കുക":"def","paribhashikku":"def",
"വിഭാഗം":"class","vibhagam":"class",
"തിരിച്ച്":"return","tirichu":"return",
"മുറിക്കുക":"break","murikku":"break",
"തുടരുക":"continue","thudaru":"continue",
"അകത്തു വരുത്തുക":"import","akathuvaru":"import",
"നിന്ന്":"from","ninnum":"from",
"ആയായി":"as","ayitu":"as",
"കൂടെ":"with","koodi":"with",
"ശ്രമിക്കുക":"try","sramikku":"try",
"വിട്ട്":"except","vitte":"except",
"അവസാനത്ത്":"finally","avasanam":"finally",
"സത്യം":"True","satya":"True",
"മിഥ്യ":"False","mithya":"False",
"ഒന്നുമില്ല":"None","onnumilla":"None",
"allengil":"or","അല്ലെങ്കില്":"or"
}

def translate(code: str) -> str:
    keys = sorted(mapping.keys(), key=lambda x: -len(x))
    for k in keys:
        code = code.replace(k, mapping[k])
    return code

def run_mllang_file(filename="test.ml"):
    with open(filename, "r", encoding="utf-8") as f:
        mal_code = f.read()
    py_code = translate(mal_code)
    with open("temp.py", "w", encoding="utf-8") as f:
        f.write(py_code)
    subprocess.run(["python3", "temp.py"])

if __name__ == "__main__":
    run_mllang_file()
