document.addEventListener("DOMContentLoaded", function () {
    var endpoint = "/financial/dashboard/data/chart/";
    $.ajax({
        method: "GET",
        url: endpoint,
        success: function (response_data) {
            dataSeries = response_data.series;
            dataLabels = response_data.labels;
            dataColors = response_data.colors;
            window.ApexCharts && (new ApexCharts(document.getElementById('chart-financial'), {
                chart: {
                    type: "line",
                    fontFamily: 'inherit',
                    height: 40.0,
                    sparkline: {
                        enabled: true
                    },
                    animations: {
                        enabled: false
                    },
                },
                fill: {
                    opacity: 1,
                },
                stroke: {
                    width: [2, 2],
                    dashArray: [0, 3],
                    lineCap: "round",
                    curve: "smooth",
                },
                series: dataSeries,
                grid: {
                    strokeDashArray: 4,
                },
                xaxis: {
                    labels: {
                        padding: 0,
                    },
                    tooltip: {
                        enabled: false
                    },
                    type: 'string',
                },
                yaxis: {
                    labels: {
                        padding: 4
                    },
                },
                labels: dataLabels,
                colors: dataColors,
                legend: {
                    show: false,
                },
            })).render();
        },
        error: function (error_data) {
            console.log(error_data);
        }
    });
});