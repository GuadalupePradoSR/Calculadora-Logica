import tkinter as tk

def calculate_logic():
    A = int(varA_entry.get())
    B = int(varB_entry.get())
    C = int(varC_entry.get())
    D = int(varD_entry.get())

    resultado = calculate_logic_logic(A, B, C, D)

    resultado_label.config(text=f"Resultado: {resultado}")

def calculate_logic_logic(A, B, C, D):
    expressao = "A^~BvCvA^DvC"
    simbolos = ["~","^","v","->","<>"]

    expressao = [i for i in expressao]
    variables = {"A": A, "B": B, "C": C, "D": D}
    for var in variables:
        if var in expressao:
            value = variables[var]
            for i in range(len(expressao)):
                if expressao[i] == var:
                    expressao[i] = value

    def result(a, sym, b):
        if sym == "~":
            return not b
        elif sym == "^":
            return a and b
        elif sym == "v":
            return a or b
        elif sym == "<>":
            if a == b:
                return True
            return False
        elif sym == "->":
            if a and not b:
                return False
            return True

    def solve(exp):
        for sym in simbolos:
            if sym in exp:
                i = exp.index(sym)
                if exp[i] == sym:
                    a, b, sym = exp[i-1], exp[i+1], exp[i]
                    res = result(a, sym, b)
                    if sym == "~":
                        exp[i] = res
                        exp.pop(i+1)
                    else:
                        exp[i-1] = res
                        exp.pop(i+1)
                        exp.pop(i)
                    if len(exp) == 1:
                        return exp[0]
                    return solve(exp)

    def full_solve(exp):
        if "(" not in exp:
            return solve(exp)
        inside_exp = []
        for i in range(len(exp)):
            if exp[i] == ")":
                removal_size = len(inside_exp) + 2
                break
            inside_exp.append(exp[i])
            if exp[i] == "(":
                remove_index = i
                inside_exp = []
        exp[remove_index-1] = solve(inside_exp)
        for i in range(removal_size):
            exp.pop(remove_index)
        if len(exp) == 1:
            return exp[0]
        return full_solve(exp)

    return full_solve(expressao)

root = tk.Tk()
root.title("Calculadora Lógica")

varA_label = tk.Label(root, text="Valor da variável A:")
varA_label.grid(row=0, column=0)
varA_entry = tk.Entry(root)
varA_entry.grid(row=0, column=1)

varB_label = tk.Label(root, text="Valor da variável B:")
varB_label.grid(row=1, column=0)
varB_entry = tk.Entry(root)
varB_entry.grid(row=1, column=1)

varC_label = tk.Label(root, text="Valor da variável C:")
varC_label.grid(row=2, column=0)
varC_entry = tk.Entry(root)
varC_entry.grid(row=2, column=1)

varD_label = tk.Label(root, text="Valor da variável D:")
varD_label.grid(row=3, column=0)
varD_entry = tk.Entry(root)
varD_entry.grid(row=3, column=1)

calculate_button = tk.Button(root, text="Calcular", command=calculate_logic)
calculate_button.grid(row=4, columnspan=2)

resultado_label = tk.Label(root, text="Resultado: ")
resultado_label.grid(row=5, columnspan=2)

root.mainloop()
