// family-trackings - Script de Interatividade do Painel Satelital

document.addEventListener("DOMContentLoaded", function () {
    console.log("family-trackings: Sistema de monitoramento satelital inicializado.");

    // Função para simular o disparo de alerta de pânico/perímetro
    window.dispararAlerta = function (idDispositivo) {
        const mensagem = `🚨 ATENÇÃO: Alerta de emergência acionado para o dispositivo #${idDispositivo}!\n\nAs coordenadas geodésicas foram transmitidas com sucesso via satélite para o painel de rastreio dos pais.`;
        alert(mensagem);
        
        // Atualiza visualmente o status na tela se estiver no painel demonstrativo
        const statusElement = document.getElementById(`status-${idDispositivo}`);
        if (statusElement) {
            statusElement.innerHTML = '<span style="color: #ef4444; font-weight: bold;">ALERTA ATIVO / RESGATE EM ANDAMENTO</span>';
        }
    };
});
