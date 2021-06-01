document.addEventListener("DOMContentLoaded", function () {
    var endpoint = "/client/dashboard/new/client/data/chart/";
    $.ajax({
        method: "GET",
        url: endpoint,
        success: function (response_data) {
            dataSeries = response_data.series;
            dataLabels = response_data.labels;
            window.ApexCharts && (new ApexCharts(document.getElementById('chart-new-clients'), {
                chart: {
                    type: "area",
                    fontFamily: 'inherit',
                    height: 40.0,
                    sparkline: {
                        enabled: true
                    },
                    animations: {
                        enabled: false
                    },
                },
                dataLabels: {
                    enabled: false,
                },
                fill: {
                    opacity: .16,
                    type: 'solid'
                },
                stroke: {
                    width: 2,
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
                    axisBorder: {
                        show: false,
                    },
                    type: 'string',
                },
                yaxis: {
                    labels: {
                        padding: 4
                    },
                },
                labels: dataLabels,
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