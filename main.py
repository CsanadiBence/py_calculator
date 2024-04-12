from pyscript import document
    
def torles(event):
    document.querySelector("#szam1").value = ""
    document.querySelector("#szam2").value = ""
    document.querySelector("#eredmeny").textContent = ""
    document.querySelector("#muvelet").selectedIndex = ""