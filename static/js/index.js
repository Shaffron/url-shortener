let Compressor = {
  init: function() {
    this.bindEvent();
    new ClipboardJS('.btn');
  },
  bindEvent: function() {
    // form clear
    $('#shorten_url')
      .on('show.bs.tab', (event) => {
        let $forms = $('#shorten_url form');
        let $shorten_inputs = $('#shorten_url .copy .input-group');
        $shorten_inputs.css('visibility', 'hidden');
        $forms.each(function() {
          this.reset();
        });
      });

    // auto generate
    $('#auto .form-row .submit')
      .off('click')
      .on('click', (event) => {
        event.preventDefault();
        this.createAutoShortenUrl();
      });

    // manual generate
    $('#manual .form-row .submit')
      .off('click')
      .on('click', (event) => {
        event.preventDefault();
        this.createManualShortenUrl();
      });
  },
  createAutoShortenUrl: function() {
    let $elem = $('#auto');
    let $select = $elem.find('select')
    let $input = $elem.find('input.origin');
    let protocol = $select.val();
    let origin = $input.val();

    // check origin is empty
    if(!origin.trim()) {
      toastr.error('please input origin url');
      $input.focus();
      return;
    }

    // validate url
    let regex = /^[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$/;
    if (!origin.match(regex)) {
      toastr.error('please check url');
      $input.focus();
      return;
    }

    $.ajax({
      url: '/generate',
      method: 'POST',
      data: {
        category: 'auto',
        protocol: protocol,
        origin: origin.trim()
      },
      success: (response) => {
        let $elem = $('#auto input.shorten');
        $elem.val(response.url);
        $elem.parent('.input-group').css('visibility', 'visible');
      },
      error: () => {
        toastr.error('fail');
      }
    });
  },
  createManualShortenUrl: function() {

  },
};