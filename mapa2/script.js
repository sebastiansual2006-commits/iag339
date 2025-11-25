const zonas = document.querySelectorAll(".zona");
const tooltip = document.getElementById("tooltip");

zonas.forEach(zona => {
    zona.addEventListener("mousemove", e => {
        tooltip.style.display = "block";
        tooltip.style.left = e.pageX + 15 + "px";
        tooltip.style.top = e.pageY + 15 + "px";
        tooltip.innerText = zona.dataset.nombre;
    });

    zona.addEventListener("mouseleave", () => {
        tooltip.style.display = "none";
    });
});


