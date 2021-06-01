document.addEventListener("DOMContentLoaded", function () {
    var endpoint = "/service/dashboard/domain/data/chart/";
    $.ajax({
        method: "GET",
        url: endpoint,
        success: function (response_data) {
            dataSeries = response_data.series;
            dataLabels = response_data.labels;
            window.ApexCharts && (new ApexCharts(document.getElementById('chart-domain'), {
                chart: {
                    type: "bar",
                    fontFamily: 'inherit',
                    height: 40.0,
                    sparkline: {
                        enabled: true
                    },
                    animations: {
                        enabled: false
                    },
                },
                plotOptions: {
                    bar: {
                        columnWidth: '50%',
                    }
                },
                dataLabels: {
                    enabled: false,
                },
                fill: {
                    opacity: 1,
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