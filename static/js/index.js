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

    // specific generate
    $('#specific .form-row .submit')
      .off('click')
      .on('click', (event) => {
        event.preventDefault();
        this.createSpecificShortenUrl();
      });
  },
  createAutoShortenUrl: function() {
    let $elem = $('#auto');
    let $protocol = $elem.find('select.protocol')
    let $origin = $elem.find('input.origin');
    let protocol = $protocol.val();
    let origin = $origin.val();

    // check origin is empty
    if(!origin.trim()) {
      toastr.error('please input origin url');
      $origin.focus();
      return;
    }

    if (!this.validateOriginUrl(origin)) {
      toastr.error('please check url');
      $origin.focus();
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
      error: (xhr, status, message) => {
        toastr.error('fail');
      }
    });
  },
  createSpecificShortenUrl: function() {
    let $elem = $('#specific');
    let $protocol = $elem.find('select.protocol')
    let $origin = $elem.find('input.origin');
    let $specific = $elem.find('input.specific');
    let protocol = $protocol.val();
    let origin = $origin.val();
    let specific = $specific.val();

    // check input is empty
    if(!origin.trim()) {
      toastr.error('please input origin url');
      $origin.focus();
      return;
    }
    if(!specific.trim()) {
      toastr.error('please input specific shorten url');
      $specific.focus();
      return;
    }

    // validate urls
    if (!this.validateOriginUrl(origin)) {
      toastr.error('please check origin url');
      $origin.focus();
      return;
    }
    if (!this.validateSpecificShortenURL(specific)) {
      toastr.error('please check specific shorten url');
      $specific.focus();
      return;
    }

    $.ajax({
      url: '/generate',
      method: 'POST',
      data: {
        category: 'specific',
        protocol: protocol,
        origin: origin.trim(),
        specific: specific.trim()
      },
      success: (response) => {
        let $elem = $('#specific input.shorten');
        $elem.val(response.url);
        $elem.parent('.input-group').css('visibility', 'visible');
      },
      error: (xhr, status, thrown) => {
        if(xhr.status === 409) {
          toastr.error(xhr.responseJSON.message);
          $specific.focus();
        }
      }
    });
  },
  validateOriginUrl: function(url) {
    let regex = /^[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$/;
    return url.match(regex);
  },
  validateSpecificShortenURL: function(url) {
    let regex = /^[0-9a-zA-Z-]{1,25}$/;
    return url.match(regex);
  }
};