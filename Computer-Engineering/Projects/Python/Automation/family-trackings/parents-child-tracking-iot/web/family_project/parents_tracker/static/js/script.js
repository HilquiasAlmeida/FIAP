document.addEventListener("DOMContentLoaded", function() {
    console.log("Painel IoT Family Tracking carregado com sucesso via GitHub!");
    
    const alertBtn = document.getElementById("alertBtn");
    if (alertBtn) {
        alertBtn.addEventListener("click", function() {
            alert("Sistema de rastreamento sincronizado com os dispositivos IoT.");
        });
    }
});
