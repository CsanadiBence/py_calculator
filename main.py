from pyscript import document
def szamit(event):
    szam1 = float(document.querySelector("#szam1").value)
    szam2 = float(document.querySelector("#szam2").value)
    muvelet = document.querySelector("#muvelet").value
    document.querySelector("#eredmeny").textContent = ""

  
def torles(event):
    document.querySelector("#szam1").value = ""
    document.querySelector("#szam2").value = ""
    document.querySelector("#eredmeny").textContent = ""
    document.querySelector("#muvelet").selectedIndex = ""