getValue =  document.getElementById("gaugeValue").textContent
gaugeValue = parseFloat(getValue)
$('.demo').kumaGauge({
    // dynamic value-up<a href="https://www.jqueryscript.net/time-clock/">date</a>. just for sample.
    value :gaugeValue
  });
  $('[name=tags]').tagify();
