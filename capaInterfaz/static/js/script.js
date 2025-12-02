// script.js
// Ubicación: ~/AlgoritmosNumericosParaIngenieria/proyectoSSOR/capaInterfaz/static/js/script.js

let chartInstance = null;

async function calcular() {
    const ecuaciones = document.getElementById('ecuaciones').value.trim().split('\n');
    const omega = parseFloat(document.getElementById('omega').value);
    const tolerancia = parseFloat(document.getElementById('tolerancia').value);
    const iterMax = parseInt(document.getElementById('iterMax').value);

    if (!ecuaciones[0]) {
        alert('Por favor ingrese al menos una ecuación');
        return;
    }

    try {
        // Enviar datos al servidor Python
        const response = await fetch('/calcular', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                ecuaciones: ecuaciones,
                omega: omega,
                tolerancia: tolerancia,
                iter_max: iterMax
            })
        });

        if (!response.ok) {
            throw new Error('Error en el servidor');
        }

        const resultados = await response.json();
        mostrarResultados(resultados);

    } catch (error) {
        console.error('Error:', error);
        alert('Error al calcular: ' + error.message);
    }
}

function mostrarResultados(resultados) {
    // Mostrar panel de resultados
    document.getElementById('resultados').classList.add('active');

    // Mostrar validaciones
    mostrarValidaciones(resultados.validaciones);

    // Mostrar solución final
    mostrarSolucionFinal(resultados.solucion);

    // Mostrar iteraciones
    mostrarIteraciones(resultados.iteraciones_detalle);

    // Mostrar gráfica
    mostrarGrafica(resultados.errores);

    // Scroll hacia los resultados
    document.getElementById('resultados').scrollIntoView({ behavior: 'smooth' });
}

function mostrarValidaciones(validaciones) {
    const simetriaIcono = validaciones.es_simetrica ? '✅' : '❌';
    const simetriaTexto = validaciones.es_simetrica ? 'La matriz es simétrica' : 'La matriz NO es simétrica';
    
    const dominanciaIcono = validaciones.es_diagonal_dominante ? '✅' : '⚠️';
    const dominanciaTexto = validaciones.es_diagonal_dominante ? 'La matriz es diagonal dominante' : 'La matriz NO es diagonal dominante';

    document.getElementById('validaciones').innerHTML = `
        <h3 style="margin-bottom: 15px;">Verificaciones de la Matriz</h3>
        <div class="validacion-item">
            <span style="font-size: 1.5em;">${simetriaIcono}</span>
            <span><strong>Simetría:</strong> ${simetriaTexto}</span>
        </div>
        <div class="validacion-item">
            <span style="font-size: 1.5em;">${dominanciaIcono}</span>
            <span><strong>Dominancia Diagonal:</strong> ${dominanciaTexto}</span>
        </div>
    `;
}

function mostrarSolucionFinal(solucion) {
    let valoresHTML = '';
    for (let i = 0; i < solucion.length; i++) {
        valoresHTML += `<div>x${i+1} = ${solucion[i].toFixed(12)}</div>`;
    }

    document.getElementById('solucionFinal').innerHTML = `
        <h3>Solución Final Aproximada</h3>
        <div class="solucion-valores">
            ${valoresHTML}
        </div>
    `;
}

function mostrarIteraciones(iteraciones_detalle) {
    let iteracionesHTML = '<h3 style="margin-bottom: 15px;">Detalle de Iteraciones</h3>';
    
    for (let detalle of iteraciones_detalle) {
        let valoresAdelanteHTML = '';
        for (let i = 0; i < detalle.x_adelante.length; i++) {
            valoresAdelanteHTML += `<div>x${i+1} = ${detalle.x_adelante[i].toFixed(8)}</div>`;
        }

        let valoresAtrasHTML = '';
        for (let i = 0; i < detalle.x_atras.length; i++) {
            valoresAtrasHTML += `<div>x${i+1} = ${detalle.x_atras[i].toFixed(8)}</div>`;
        }

        iteracionesHTML += `
            <div class="iteracion">
                <h4>Iteración ${detalle.iteracion}</h4>
                <div style="margin-left: 15px;">
                    <strong>Adelante (SOR):</strong>
                    <div class="valores">
                        ${valoresAdelanteHTML}
                    </div>
                    <strong>Atrás (SSOR):</strong>
                    <div class="valores">
                        ${valoresAtrasHTML}
                    </div>
                    <div style="margin-top: 10px; color: #667eea;">
                        <strong>Error:</strong> ${detalle.error.toExponential(6)}
                    </div>
                </div>
            </div>
        `;
    }
    
    document.getElementById('iteraciones').innerHTML = iteracionesHTML;
}

function mostrarGrafica(errores) {
    const ctx = document.getElementById('grafica').getContext('2d');
    
    if (chartInstance) {
        chartInstance.destroy();
    }

    const labels = errores.map((_, i) => i + 1);

    chartInstance = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Error',
                data: errores,
                borderColor: '#667eea',
                backgroundColor: 'rgba(102, 126, 234, 0.1)',
                tension: 0.4,
                fill: true
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    type: 'logarithmic',
                    title: {
                        display: true,
                        text: 'Error (escala logarítmica)'
                    }
                },
                x: {
                    title: {
                        display: true,
                        text: 'Iteración'
                    }
                }
            },
            plugins: {
                legend: {
                    display: false
                }
            }
        }
    });
}

function limpiar() {
    document.getElementById('ecuaciones').value = '';
    document.getElementById('omega').value = '1.2';
    document.getElementById('tolerancia').value = '0.0001';
    document.getElementById('iterMax').value = '50';
    document.getElementById('resultados').classList.remove('active');
    
    if (chartInstance) {
        chartInstance.destroy();
        chartInstance = null;
    }
}

function salir() {
    if (confirm('¿Está seguro que desea salir?')) {
        window.close();
    }
}
