from pyscript import document
def szamit(event):
    szam1 = float(document.querySelector("#szam1").value)
    szam2 = float(document.querySelector("#szam2").value)
    muvelet = document.querySelector("#muvelet").value
    
    res=0
    
    if muvelet=="osszeadas":
        res=szam1+szam2
    elif muvelet=="kivonás":
        res=szam1-szam2
    elif muvelet=="szorzás":
        res=szam1*szam2
    elif muvelet=="osztás":
        res=szam1/szam2
    
    document.querySelector("#result-number").textContent = res

  
def torol(event):
    document.querySelector("#szam1").value = ""
    document.querySelector("#szam2").value = ""
    document.querySelector("#result-number").textContent = "0"
    document.querySelector("#muvelet").selectedIndex = 0