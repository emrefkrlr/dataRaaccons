function createPDF() {
    var pdf = document.getElementById("reports_view");
    var opt = {
        margin: 1,
        filename: 'raccoon_analytic_dashboard.pdf',
        image: { type: 'jpeg', quality: 1 },
        html2canvas: { scale: 2 },
        jsPDF: { unit: 'in', format: 'a4', orientation: 'portrait' }
    };
    html2pdf().set(opt).from(pdf).save();
}