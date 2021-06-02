document.addEventListener("DOMContentLoaded", function () {
    var endpoint = "/service/dashboard/web/service/data/chart/";
    $.ajax({
        method: "GET",
        url: endpoint,
        success: function (response_data) {
            dataSeries = response_data.series;
            dataLabels = response_data.labels;
            dataColors = response_data.colors;
            window.ApexCharts && (new ApexCharts(document.getElementById('chart-webservice'), {
                chart: {
                    type: "bar",
                    fontFamily: 'inherit',
                    height: 240,
                    stacked: true,
                    toolbar: {
                        show: true
                    },
                    zoom: {
                        enabled: true
                    }
                },
                plotOptions: {
                    bar: {
                        borderRadius: 8,
                        horizontal: false,
                    },
                },
                fill: {
                    opacity: 1,
                },
                series: dataSeries,
                labels: dataLabels,
                xaxis: {
                    categories: dataLabels,
                },
                legend: {
                    position: 'bottom',
                    // offsetY: 40
                },
                colors: dataColors,
            })).render();
        },
        error: function (error_data) {
            console.log("Error webservice_data_chart");
            console.log(error_data);
        }
    });
});